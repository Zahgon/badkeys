import re

# Find suspicious patterns of 16 repeating bytes
_bprex = re.compile(rb"(.)\1{15}")


def pattern(n, e=0):  # noqa: ARG001
    pass
