# The Salamander Circle of Pyrewick
# 
# The Conjurers' Lodge of Pyrewick pays well for any adventurer who can say, before the chalk is drawn,
# whether a fire-salamander can be called into the iron circle on the cliffs tonight. A failed summoning
# wastes a season's worth of brimstone, so the Lodge wants a certain answer.
# 
# A salamander can be summoned when all three of these conditions hold:
# 
# 1. The brazier's heat is at least 300 degrees.
# 2. The night is moonless, or the summoner wears a salt-iron ring, or both.
# 3. It is not raining.
# 
# Write can_summon(heat, moonless, ring, rain) where:
# 
#   - heat is an integer, the brazier's heat in degrees (it may be zero).
#   - moonless is a boolean, true if the night is moonless.
#   - ring is a boolean, true if the summoner wears a salt-iron ring.
#   - rain is a boolean, true if it is raining.
# 
# Return a boolean: true if all three conditions hold, otherwise false.

def can_summon(heat, moonless, ring, rain):
    if heat >= 300 and (moonless or ring) and not rain:
        return True
    return False