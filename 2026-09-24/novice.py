# The Miller's Whole-Stone Tally
# 
# The mill at the edge of bitwick weighs every sack on a scale that reads fractions, but the tally board nailed
# above the hopper has room only for whole numbers. The miller wants the board filled in before the carts arrive.
# 
# weights is a list of non-negative numbers, one per sack, each a weight in stones.
# 
# Write tallyStones(weights), which returns a new list of the same length, in the same order.
# Each entry is the matching weight rounded to the nearest whole stone, and a weight lying exactly
# halfway between two whole stones rounds up to the larger one. Every returned value is a whole number.
# An empty list of weights returns an empty list.

def tally_stones(weights):
    tally = []
    for weight in weights:
        tally.append(int((weight + 0.5) // 1))
    return tally




print(tally_stones([2.5, 2.4, 2.6]))      # output: [3, 2, 3]
print(tally_stones([0.5, 3.5]))           # output: [1, 4]
print(tally_stones([]))                   # output: []