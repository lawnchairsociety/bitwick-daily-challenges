# The Rain Barrel at the Watch-House
# 
# The watch-house on the north wall keeps one rain barrel, and the night warden keeps a strip
# of birch bark with the barrel's fortunes written on it in order.
# 
# Each mark on the bark is an integer:
# 
#   - a positive number is rain, adding that many pails to the barrel;
#   - a negative number is the guards drawing water, taking that many pails out;
#   - a zero is a quiet watch and changes nothing.
# 
# The barrel starts empty and holds at most cap pails. Rain that would carry the level above cap
# fills the barrel to the brim and the rest spills away. A draw that asks for more than the barrel
# holds empties it completely, and the pails that could not be given are unmet.
# 
# Write rain_barrel(entries, cap), where entries is a list of integers (possibly empty) read left to right
# and cap is an integer of at least 0. Return a list of exactly three integers: the barrel's final level,
# the total pails spilled over all entries, and the total pails left unmet over all entries.

def rain_barrel(entries, cap):
    barrel = 0
    spilled = 0
    unmet = 0

    for entry in entries:
        if barrel + entry > cap:
            spilled += abs(cap - (barrel + entry))
            barrel = cap
            continue
        if entry < 0:
            barrel += entry
            if barrel < 0:
                unmet += (0 - barrel)
                barrel = 0
            continue
        barrel += entry

    return [barrel, spilled, unmet]