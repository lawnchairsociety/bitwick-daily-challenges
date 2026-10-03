# The Reagent Roll of the Cinderpike Expedition
# 
# The Guild of Ashen Alchemists is outfitting an expedition to the fire-vents of Cinderpike. Before the mules are loaded,
# the Guild's quartermaster must know how many measures of the required reagents the Guild's store actually holds.
# 
# The store's inventory is a dictionary, stock, mapping each reagent's name (a string) to the number of measures on hand (a non-negative integer).
# The expedition's requirements are a list of reagent names, wanted.
# 
# Write tally_reagents(stock, wanted), which returns an integer: the sum, over every name in wanted, of that name's count in stock.
# 
# Rules:
#     - A name in wanted that is not a key in stock contributes 0.
#     - Names match exactly, including upper and lower case.
#     - If a name appears more than once in wanted, its count is added once for each appearance.
#     - If wanted is empty, return 0.
# 
# Neither argument should be modified.

def tally_reagents(stock, wanted):
    reagents = 0
    for item in wanted:
        if item not in stock:
            continue
        reagents += stock[item]
    return reagents