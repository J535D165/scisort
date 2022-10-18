import pandas as pd
from pandas.testing import assert_series_equal

from scisort import scisort_keygen
from scisort import scisort_keygen_pandas

tree = [
    ".flake8",
    "data",
    "data/a (11).csv",
    "data/a (8).csv.gz",
    "data/readme.md",
    "jobs.sh",
    "random_file.xyz",
    "README.md",
    "scripts",
    "installation.R",
    "requirements.txt",
    "tests",
]

tree_expected = [
    "README.md",
    "installation.R",
    "requirements.txt",
    ".flake8",
    "random_file.xyz",
    "jobs.sh",
    "data",
    "data/readme.md",
    "data/a (8).csv.gz",
    "data/a (11).csv",
    "scripts",
    "tests",
]


def test_keygen_readme():

    assert scisort_keygen()("readme.md")[0][0][0] == 0


def test_keygen_jobs():

    assert scisort_keygen()("jobs.sh")[0][0][0] == 6


def test_keygen_no_match():

    assert scisort_keygen()("jobs.xyz")[0][0][0] == 5


def test_keygen_data():

    assert scisort_keygen()("data")[0][0][0] == 7


def test_keygen_sorted():

    assert sorted(tree, key=scisort_keygen()) == tree_expected


def test_keygen_pandas():

    s = pd.Series(tree)
    s_exp = pd.Series(tree_expected)

    assert_series_equal(
        s.sort_values(ignore_index=True, key=scisort_keygen_pandas()), s_exp
    )
