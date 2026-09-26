# The Tollhouse at Mirebridge
# 
# The tollkeeper at Mirebridge has gone to market and left the gate to you. A queue of wagons waits on the near bank,
# and the toll board on the wall lists the rates.
# 
# You are given wagons, a list of wagons. Each wagon is a list of three values: the number of wheels (an integer, zero or more),
# the weight in stone (an integer, zero or more), and the cargo (a string).
# 
# The toll for one wagon is worked out in this order:
# 
# 1. Base rate, by wheels. Exactly 2 wheels costs 3 coins. Exactly 4 wheels costs 5 coins. Any other number of wheels costs 8 coins.
# 2. Weight surcharge. If the weight is more than 500, add 4 coins. Otherwise, if the weight is more than 200, add 2 coins. Otherwise add nothing.
# 3. Cargo adjustment. If the cargo is exactly "grain", the toll so far is halved and rounded down to a whole number of coins.
#     If the cargo is exactly "ore", the toll so far is doubled. Any other cargo leaves the toll unchanged.
# 4. Minimum toll. If the result is less than 2 coins, the wagon pays 2 coins instead.
# 
# Write mirebridge_toll(wagons), which returns an integer: the sum of the tolls of every wagon in the list. An empty list returns 0.


def mirebridge_toll(wagons):
    sum = 0
    for wagon in wagons:
        wagon_sum = 0
        wheel_num = wagon[0]
        wagon_weight = wagon[1]
        cargo = wagon[2]

        # wheel count
        if wheel_num == 2:
            wagon_sum += 3
        elif wheel_num == 4:
            wagon_sum += 5
        else:
            wagon_sum += 8
        
        # weight
        if wagon_weight > 500:
            wagon_sum += 4
        elif wagon_weight > 200 and wagon_weight <= 500:
            wagon_sum += 2
        
        # cargo
        if cargo == "grain":
            wagon_sum = wagon_sum // 2
        elif cargo == "ore":
            wagon_sum = wagon_sum * 2

        # minimum
        if wagon_sum < 2:
            wagon_sum = 2

        # add to total
        sum += wagon_sum
        
    return sum