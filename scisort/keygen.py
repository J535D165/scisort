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
        Pattern(regexp=r"\..*"),
        # level: All other files without extensions
        Pattern(regexp=r".*\..*", stop_search=False),
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


def scisort_keygen(pattern=SCISORT_DEFAULT, **kwargs):
    """Key for scientific file sorting.

    Arguments
    ---------
    pattern: scisort.api.Group
        Sort pattern or algorithm composed from groups and
        Patterns.
    **kwargs:
        Additional keyword arguments to be passed to
        natsort.natsort_keygen.

    Returns
    -------

    type:
        A function that parses input for scientific sorting that
        is suitable for passing as the key argument to functions
        such as sorted.
    """

    def _scisort_key(f, pattern=SCISORT_DEFAULT, **kwargs):
        def _matcher(f_sub, gr, rank=tuple()):

            if not isinstance(gr, Group):
                raise ValueError("Expected Group")

            latest_k = None

            # iter over patterns
            for rank_group, match_obj in enumerate(gr.match_objs):

                if isinstance(match_obj, Group):
                    k = _matcher(
                        f_sub,
                        match_obj,
                        rank=rank + (rank_group,),
                    )

                    if k and match_obj.stop_search:
                        latest_k = k
                        return latest_k

                # the object is a pattern
                if isinstance(match_obj, Pattern):

                    # there is a match with the file/folder
                    if match_obj.score(f_sub):

                        # set the result of the sorting to k
                        latest_k = (
                            (
                                rank + (rank_group,),
                                ns.natsort_keygen(alg=ns.PATH, **kwargs)(f_sub),
                            ),
                        )

                        # stop the search if given
                        if match_obj.stop_search:
                            return latest_k

            return latest_k

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

    return _scisort_key


def scisort_keygen_pandas(**kwargs):
    """Key for scientific file sorting in Pandas.

    Arguments
    ---------
    pattern: scisort.api.Group
        Sort pattern or algorithm composed from groups and
        Patterns.
    **kwargs:
        Additional keyword arguments to be passed to
        natsort.natsort_keygen.

    Returns
    -------

    type:
        A function that parses input for scientific sorting that
        is suitable for passing as the key argument to pandas sort
        functions.
    """

    def _scisort_key_pandas(s, **kwargs):

        return s.map(scisort_keygen(**kwargs))

    return _scisort_key_pandas
