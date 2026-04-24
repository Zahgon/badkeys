import contextlib
import io

from .checks import checksshpubkey, defaultchecks
from .utils import _errexit


def scanssh(host, port=22, checks=defaultchecks.keys()):
    pass
