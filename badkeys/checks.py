import hashlib
import warnings

import cryptography
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh, dsa, ec, ed448, ed25519, rsa, x448, x25519

from .allkeys import blocklist
from .dsakeys import dsasparse
from .rsakeys import (fermat, pattern, roca, rsabias, rsainvalid, rsapoly, rsarecover, rsawarnings,
                      sharedprimes, smalld, smallfactors, xzbackdoor)

# List of available checks
defaultchecks = {
    "fermat": {
        "type": "rsa",
        "function": fermat,
        "desc": "Fermat factorization / close prime vulnerability",
    },
    "roca": {
        "type": "rsa",
        "function": roca,
        "desc": "Return of the Coopersmith Attack (ROCA) vulnerability",
    },
    "rsainvalid": {
        "type": "rsa",
        "function": rsainvalid,
        "desc": "RSA keys with invalid values",
    },
    "rsapoly": {
        "type": "rsa",
        "function": rsapoly,
        "desc": "0-byte pattern in modulus allowing polynomial factoring",
    },
    "sharedprimes": {
        "type": "rsa",
        "function": sharedprimes,
        "desc": "Shared prime factors (batchgcd)",
    },
    "smalld": {
        "type": "rsa",
        "function": smalld,
        "desc": "Small private d (Wiener's attack)",
    },
    "smallfactors": {
        "type": "rsa",
        "function": smallfactors,
        "desc": "Small prime factors (<=65537, usually corrupt)",
    },
    "blocklist": {
        "type": "all",
        "function": blocklist,
        "desc": "Blocklists of compromised keys",
    },
    "dsasparse": {
        "type": "dsa",
        "function": dsasparse,
        "desc": "DSA sparse key vulnerability"
    }
}

warningchecks = {
    "rsawarnings": {
        "type": "rsa",
        "function": rsawarnings,
        "desc": "RSA key size and exponent warnings",
    },
    "rsabias": {
        "type": "rsa",
        "function": rsabias,
        "desc": "RSA modulus with bias of 0/1 bits",
    },
}

# These lead to a problematic rate of false positives and
# have limited value. They may be removed in the future.
extrachecks = {
    "pattern": {
        "type": "rsa",
        "function": pattern,
        "desc": "Implausible repetition pattern in modulus",
    },
    "xzbackdoor": {
        "type": "rsa",
        "function": xzbackdoor,
        "desc": "xz backdoor payload in RSA n",
    },
}

allchecks = defaultchecks | warningchecks | extrachecks

# cryptography warns about SSH DSA keys being deprecated.
# For now, disable the warnings. Needs a better long-term solution.
warnings.filterwarnings("ignore", category=cryptography.utils.CryptographyDeprecationWarning,
                        module="badkeys.checks")


def _checkkey(key, checks, keyrecover=False):
    pass


def checkrsa(n, e=65537, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checkdsa(y, p=0, checks=defaultchecks.keys()):
    pass


def checkall(x, checks=defaultchecks.keys()):
    pass


def _reterr(rtype, ex):
    pass


def checkpubkey(rawkey, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checkprivkey(rawkey, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checkcrt(rawcert, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checkcsr(rawcsr, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checksshprivkey(sshkey, checks=defaultchecks.keys(), keyrecover=False):
    pass


def checksshpubkey(sshkey, checks=defaultchecks.keys(), keyrecover=False):
    pass


def detectandcheck(inkey, checks=defaultchecks.keys(), keyrecover=False):
    pass
