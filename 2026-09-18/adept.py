# The Lanterns of Dusk Lane
# 
# The lamplighter of bitwick keeps Dusk Lane, where the lanterns stand in a single row from the gate to the well. Each evening she records how
# brightly each one burns, and the Lamplighters' Guild pays only for steady work: a run of neighbouring lanterns counts as steady when the
# brightest and the dimmest lantern in that run differ by no more than the allowance the Guild set for the night.
# 
# You are given:
# 
#    - lamps — a list of integers, the brightness of each lantern in order along the lane. Values may be negative. The list may be empty.
#    - spread — a non-negative integer, the Guild's allowance for the night.
# 
# Return an integer: the number of lanterns in the longest contiguous run of lamps in which
# (maximum brightness − minimum brightness) is at most spread.
# A run of a single lantern always qualifies, since its maximum and minimum are the same. If lamps is empty, return 0.
# 
# Write longestSteadyStretch(lamps, spread).

def longest_steady_stretch(lamps, spread):
    longest_run = 0
    left = 0
    for right in range(len(lamps)):
        while max(lamps[left:right + 1]) - min(lamps[left:right + 1]) > spread:
            left += 1
        longest_run = max(longest_run, right - left + 1)
    
        
    return longest_run