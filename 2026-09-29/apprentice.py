# The Tollgates of Marrowmere
# 
# The road out of Marrowmere runs through a line of gatehouses. Some gates take a toll from a passing cart; others hand out a bounty from the town chest.
# 
# You are given three arguments:
# 
#   - purse — an integer, the coins the carter sets out with (0 <= purse <= cap).
#   - cap — an integer, the most coins the purse can hold.
#   - tolls — a list of integers, one per gatehouse, in the order they are met. A positive value is a toll charged;
#     a value of zero or less is a bounty of that many coins paid to the carter (a value of 0 pays nothing).
# 
# The cart meets the gatehouses in order:
# 
#   - At a gate with a positive value v: if the purse holds at least v coins, v coins are paid out of the purse and the gate is passed.
#     Otherwise the cart is turned back at once — that gate is not passed, and no later gate is reached.
#   - At a gate with a value of zero or less: the bounty is added to the purse, and the gate is passed.
#     If this would take the purse above cap, the purse is left holding exactly cap coins and the surplus is lost.
# 
# Write toll_run(purse, cap, tolls), which returns a list of exactly two integers:
#   - the number of gates passed, and
#   - the coins left in the purse when the journey ends.

def toll_run(purse, cap, tolls):
    gates = 0
    coins = purse
    for toll in tolls:
      if coins >= toll:
        gates += 1
      else:
        break

      coins -= toll
      
      if coins > cap:
        coins = cap

      if coins < 0:
        coins = 0
        continue

    return [gates, coins]