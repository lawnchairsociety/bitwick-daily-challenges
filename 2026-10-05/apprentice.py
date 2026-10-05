# The Restless Chrysalis of Briarcombe
# 
# The Moth-Wardens of Briarcombe have caged a cursed chrysalis inside a chalk warding circle,
# and they pay well for anyone who can tell them what the coming nights will bring.
# 
# The chrysalis glows, and its glow is always a positive whole number. Each night the glow changes exactly once:
# 
#   - if the glow is even, it becomes half of itself;
#   - if the glow is odd, it becomes three times itself plus one.
# 
# The creature inside wakes on the night the glow first equals exactly 1. The warding circle holds any glow up to
# and including ceiling. A glow strictly greater than ceiling breaks the circle.
# 
# Write chrysalis_nights(start, ceiling).
# 
#   - start is tonight's glow, an integer.
#   - ceiling is the circle's limit, an integer.
#   - You may assume 1 <= start <= ceiling.
# 
# Return an integer: the number of nightly changes until the glow first equals 1. If any glow reached along the way
# is greater than ceiling before the glow reaches 1, return -1 instead. If start is already 1, return 0.

def chrysalis_nights(start, ceiling):
    nightly_changes = 0
    if start == 1:
        return 0
    
    glow = start
    while glow != 1:
        nightly_changes += 1
        if glow % 2 == 0:
            glow = glow // 2
        else:
            glow = (glow * 3) + 1

        if glow > ceiling:
            return -1
    
    return nightly_changes