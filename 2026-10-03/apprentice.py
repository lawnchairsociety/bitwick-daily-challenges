# The Amber Caravan's Salt Road
# 
# The Amber Caravan means to cross the Saltglass Waste, and the Guild of Dune-Pilots will pay for a reckoning
# of how far its water will carry it before anyone sets out.
# 
# The caravan's skins hold at most cap units of water, and it leaves the last well with them full.
# The road is a list legs of integers, walked in order from index 0:
# 
#   - A leg with value 0 or greater is a dry stretch. Crossing it costs exactly that many units of water.
#     The caravan can cross it only if the water it is carrying is at least the leg's value. Water may fall
#     to exactly 0, and the caravan can still go on.
#   - A leg with a negative value is a spring. Passing it adds the absolute value of that number to the
#     water carried. The water carried never rises above cap, and anything beyond that is lost.
# 
# Write first_stranded_leg(cap, legs):
# 
#     cap is an integer, 0 or greater.
#     legs is a list of integers, possibly empty.
# 
# Return the 0-based index of the first dry stretch the caravan does not have enough water to cross.
# If the caravan crosses every leg, return -1.

def first_stranded_leg(cap, legs):
    days = 0
    water = cap
    for leg in legs:
        water -= leg
        if water > cap:
            water = cap
            
        if water < 0:
            break
        else:
            days += 1
    if days == len(legs):
        days = -1
    return days