# The Cistern-Keeper's Tally at Tidewell
# 
# The stone cistern below Tidewell holds rain and gives it back to the village, and the keeper must file a tally at the end of each season.
# 
# You are given cap, a non-negative integer, the cistern's capacity in barrels, and flow, a list of integers read from the keeper's log in order. A positive entry is that many barrels of rain arriving; a negative entry is a demand for that many barrels to be drawn out; zero is a quiet day.
# 
# The cistern starts empty. Process the entries in order. For each entry, add it to the current level, then:
# 
#    - If the result is above cap, the excess above cap runs out of the overflow channel and is lost; the level becomes cap.
#    - If the result is below 0, the part below 0 is demand that could not be met; the level becomes 0.
#    - Otherwise the level is exactly the result.
# 
# Write cisternTally(cap, flow), which returns a list of exactly three integers:
#    - the level in the cistern after the last entry,
#    - the total number of barrels lost to overflow across the whole log,
#    - the total number of barrels of demand that went unmet across the whole log — in that order.
# 
# An empty log returns three zeros.

def cistern_tally(cap, flow):
    if len(flow) == 0:
        return [0, 0, 0]
    current_level = 0
    lost = 0
    unmet = 0
    for entry in flow:
        current_level += entry
        if current_level < 0:
            unmet = unmet - current_level
            current_level = 0
        elif current_level > cap:
            lost = lost + (current_level - cap)
            current_level = cap
    
    return [current_level, lost, unmet]


print(cistern_tally(10, [6, 7, -20, 3]))        # output: [3, 3, 10]
print(cistern_tally(0, [4, -2, 7]))             # output: [0, 11, 2]
print(cistern_tally(100, [10, -3, 5, -12]))     # output: [0, 0, 0]