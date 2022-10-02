import logging
from pathlib import Path

import natsort as ns

from scisort.api import MatchGroup
from scisort.api import Pattern

SCISORT_DEFAULT = MatchGroup(
    [
        # level: Landing docs
        MatchGroup([Pattern(regexp=r"read[-_\s]{0,1}me.*")], name="doc_landing"),
        # level: License
        MatchGroup([Pattern(regexp=r"license.*")], name="license"),
        # level: Installation
        MatchGroup(
            [
                Pattern(regexp=r"installation.*"),
                Pattern(regexp=r"install.*"),
                Pattern(regexp=r"setup.*"),
                Pattern(s="requirements.txt"),
            ],
            name="installation",
        ),
        # level: Citation
        MatchGroup([Pattern(regexp=r"citation.*")], name="citation"),
        # level: Data
        MatchGroup(
            [
                MatchGroup(
                    [
                        Pattern(regexp=r"raw[-_\s]{0,1}data.*"),
                        Pattern(regexp=r"data[-_\s]{0,1}raw.*"),
                    ]
                ),
                MatchGroup(
                    [
                        Pattern(regexp=r"clean[-_\s]{0,1}data.*"),
                        Pattern(regexp=r"data[-_\s]{0,1}clean.*"),
                    ]
                ),
                Pattern(regexp=r"data.*"),
            ],
            name="data",
        ),
        # level: Scripts
        MatchGroup(
            [
                Pattern(regexp=r"scripts.*"),
                Pattern(regexp=r"src.*"),
                Pattern(regexp=r"code.*"),
            ],
            name="scripts",
        ),
        # level: Results
        MatchGroup(
            [Pattern(regexp=r"output.*"), Pattern(regexp=r"results.*")], name="results"
        ),
    ]
)


def scisort_keygen(f, pattern=SCISORT_DEFAULT, **kwargs):
    """Key for scientific file sorting."""

    def _matcher(s, group_or_pattern, rank=tuple()):

        if isinstance(group_or_pattern, MatchGroup):

            for rank_sub, match_obj in enumerate(group_or_pattern.match_objs):
                m = _matcher(s, match_obj, rank + (rank_sub,))
                if m:
                    return m
        elif isinstance(group_or_pattern, Pattern):
            if group_or_pattern.score(s):

                k = ((rank, ns.natsort_keygen(alg=ns.PATH, **kwargs)(s)),)
                return k
        else:
            raise ValueError("Matcher object not correctly configured")

    res = tuple()
    for fpart in Path(f).parts:

        m = _matcher(fpart, pattern)

        if m is None:
            k = (
                (
                    (len(pattern.match_objs),),
                    ns.natsort_keygen(alg=ns.PATH, **kwargs)(fpart),
                ),
            )
            res = res + k
            continue

        res = res + m

    logging.debug(res)

    return res


def scisort_keygen_pandas(s, **kwargs):

    return s.map(lambda x: scisort_keygen(x, **kwargs))
