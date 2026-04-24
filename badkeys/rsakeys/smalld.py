# SPDX-License-Identifier: MIT
# (c) Nao Yonashiro
# (c) Hanno BÃ¶ck
#
# Part of badkeys: https://badkeys.info/
#
# Based on:
# https://github.com/orisano/owiener/

from collections.abc import Iterable, Iterator

import gmpy2


def rational_to_contfrac(x: int, y: int) -> Iterator[int]:
    """
    ref: https://en.wikipedia.org/wiki/Euclidean_algorithm#Continued_fractions

    >>> list(rational_to_contfrac(4, 11))
    [0, 2, 1, 3]
    """
    pass


def contfrac_to_rational_iter(contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
    pass


def convergents_from_contfrac(contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
    pass


def smalld(n, e):
    # it makes no sense to test with small e
    pass
