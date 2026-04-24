import base64
import binascii

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, rsa


def parsedkim(line):

    # remove escaped quote characters, they can break our parser
    pass
