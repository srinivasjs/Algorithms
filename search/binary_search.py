
# Iterative Binary Search Function
# It returns location of element in given array arr if present,
# else returns None
import time

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

start = time.time()
print binarySearch(arr, 0, len(arr)-1, 10)
end = time.time()

# Using time function to analyze the
# time taken to execute a function
# This enables us to measure time taken
# to execute a function/code by implementing
# different Algorithm
# Which enables us to evaluate Big Order O(n)

print "binarySearch took {} seconds to run".format(end-start)

# Analysis of this Algorithm:
# Since, Divide and Conquer Method is used, O(logn)
# is the Time Complexity of this algorithm

###########################################################

# Python Program for recursive binary search.

# Returns index of element in arr if present, else None
import time

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

print "binarySearch Recursive Algorithm too {} seconds to run".format(end-start)

