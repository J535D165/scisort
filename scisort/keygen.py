import re

import natsort as ns


class Pattern(object):
    """File or folder object to match on."""

    def __init__(self, s=None, regexp=None, lower=True):
        super(Pattern, self).__init__()
        self.s = s
        self.regexp = regexp
        self.lower = lower

    def score(self, fp):

        if self.regexp:

            if self.lower:
                flags = re.IGNORECASE

            p = re.compile(self.regexp, flags=flags)

            return p.match(fp)

        if self.s:

            return isinstance(fp, str) and fp == self.s

        raise ValueError("Can't compute score")


class MatchGroup(object):
    """docstring for MatchGroup"""

    def __init__(self, match_objs, name=None):
        super(MatchGroup, self).__init__()
        self.match_objs = match_objs
        self.name = name


FILE_RANKING = MatchGroup(
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


def scisort_keygen(f, alg=ns.PATH, **kwargs):
    """Key for scientific file sorting."""

    def _matcher(group_or_pattern, rank=tuple()):

        if isinstance(group_or_pattern, MatchGroup):

            for rank_sub, match_obj in enumerate(group_or_pattern.match_objs):
                m = _matcher(match_obj, rank + (rank_sub,))
                if m:
                    return m
        elif isinstance(group_or_pattern, Pattern):
            if group_or_pattern.score(f):
                return rank + ns.natsort_keygen(alg=alg, **kwargs)(f)
        else:
            raise ValueError("Matcher object not correctly configured")

    m = _matcher(FILE_RANKING)

    if m is None:
        return (len(FILE_RANKING.match_objs),) + ns.natsort_keygen(alg=alg, **kwargs)(f)

    return m


def scisort_keygen_pandas(s, alg=ns.PATH, **kwargs):

    return s.map(lambda x: scisort_keygen(x, alg=alg, **kwargs))
