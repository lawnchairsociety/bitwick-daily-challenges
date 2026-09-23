# The Ferryman's Tally Board
# 
# The ferryman at the Bitwick crossing keeps a tally board on the jetty post. The punt holds a fixed number of seats,
# and a crowd of travellers waits on the bank. The ferryman poles across with a full load each trip until everyone is over;
# the last trip may go part-empty.
# 
# Write ferryCrossings(travellers, seats).
# 
#    - travellers is a non-negative integer: how many people are waiting.
#    - seats is a positive integer: how many people fit in the punt on one crossing.
# 
# Return a list of exactly two integers:
# 
# 1. the number of crossings needed to carry every traveller over, and
# 2. the number of unused seats on the final crossing.
# 
# Every crossing but the last carries exactly seats travellers. If travellers is 0, return [0, 0].

def ferry_crossings(travellers, seats):
    crossings = travellers // seats if travellers % seats == 0 else (travellers // seats) + 1
    unused = 0 if travellers % seats == 0 else seats - (travellers % seats)

    return [crossings, unused]


print(ferry_crossings(7, 3))    # output: [3, 2]
print(ferry_crossings(6, 3))    # output: [2, 0]
print(ferry_crossings(0, 4))    # output: [0, 0]