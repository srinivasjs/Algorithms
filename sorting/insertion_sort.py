# Implementation of insertion sort in python

import timeit

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

arr = [23, 4, 12, 6, 21, 5]
t1 = timeit.timeit('insertionSort(arr)', setup='from __main__ import insertionSort, arr')
print 'insertionSort took {} seconds to execute'.format(t1)
print 'sorted list {}'.format(arr)

# output
# insertionSort took 0.967344045639 seconds to execute
# sorted list [4, 5, 6, 12, 21, 23]

# Analysis of this Algorithm :
# The Time complexity is O(n*n)

# Time complexity of this algorithm is considered to be O(n*n)
# Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time O(n) when #elements are already sorted.
