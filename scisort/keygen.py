import logging
from pathlib import Path

import natsort as ns

from scisort.api import Group
from scisort.api import Pattern

SCISORT_DEFAULT = Group(
    [
        # level: Landing docs
        Group([Pattern(regexp=r"read[-_\s]{0,1}me.*")], name="doc_landing"),
        # level: License
        Group([Pattern(regexp=r"license.*")], name="license"),
        # level: Installation
        Group(
            [
                Pattern(regexp=r"installation.*"),
                Pattern(regexp=r"install.*"),
                Pattern(regexp=r"setup.*"),
                Pattern(s="requirements.txt"),
            ],
            name="installation",
        ),
        # level: Citation
        Group([Pattern(regexp=r"citation.*")], name="citation"),
        # level: Config & hidden
        Group([Pattern(regexp=r"\..*")], name="config"),
        # level: Executables
        Group(
            [
                Pattern(regexp=r".*\.sh"),
                Pattern(regexp=r".*\.bat"),
                Pattern(regexp=r".*\.bash"),
                Pattern(regexp=r".*\.exe"),
            ],
            name="executable",
        ),
        # level: Data
        Group(
            [
                Group(
                    [
                        Pattern(regexp=r"raw[-_\s]{0,1}data.*"),
                        Pattern(regexp=r"data[-_\s]{0,1}raw.*"),
                    ]
                ),
                Group(
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
        Group(
            [
                Pattern(regexp=r"scripts.*"),
                Pattern(regexp=r"src.*"),
                Pattern(regexp=r"code.*"),
            ],
            name="scripts",
        ),
        # level: Results
        Group(
            [Pattern(regexp=r"output.*"), Pattern(regexp=r"results.*")], name="results"
        ),
        # level: Tests
        Group([Pattern(regexp=r"test.*")], name="tests"),
    ]
)


def scisort_keygen(f, pattern=SCISORT_DEFAULT, **kwargs):
    """Key for scientific file sorting."""

    def _matcher(s, group_or_pattern, rank=tuple()):

        if isinstance(group_or_pattern, Group):

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
