import re


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


class Group(object):
    """docstring for Group"""

    def __init__(self, match_objs, name=None):
        super(Group, self).__init__()
        self.match_objs = match_objs
        self.name = name
