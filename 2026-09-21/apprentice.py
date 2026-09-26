# The Tollhouse Permit Desk
# 
# The tollhouse at the east road keeps a desk where carters hand over their permits, and the clerk has gone to market.
# The rules carved into the desk are these, and they are checked strictly in this order — a permit is judged by the first rule it breaks, and no further.
# 
# A permit is a string. Using zero-based positions:
# 
# 1. It must be exactly 9 characters long. Otherwise the verdict is "length".
# 2. Positions 0, 1 and 2 must each be an uppercase letter A–Z. Otherwise the verdict is "prefix".
# 3. Position 3 must be the hyphen character -. Otherwise the verdict is "dash".
# 4. Positions 4, 5, 6, 7 and 8 must each be a digit 0–9. Otherwise the verdict is "digits".
# 5. The sum of those five digits must be even. Otherwise the verdict is "checksum".
# 
# A permit that breaks no rule has the verdict "valid".
# 
# Write inspectPermits(permits), which takes a list of strings and returns a list of strings:
#     - the verdict for each permit, in the same order as the input.
#     - An empty input list returns an empty list.

def inspect_permits(permits):
    ret_set = []
    for permit in permits:

        if len(permit) != 9:
            ret_set.append("length")
            continue
        if not permit[0].isupper() or not permit[1].isupper() or not permit[2].isupper():
            ret_set.append("prefix")
            continue
        if permit[3] != "-":
            ret_set.append("dash")
            continue
        if not permit[4].isdigit() or not permit[5].isdigit() or not permit[6].isdigit() or not permit[7].isdigit() or not permit[8].isdigit():
            ret_set.append("digits")
            continue
        if (int(permit[4]) + int(permit[5]) + int(permit[6]) + int(permit[7]) + int(permit[8])) % 2 != 0:
            ret_set.append("checksum")
            continue
        ret_set.append("valid")

    return ret_set