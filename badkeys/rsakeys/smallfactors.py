import functools

import gmpy2

MAX_PRIME = 65537


@functools.cache
def _gensmallprimes():
    # Generate product of all primes <= MAX_PRIME.
    # We calculate this once per program run, we could precalculate the
    # constant, but it's fast enough to calculate on the fly.
    pass


def smallfactors(n, e=0):  # noqa: ARG001
    # Don't try to factor nonsensical keys
    pass
