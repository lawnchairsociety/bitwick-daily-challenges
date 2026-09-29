# The Ferryman's Toll at Grainmouth Dock
# 
# The mill above bitwick sends its harvest across the river, and the ferryman at Grainmouth Dock will not haggle.
# 
# Each barge carries at most cap sacks of grain. The ferryman charges fee coins for every barge that leaves the dock,
# whether it is loaded to the rim or carrying a single sack. All the grain must cross.
# 
# Write ferry_toll(sacks, cap, fee), where:
# 
#   - sacks is a non-negative integer: the number of sacks waiting on the dock.
#   - cap is an integer of 1 or more: the most sacks one barge can carry.
#   - fee is a non-negative integer: the coins charged per departing barge.
# 
# Return a single integer: the total number of coins owed to the ferryman for moving all the grain across.

def ferry_toll(sacks, cap, fee):
    return (sacks // cap) * fee + (fee if sacks % cap > 0 else 0)