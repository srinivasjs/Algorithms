# Python program for implementation of Quicksort Sort

import time #used for timing the program run

def partition(arr,low,high):
	i = ( low-1 )		 
	pivot = arr[high]	 

	for j in range(low , high):

		if arr[j] <= pivot:
		
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return ( i+1 )


def quickSort(arr,low,high):
	if low < high:

		pi = partition(arr,low,high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [10, 6, 4, 2, 1]
t1=time.time()
quickSort(arr, 0, len(arr)-1)
t2=time.time()
print arr
print "quickSort has taken {} seconds to run".format(t2-t1) # t2-t1 gives the actual time taken by program to run

# Time Complexity of the Algorithm
# O(nlogn)
# Worst case scenario would be if the pivot selected is the last element and if the array is already in increasing (or) decreasing #Sorting order
