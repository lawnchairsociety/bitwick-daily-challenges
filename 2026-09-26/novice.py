# The Roster of the Night Watch
# 
# A notice from the captain of the gate at bitwick.
# 
# The night watch roster is a list of watchmen's names, written in the order they stand their turns.
# When a watchman sends word that he cannot come, the captain crosses off the first entry bearing his name and leaves
# the rest of the roster exactly as it was — later entries with the same name still stand their turns.
# 
# Write cross_off(watch, absent).
# 
#   - watch is a list of strings, the roster in order. It may be empty.
#   - absent is a single string, the name to cross off. Names are matched exactly, letter for letter, including capitalisation.
# 
# Return a new list of strings: the roster in its original order with the first entry equal to absent removed.
# If no entry matches absent, return a list with the same names in the same order.

def cross_off(watch, absent):
    present = []
    marked = False
    for name in watch:
        if not marked and name == absent:
            marked = True
            continue
        present.append(name)
    return present