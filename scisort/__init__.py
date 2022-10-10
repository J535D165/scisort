try:
    from scisort._version import __version__
    from scisort._version import __version_tuple__
except ImportError:
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)


from scisort.keygen import scisort_keygen
from scisort.keygen import scisort_keygen_pandas

__all__ = ["scisort_keygen", "scisort_keygen_pandas"]
