# Searching an element in a list/array in python

# Simplest way of searching an element in array

arr = [2, 4, 6, 8, 10, 100, 34]

def elementSearch(element, arr):
    """
    Given an Element, return it's Location if present
    else return None
    """
    if element in arr:
        return arr.index(element)+1
    return None

# Prints Location of the element (8 in this case) if
# present in arr
#else prints None
print elementSearch(8, arr)

# Analysis of this Algorithm:
# O(1) >> No Iterations and always only one operation
# i.e. "if element in arr:"

# Enhancements that can be done
# element passed as an args to function elementSearch
# can be checked for type . If type other than "int"
# an error can be thrown
