# The Oracle Bones of Quenmoor
# 
# The seers of Quenmoor carve each prophecy onto a strip of bone as a line of glyphs.
# Before the bone leaves the shrine, the seers add warding glyphs to it: the same number at the
# front as at the back. An adventurer who carries a bone to the far villages must read out only
# the prophecy between the wards.
# 
# Write read_prophecy(glyphs, n), where:
# 
#   - glyphs is a string, the full line carved on the bone (it may be empty).
#   - n is a non-negative integer, the number of warding characters at each end.
# 
# Return a string: glyphs with its first n characters and its last n characters removed, with the
# remaining characters kept in their original order.
# 
# If n is 0, return glyphs unchanged. If glyphs has 2 * n characters or fewer,
# nothing is left between the wards, so return the empty string "".

def read_prophecy(glyphs, n):
    if n == 0:
        return glyphs
    return glyphs[n:-n]