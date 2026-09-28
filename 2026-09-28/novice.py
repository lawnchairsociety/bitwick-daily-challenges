# The Cooper's Middle Stave
# 
# The cooper of bitwick brands the middle of every barrel she builds, and she needs a tally of which staves get the iron.
# 
# A barrel is given as a list of strings, each the name of one stave, laid out in the order they sit around the hoop.
# 
# Write middle_staves(staves), which takes that list and returns a new list of strings:
# 
#   - If the list has an odd number of staves, return a list containing only the single middle stave.
#   - If the list has an even number of staves, return a list containing the two middle staves,
#     in the same order they appear in the input.
#   - If the list is empty, return an empty list.
# 
# The input list must not be modified.

def middle_staves(staves):
    if len(staves) == 0:
        return []
    if len(staves) % 2 == 1:
        return [staves[len(staves) // 2]]
    if len(staves) % 2 == 0:
        return [staves[(len(staves) // 2) - 1], staves[(len(staves) // 2)]]