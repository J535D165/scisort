import re

import natsort as ns

FILE_RANKING = [
    # level 0: Landing docs
    [re.compile("read[-_]{0,1}me.*", flags=re.IGNORECASE)],
    # level 1: License
    [re.compile("license.*", flags=re.IGNORECASE)],
    # level 2: Installation
    [
        re.compile("installation.*", flags=re.IGNORECASE),
        re.compile("install.*", flags=re.IGNORECASE),
        re.compile("setup.*", flags=re.IGNORECASE),
        "requirements.txt",
    ],
    # level 3: Citation
    [
        re.compile("citation.*", flags=re.IGNORECASE)
    ],
    # level 4: Data
    [
        re.compile("data.*", flags=re.IGNORECASE)
    ],
    # level 5: Scripts
    [
        re.compile("scripts.*", flags=re.IGNORECASE),
        re.compile("src.*", flags=re.IGNORECASE),
        re.compile("code.*", flags=re.IGNORECASE),
    ],
    # level 6: Results
    [
        re.compile("output.*", flags=re.IGNORECASE),
        re.compile("results.*", flags=re.IGNORECASE)
    ]
]


def scisort_keygen(f, alg=ns.PATH, **kwargs):
    """Key for scientific file sorting.

    """

    for rank, patterns in enumerate(FILE_RANKING):
        for p in patterns:
            if (isinstance(p, re.Pattern) and p.match(str(f))) or \
                    (isinstance(p, str) and f == p):
                return (rank,) + ns.natsort_keygen(alg=alg, **kwargs)(f)


    else:
        return (len(FILE_RANKING),) + ns.natsort_keygen(alg=alg, **kwargs)(f)
