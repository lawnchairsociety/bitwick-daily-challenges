# The Griffon Flight to Skarrow Isle
# 
# The Aerie Mistress of Kestrel Scar has posted a commission: a company of adventurers must be flown across the Gloaming Sound
# to Skarrow Isle before the autumn gales close the sky. Every griffon in the aerie wears the same saddle, and each saddle holds
# a fixed number of riders. All the riders fly in a single crossing, so every rider needs a seat on some griffon.
# 
# Write griffons_needed(riders, seats), which returns the smallest number of griffons needed to carry every rider.
# 
#   - riders is a whole number, 0 or greater: how many adventurers must cross.
#   - seats is a whole number, 1 or greater: the most riders a single griffon can carry.
# 
# Return a whole number. A griffon may fly with fewer riders than it has seats. If there are no riders, no griffons are needed.

def griffons_needed(riders, seats):
    if riders % seats == 0:
        return riders // seats
    else:
        return (riders // seats) + 1