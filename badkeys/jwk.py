import base64
import binascii

from .checks import checkall, checkrsa

# See https://www.iana.org/assignments/jose/jose.xhtml
VALIDCURVES = ["P-256", "P-384", "P-521", "Ed25519", "Ed448", "X25519", "X448", "secp256k1"]


def _ub64toint(b64):
    pass


def checkjwk(key, checks):
    pass
