# The Warden Door of the Sunken Vault
# 
# Beneath the drowned hills east of Bitwick lies the Sunken Vault, sealed by a warden door that judges every
# adventurer who lays a hand on it. The Delvers' Guild will pay well for a charm that predicts the door's verdict
# before anyone risks the descent.
# 
# The door follows exactly these rules:
# 
#   - A cursed adventurer is always refused, whatever else is true of them.
#   - An adventurer who is not cursed is admitted if they carry the vault key, or if their level is 10 or higher.
#   - Anyone else is refused.
# 
# Write warden_door(level, key, cursed), where:
# 
#   - level is a non-negative integer, the adventurer's level.
#   - key is a boolean, true if the adventurer carries the vault key.
#   - cursed is a boolean, true if the adventurer bears a curse.
# 
# Return a boolean: true if the door admits the adventurer, false if it refuses them.

def warden_door(level, key, cursed):
    if cursed: return False
    elif key or level >= 10: return True

    return False