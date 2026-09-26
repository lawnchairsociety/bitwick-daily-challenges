# The Cellar Ledger of the Sleeping Badger
# 
# The cellarer of the Sleeping Badger keeps one ledger of what rests in the cellar,
# and each morning a runner brings down a list of what the taproom wants.
# 
# The ledger is given as stock: a mapping from cask name (a string) to the number of casks
# held (a non-negative integer). The morning list is given as order: a list of cask names (strings),
# which may repeat and may name casks the ledger has never heard of.
# 
# Write tallyOrder(stock, order), which returns a list of integers of the same length as order.
# The entry at each position is the number the ledger records for the cask named at that position in order,
# or 0 if that name does not appear in the ledger at all. The order of the returned list matches the order of order.

def tally_order(stock: dict[str, int], order: list[str]) -> list[int]:
    tally = []
    for item in order:
        tally.append(0 if stock.get(item) == None else stock.get(item))
    return tally