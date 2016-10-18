# Implementation of Selection Sort
import time

A = [4, 3, 2, 5, 1]

def selectionSort():
    for i in range(len(A)-1):
	
	    min_elem_idx = i
	    for j in range(i+1, len(A)):
		    if A[min_elem_idx] > A[j]:
			    min_elem_idx = j
			
	    A[i], A[min_elem_idx] = A[min_elem_idx], A[i]
	    
start = time.time()
selectionSort()
end = time.time()

print "Time taken to run selectionSort is {} seconds".format(end-start)

# Analysis of this Algorithm:
# Time Complexity  :  O(n*n) >> Since, 2 loops are used 

# SelectionSort is an inplace Algorithm i.e. it does not
# use extra auxillary memory
