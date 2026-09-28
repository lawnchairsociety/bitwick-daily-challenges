# The Granary Ledger of Hollow Mill
# 
# The reeve of Hollow Mill audits the granary ledger at the end of every season. The ledger holds one whole number for each day:
#   - sacks carried in (positive),
#   - sacks carried out (negative),
#   - or a still day when nothing moved (zero).
# 
# The reeve's question is always the same. Over how many stretches of consecutive days did the granary's stock change by exactly a given amount?
# 
# Write count_stretches(days, target).
# 
#   - days is a list of integers, possibly empty. Values may be negative, positive, or zero.
#   - target is an integer.
# 
# Return an integer: the number of index pairs (i, j) with 0 <= i <= j < len(days) such that days[i] + days[i+1] + ... + days[j] equals target.
# A stretch must cover at least one day. Two stretches are different whenever they begin or end on different days, even if they cover the same numbers.

def count_stretches(days, target):
    stretches = 0
    current_stretch = 0
    stretch_map = {0: 1}
    for day in days:
      current_stretch += day
      if current_stretch - target in stretch_map:
        stretches += stretch_map[current_stretch - target]

      stretch_map[current_stretch] = stretch_map.get(current_stretch, 0) + 1
        
    return stretches