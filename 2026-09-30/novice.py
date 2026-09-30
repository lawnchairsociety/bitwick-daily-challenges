# The Flood Stone of Mill Ford
# 
# The miller at Mill Ford keeps a flood stone by the wheel: a line carved in the rock, and
# beside it a tally of the river's height. Each morning a notch count is written down —
# a positive number for notches above the line, a negative number for notches below it,
# and zero when the water sits exactly on the line.
# 
# The miller wants a second column beside the first: for each morning, the highest reading
# recorded so far, counting that morning and every morning before it.
# 
# Write high_water_marks(marks).
# 
#   - marks is a list of integers, in the order the readings were taken. It may be empty.
#   - Return a new list of the same length, where the value at each position is the largest value
#     found at that position or any earlier position in marks.
#   - For an empty list of readings, return an empty list.

def high_water_marks(marks):
  extremes = []
  for mark in marks:
    if len(extremes) == 0:
      extremes.append(mark)
      continue

    if mark > extremes[len(extremes) - 1]:
      extremes.append(mark)
    else:
      extremes.append(extremes[len(extremes) - 1])
  
  return extremes