# The Slayers' Tally of the Hunters' Guild
# 
# Each dawn the Hunters' Guild of Bitwick pins a fresh tally beside the inn door, one line for every'
# 'hunter who came back from the wild with proof of a kill. The Guild's scribe has fallen to a ghoul's bite,'
# 'and the Guild will pay a silver crown to whoever can write the lines in the scribe's exact form.
# 
# Write tally_line(badge, hunter, beast, count), which returns one line of the tally as a string.
# 
# Arguments
#   - badge - a non-negative integer, the hunter's Guild badge number.
#   - hunter - a non-empty string, the hunter's name.
#   - beast - a non-empty string, the singular name of the beast slain.
#   - count - a non-negative integer, how many of that beast the hunter slew.
# 
# Return a string made of these parts, in this order:
#   1. The character #, followed by the badge number written with leading zeros so that it has at least three digits.
#      A badge that already has three or more digits is written unchanged.
#   2. A single space, then hunter exactly as given.
#   3. The text slew (a space, the word slew, a space).
#   4. count written as a plain integer, then a single space.
#   5. beast exactly as given, followed by the letter s if count is anything other than exactly 1.
#      When count is 1, no s is added.
# 
# There is no trailing space or punctuation.

def tally_line(badge, hunter, beast, count):
    
    return "#" + str(badge).zfill(3) + " " + hunter + " slew " + str(count) + " " + beast + ("s" if count != 1 else "")