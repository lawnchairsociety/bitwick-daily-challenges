# The Cooper's Tally at the Brimming Barrel
# 
# The cooper behind the Brimming Barrel fills her barrels from a row of clay jugs. Every barrel takes
# the same number of jugs, and she will not cart a barrel to market unless it is
# completely full — whatever jugs are left after the last full barrel stay on the shelf.
# 
# Write tallyBarrels(jugs, size).
# 
#    - jugs is an integer, 0 or greater: how many jugs are on the shelf.
#    - size is an integer, 1 or greater: how many jugs fill one barrel exactly.
# 
# Return a list (array) of exactly two integers: first the number of completely filled barrels,
# then the number of jugs left over.

def tally_barrels(jugs, size):
    barrels = jugs // size
    left_over = jugs % size
    return [barrels, left_over]



print(tally_barrels(29, 12))    # output: [2, 5]
print(tally_barrels(24, 12))    # output: [2, 0]
print(tally_barrels(7, 12))     # output: [0, 7]
print(tally_barrels(0, 5))      # output: [0, 0]