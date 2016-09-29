
# Iterative Binary Search Function
# It returns location of element in given array arr if present,
# else returns None
import timeit

arr = [2, 4, 6, 8, 10, 200, 324, 345, 290]

def binarySearch(arr, l, r, element):

	while l <= r:

		mid = l + (r - l)/2;
		
		if arr[mid] == element:
			return mid

		elif arr[mid] < element:
			l = mid + 1

		else:
			r = mid - 1
	
	return None

print binarySearch(arr, 0, len(arr)-1, 10)

# Using timeit function to analyze the
# time taken to execute a function
# This enables us to measure time taken
# to execute a function/code by implementing
# different Algorithm
# Which enables us to evaluate Big Order O(n)

t1 = timeit.timeit('binarySearch(arr, 0, len(arr)-1, 10)',setup='from __main__ import binarySearch, arr')
print "binarySearch Function took {} seconds to run".format(t1)

# Analysis of this Algorithm:
# Since, Divide and Conquer Method is used, O(logn)
# is the Time Complexity of this algorithm

###########################################################

# Python Program for recursive binary search.

# Returns index of element in arr if present, else None
import timeit

def binarySearch (arr, l, r, element):

	if r >= l:

		mid = l + (r - l)/2

		if arr[mid] == element:
			return mid
		
		elif arr[mid] > element:
			return binarySearch(arr, l, mid-1, element)

		else:
			return binarySearch(arr, mid+1, r, element)

	else:
		return None

print binarySearch(arr, 0, len(arr)-1, 10)

# Using timeit function to analyze the
# time taken to execute a function
# This enables us to measure time taken
# to execute a function/code by implementing
# different Algorithm
# Which enables us to evaluate Big Order O(n)

t1 = timeit.timeit('binarySearch(arr, 0, len(arr)-1, 10)',setup='from __main__ import binarySearch, arr')
print "binarySearch Recursive Function took {} seconds to run".format(t1)

# Analysis of this Algorithm:
# Since, Divide and Conquer Method is used, O(logn)
# is the Time Complexity of this algorithm


# Time it took to search "10" element : 

# 4
# binarySearch Function took 0.245880126953 seconds to run
# 4
# binarySearch Recursive Function took 0.238392114639 seconds to run

# Time it took to search "100000"(not present in array) :

# None
# binarySearch Function took 0.738080978394 seconds to run
# None
# binarySearch Recursive Function took 1.08194184303 seconds to run

