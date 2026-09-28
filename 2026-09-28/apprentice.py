# The Sluice-Keeper's Cistern Ledger
# 
# The sluice-keeper above bitwick tends a stone cistern and writes one number in her ledger each day:
# the water that ran in, or (as a negative number) the water the town drew out. The cistern holds only so much.
# Water that arrives when the cistern is already brimming runs over the lip and is lost down the hill;
# water the town asks for when the cistern is dry is simply never delivered. She wants the season's totals.
# 
# Write tally_cistern(cap, start, flow).
# 
#     cap is an integer, the cistern's capacity, cap >= 0.
#     start is an integer, the level at the start of the season, with 0 <= start <= cap.
#     flow is a list of integers, the ledger entries in order. Each may be positive, negative, or zero.
# 
# The level begins at start. Process the entries in order. For each entry, add it to the level. If the level is then above cap,
# the excess above cap is spilled and the level becomes cap. If the level is then below 0, the amount below 0 is a shortfall
# and the level becomes 0.
# 
# Return a list of three integers:
#   - the level after the last entry,
#   - the total spilled over the whole season,
#   - and the total shortfall over the whole season, in that order.
#   - With an empty flow, return the starting level and two zeros.

def tally_cistern(cap, start, flow):
    level = start
    spillage = 0
    shortfall = 0
    for day in flow:
      level += day
      if level > cap:
        spillage += (level - cap)
        level = cap
      elif level <= 0:
        shortfall += level
        level = 0

    return [level, spillage, abs(shortfall)]
    