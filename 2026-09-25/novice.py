# The Chalkboard of the Hearth and Hammer
# 
# The innkeeper of the Hearth and Hammer chalks one line on the board for every order that leaves the kitchen,
# and the lines must all be the same width so the board reads clean from the door.
# 
# Write tally_line(name, count, price).
# 
# -  name is a string: the name of the item.
# -  count is a non-negative integer: how many were ordered.
# -  price is a non-negative integer: the cost in coins of one of them.
# 
# Return a single string built like this:
# 
# 1. The tally is the count, a space, the letter x, a space, then the name: e.g. 3 x Barley Ale.
# 2. The total is count multiplied by price. The charge is that total, a space, then the word `coin` if the total is exactly 1, and `coins` otherwise.
# 3. The returned line is the tally, then a run of . dots, then the charge, with the dots chosen so the whole line is exactly 32 characters long.
# 4. If the tally and the charge together take up 31 characters or more, there is no room for a proper run: put exactly one dot between them,
#    and the line is longer than 32 characters.
# 
# The return value is that string. No leading or trailing spaces are added anywhere.

def tally_line(name, count, price):
    spacer = '.'
    charge = price * count
    head = "{} x {}".format(str(count), name)
    tail = "{} {}".format(str(charge), "coin" if charge == 1 else "coins")
    dot_count = 1 if len(head) + len(tail) >= 31 else 32 - (len(head) + len(tail))
    return head + spacer * dot_count + tail



print(tally_line("Barley Ale", 3, 4))                            # output: "3 x Barley Ale..........12 coins"
print(tally_line("Mead", 1, 1))                                  # output: "1 x Mead..................1 coin"
print(tally_line("Thrice-Distilled Dragonfire Brandy", 2, 50))   # output: "2 x Thrice-Distilled Dragonfire Brandy.100 coins"