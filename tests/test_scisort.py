from scisort import scisort_keygen, scisort_keygen_pandas

import pandas as pd

from pandas.testing import assert_series_equal

tree = [
    ".flake8",
    "data",
    "data/a (11).csv",
    "data/a (8).csv.gz",
    "data/README.md",
    "README.md",
    "scripts",
    "installation.R",
    "requirements.txt",
    "tests"
]

tree_expected = [
    "README.md",
    "installation.R",
    "requirements.txt",
    ".flake8",
    "data",
    "data/a (8).csv",
    "data/a (11).csv.gz",
    "data/README.md",
    "scripts",
    "tests"
]


def test_keygen_sorted():

    assert sorted(tree, key=scisort_keygen) == tree_expected


def test_keygen_pandas():

    s = pd.Series(tree)
    s_exp = pd.Series(tree_expected)

    assert_series_equal(
        s.sort_values(ignore_index=True, key=scisort_keygen_pandas),
        s_exp
    )
