# The Wandering Comets of Ulverholm
# 
# The star-readers of Ulverholm Observatory have posted a commission. Several comets cross the sky
# above the observatory, and each one returns on a fixed rhythm. The Guild of the Brass Astrolabe
# will pay a bounty to whoever names the first night on which every one of these comets burns overhead
# together, so that the great lens can be turned on all of them at once.
# 
# The comets are described by two lists of the same length:
# 
#   - periods[i] is a positive integer, the rhythm of comet i.
#   - offsets[i] is an integer with 0 <= offsets[i] < periods[i].
# 
# Comet i is visible on night n exactly when the remainder of n divided by periods[i] equals offsets[i].
# 
# Nights are numbered from 1. Night 0 is never considered. limit is a non-negative integer, the last night the
# star-readers are willing to wait for.
# 
# Write first_conjunction(periods, offsets, limit). It returns the smallest integer n with 1 <= n <= limit on which
# every comet is visible. If no such night exists in that range, it returns -1.
# 
# There is always at least one comet, and the two lists always have the same length.

def first_conjunction(periods, offsets, limit):
    for n in range(1, limit + 1):
        if all(n % periods[i] == offsets[i] for i in range(len(periods))):
            return n
    return -1