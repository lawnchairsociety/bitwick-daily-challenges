# The Muster Rolls of Fellbarrow Pass
# 
# The war-marshal of Fellbarrow Pass is raising sellsword companies against the raiders on the high road.
# Each company that answers the horn is entered on the muster roll as one line: the company's name, how many
# blades it brings, and the holdfast it is sent to guard. The scribe has fallen to a crossbow bolt, and the
# marshal will pay a fair purse to whoever can write the lines in the proper form.
# 
# Write muster_call(company, blades, place), where:
# 
#   - company is a non-empty string, the company's name.
#   - blades is a non-negative integer, the number of fighters the company brings.
#   - place is a non-empty string, the holdfast the company is sent to.
# 
# Return a single string of exactly this form:
# 
# `<company>: <blades> blades bound for <place>.`
# 
# The rules are:
# 
#   - Write company and place exactly as given, with no change to their letters or spacing.
#   - Write blades as an ordinary whole number.
#   - Use the word blade when blades is exactly 1. For every other number, including 0, use blades.
#   - There is a colon directly after the company name, single spaces between words, and a full stop at the end.

def muster_call(company, blades, place):
    plural_blades = "blades" if blades != 1 else "blade"
    call = f"{company}: {blades} {plural_blades} bound for {place}."
    return call