# The Beacon-Keeper's Oil Ledger
# 
# The beacon on Bitwick Head has burned every night for ninety years, and the keeper writes one number in her ledger for each 
# thing she does to the oil tank. The tank holds at most cap units and begins the night empty.
# 
# You are given two arguments:
# 
#     - cap: a non-negative integer, the capacity of the tank in units.
#     - log: a list of integers, the ledger entries in the order they were written.
# 
# Each entry is applied to the tank in order:
# 
#     - A positive entry n pours n units in. Whatever does not fit runs over the rim and is lost; the tank is left full.
#     - A negative entry n burns -n units. If the tank holds less than that, it burns everything it has and is left empty; the units it 
#       could not supply are the shortfall.
#     - An entry of 0 changes nothing.
# 
# Write tally_oil(cap, log), which returns a list of exactly two integers: the total number of units spilled over the rim across 
# the whole ledger, followed by the total shortfall across the whole ledger.

def tally_oil(cap, log):
    spillage = 0
    shortfall = 0
    current_tank_level = 0
    for entry in log:
        if entry == 0:
            pass
        elif entry > 0:
            # pour
            if current_tank_level + entry > cap:
                # spillage
                spillage += (current_tank_level + entry) - cap
                current_tank_level = cap
            else:
                current_tank_level += entry
        else:
            # burn
            if current_tank_level + entry > 0:
                # excess
                current_tank_level += entry
            elif current_tank_level + entry < 0:
                # shortfall
                shortfall += abs(current_tank_level + entry)
                current_tank_level = 0
            else:
                # exact
                current_tank_level = 0
    return [spillage, shortfall]