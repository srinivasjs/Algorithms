# Implementation of Selection Sort
import timeit

A = [4, 3, 2, 5, 1]

def selectionSort():
    for i in range(len(A)):
	
	    min_elem_idx = i
	    for j in range(i+1, len(A)):
		    if A[min_elem_idx] > A[j]:
			    min_elem_idx = j
			
	    A[i], A[min_elem_idx] = A[min_elem_idx], A[i]
	    
print "Array/List before sort : {}".format(A)
print timeit.timeit("selectionSort()", setup="from __main__ import selectionSort, A")
print "Array/List after sort : {}".format(A)

# output
# Array/List before sort : [4, 3, 2, 5, 1]
# 2.70688509941
# Array/List after sort : [1, 2, 3, 4, 5]

# Analysis of this Algorithm:
# Time Complexity  :  O(n*n) >> Since, 2 loops are used 
