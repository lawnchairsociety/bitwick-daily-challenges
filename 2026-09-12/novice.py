# The Tap-Room Slate
# 
# The innkeeper of the Wet Badger chalks one line on the slate for every order that leaves the kitchen, and last night's 
# cellar-hand chalked them all crooked. She wants a carver who can write the lines the same way every time.
# 
# Write slateLine(name, count, price).
# 
#     - name is a string: the item ordered.
#     - count is a non-negative integer: how many were ordered.
#     - price is a non-negative integer: the cost in coins of a single one.
# 
# Return a single string of the form:
# 
# NAME xCOUNT = TOTAL coins
# 
# where NAME is name exactly as given, COUNT is count, and TOTAL is count multiplied by price. The spaces and the x and 
# the = appear exactly as shown above.
# 
# The last word is coins, except when the total is exactly 1, in which case it is coin.

def slate_line(name, count, price):
    return f"{name} x{count} = {count * price} {"coin" if count * price == 1 else "coins"}"