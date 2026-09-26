# The Miller's Tally Stick
# Pinned by the miller of bitwick, beside the flour scales.
# 
# Every sack of grain that goes through the mill is recorded as a character notched onto a tally stick.
# Before a stick is filed away, the miller squares off both ends, shaving away the same number of notches from
# the front and from the back.
# 
# You are given stick, a string, and k, a non-negative integer.
# 
# Write trim_stick(stick, k), which returns a string: the characters of stick that remain after removing the first `k`
# characters and the last `k` characters. If the length of stick is less than or equal to 2 * k, return the empty string.
# 
# `stick` is never modified; a new string is returned.

def trim_stick(stick, k):
    if len(stick) <= 2*k:
        return ""

    if k == 0:
        return stick

    return stick[k:-k]