# Implementation of insertion sort in python

import time

def insertionSort(arr):
    for i in range(0, len(arr)):
        value = arr[i]
        j = i-1
        while (j>=0 and value<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = value

arr = [7, 2, 4, 1, 5, 3]
start = time.time()
insertionSort(arr)
end = time.time()
print "insertionSort executed in {} seconds".format(end-start)

# output
# insertionSort executed in 7.86781311035e-06 seconds
# [1, 2, 3, 4, 5, 7]


# Analysis of this Algorithm :
# The Time complexity is O(n*n)

# Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time O(n) when #elements are already sorted.
