# Linearly search x in arr[], which is an 
# List implementation in Python
# If x is present then return its location
# else return None
import timeit

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

print linearSearch(arr, 78)

# Using timeit function to analyze the
# time taken to execute a function
# This enables us to measure time taken
# to execute a function/code by implementing
# different Algorithm
# Which enables us to evaluate Big Order O(n)

t1 = timeit.timeit('linearSearch(arr, 78)',setup='from __main__ import linearSearch, arr')
print "linearSearch Function took {} seconds to run".format(t1)
# Analysis of this Algorithm:

# Since, looping is involved here, O(n)
# is the Time Complexity of this algorithm
# Takes "n" iterations for finding the element
# if present at last index (or) no element in
# array/List

# Note :
# range has been upgraded to xrange()
# since, The problem with the original
# range() function was that it used a 
# very large amount of memory when producing 
# a lot of numbers. However it tends to be 
# quicker with a small amount of numbers.
