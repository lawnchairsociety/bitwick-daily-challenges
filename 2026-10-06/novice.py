# The Spent Runes of the Dunmarrow Colossus
# 
# Beneath the moor of Dunmarrow lies a stone Colossus, asleep for three hundred years.
# A single row of rune-stones is set down its spine, and each stone holds a charge.
# The Order of Tollan Wakewright pays a bounty to any adventurer who can tell its menders which
# stones have gone dark, so that the menders know which ones to recarve before the Colossus is roused.
# 
# A stone is spent if its charge is zero or less. A stone with a negative charge has cracked and is draining,
# and it counts as spent too.
# 
# Write spent_runes(charges).
# 
#   - charges is a list of integers. charges[0] is the stone at the top of the spine
#     and the rest follow in order down the spine. The list may be empty.
#   - Return a list of integers giving the 0-based positions of every spent stone, in increasing order.
#   - If no stone is spent, including when charges is empty, return an empty list.
#   - Do not modify charges.

def spent_runes(charges):
    spent_stones = []
    for i in range(len(charges)):
        if charges[i] <= 0:
            spent_stones.append(i)
    return spent_stones