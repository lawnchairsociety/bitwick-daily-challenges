# The Rising Storms of the Brasswind Spires
# 
# High on the Brasswind Spires, the Weatherwrights' Lodge keeps a record of every storm that breaks over the peaks.
# Each thunderclap is written down as an integer loudness, in the order it was heard. The Lodge pays a bounty to anyone
# who can cut a storm's record into its rising rolls, so the storm-readers can study how each surge of thunder built.
# 
# A rising roll is a run of consecutive thunderclaps in which every clap is strictly louder than the one immediately before it.
# Each roll is made as long as possible.
# 
# Write rising_rolls(claps), where claps is a list of integers giving the loudness of each thunderclap in order.
# 
# Return a list of lists of integers: the claps split into consecutive rising rolls, in their original order.
# 
#   - Joining the rolls end to end gives back claps exactly.
#   - Within each roll, every value is strictly greater than the value before it.
#   - A clap that is equal to or quieter than the clap immediately before it begins a new roll.
#   - A roll may contain a single clap.
#   - If claps is empty, return an empty list.

def rising_rolls(claps):
    if not claps:
        return []
        
    rolls = []
    current_roll = [claps[0]]

    for previous, current in zip(claps, claps[1:]):
        if current <= previous:
            rolls.append(current_roll)
            current_roll = [current]
        else:
            current_roll.append(current)
    
    rolls.append(current_roll)
    return rolls