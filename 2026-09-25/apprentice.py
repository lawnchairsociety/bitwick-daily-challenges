# The Ferryman's Rafts
# 
# The ferryman at bitwick's lower crossing lashes crates onto rafts one at a time,
# in the exact order they sit on the bank. He never reorders them.
# 
# He loads the raft in front of him until the next crate would break one of his two rules,
# then poles that raft across and starts a fresh one:
# 
# - the total weight on a raft may not exceed limit
# - a raft may not carry more than size crates
# 
# A crate that is heavier than limit all by itself is still ferried: placed on an empty raft,
# it rides alone (and that raft is full as soon as another rule would be broken by the next crate).
# 
# Write load_rafts(weights, limit, size).
# 
# - weights is a list of positive integers, the crate weights in bank order.
# - limit is a positive integer, the greatest total weight a raft may carry.
# - size is an integer of at least 1, the greatest number of crates a raft may carry.
# 
# Return a list of lists of integers: the crates on each raft, in loading order, with the rafts in the order they crossed.
# An empty weights returns an empty list.

def load_rafts(weights, limit, size):
    ret_set = []

    raft = []
    for weight in weights:
        if len(raft) > 0 and sum(raft) + weight > limit:
            ret_set.append(raft)
            raft = []
        
        if weight >= limit:
            raft.append(weight)
            ret_set.append(raft)
            raft = []
            continue

        raft.append(weight)

        if len(raft) == size:
          ret_set.append(raft)
          raft = []

    if len(raft) > 0:
        ret_set.append(raft)
    return ret_set



print(load_rafts([4, 4, 4], 8, 5))             # output: [[4, 4], [4]]
print(load_rafts([10, 1, 2], 5, 3))            # output: [[10], [1, 2]]
print(load_rafts([1, 1, 1, 1, 1], 10, 2))      # output: [[1, 1], [1, 1], [1]]