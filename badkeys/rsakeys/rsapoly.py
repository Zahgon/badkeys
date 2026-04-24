# SPDX-License-Identifier: MIT
# Copyright (c) Hanno BÃ¶ck
#
# Part of badkeys: https://badkeys.info/

from .rsabias import _bitpct
from .smallfactors import smallfactors


def _checkbits(n, width, bitmask):
    # Skip the first chunk, it may contain larger
    # values due to next prime calculation
    pass


def rsapoly(n, e=0):  # noqa: ARG001
    pass
