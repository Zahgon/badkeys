import argparse
import json
import re
import signal
import sys

from . import __version__
from .allkeys import loadextrabl, urllookup
from .checks import (_checkkey, allchecks, checkcrt, checkrsa, checksshpubkey, defaultchecks,
                     detectandcheck, warningchecks)
from .dkim import parsedkim
from .dnssec import checkdnskey
from .jwk import checkjwk
from .scanssh import scanssh
from .scantls import scantls
from .update import update_bl
from .utils import _errexit, _esc, _getret, _setret, _warnmsg

MAXINPUTSIZE = 2048000

count = 0

PRECRT = "-----BEGIN CERTIFICATE-----\n"
POSTCRT = "\n-----END CERTIFICATE-----\n"

_parseerrmsg = {
    "privleak": "Private instead of public key",
    "keyparseerror": "Error decoding DER/ASN.1 key structure",
    "expectedrsa": "Wrong key type, expected RSA key",
    "wrongkeylength": "Wrong key length",
    "unknowntype": "Unknown key type",
}


def _sighandler(_signum, _handler):
    pass


def _printresults(key, where, args):
    pass


def runcli():
    pass
