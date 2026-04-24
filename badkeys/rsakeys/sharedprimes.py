from importlib.resources import files

import gmpy2

_moduli = {}

_supported_bits = [512, 768, 1024, 2048, 4096]


def sharedprimes(n, e=0):  # noqa: ARG001
    pass
