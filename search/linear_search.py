# Linearly search x in arr[], which is an 
# List implementation in Python
# If x is present then return its location
# else return None
import time

arr = [1, 4, 7, 9, 23, 46, 78]

def linearSearch(arr, element):
    # range in Python helps in generating 
    # numbers . Returns a Python List with
    # numbers in them 
    # range(start, stop, step)
    # range(3)  >>  [0, 1, 2]
    # range(0, 6) >> [0, 1, 2, 3, 4, 5]
    # range(2, 8) >> [2, 3, 4, 5, 6, 7]
    # range(2, 8, 2) >> [2, 4, 6]
	for i in range(len(arr)):

		if arr[i] == element:
			return i+1

	return None

start = time.time()
retval = linearSearch(arr, 78)
end = time.time()
print "linearSearch took {} seconds to run".format(end-start)

# Analysis of this Algorithm:
# Since, looping is involved here, O(n)
# is the Time Complexity of this algorithm
# Takes "n" iterations for finding the element
# if present at last index (or) no element in
# array/List
# Best run time would be if the element to be searched
# is in First index itself
# Worst case being the element to be serched not present
# in array

# Note :
# range has been upgraded to xrange()
# since, The problem with the original
# range() function was that it used a 
# very large amount of memory when producing 
# a lot of numbers. However it tends to be 
# quicker with a small amount of numbers.
