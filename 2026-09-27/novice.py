# The Cellar Ledger of the Rusty Tankard
# 
# The cellarer of the Rusty Tankard keeps a ledger of what sits in the cellar: each barrel name written beside the number of measures left in it.
# Barrels that have been drained are not always struck out — some still sit in the ledger with a nought beside them — and casks the inn has never
# carried are simply absent.
# 
# Each morning the cook hands over a list of names to check before the market opens.
# 
# Write out_of_stock(stock, wanted), where:
# 
#   - stock is a dictionary (object) whose keys are barrel names (strings) and whose values are the measures remaining (non-negative integers).
#   - wanted is a list (array) of barrel names (strings). It contains no repeated names, and may be empty.
# 
# Return a new list of the names from wanted that the inn cannot serve:
#     - a name counts as unservable if it does not appear as a key in stock, or if it appears with a value of 0.
#     - The returned names must be in the same order as they appear in wanted.
#     - If every wanted name is servable, return an empty list.

def out_of_stock(stock, wanted):
    oos = []
    for item in wanted:
        if stock.get(item) == None or stock.get(item) == 0:
            oos.append(item)
    return oos