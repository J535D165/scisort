from setuptools_scm import get_version

from scisort.keygen import scisort_keygen
from scisort.keygen import scisort_keygen_pandas

__all__ = ["scisort_keygen", "scisort_keygen_pandas"]

__version__ = get_version()
