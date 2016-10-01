# Python program for implementation of Bubble Sort
import timeit

arr = [2, 7, 4, 1, 5, 3]
length = len(arr)

def bubbleSort():
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
t1 = timeit.timeit("bubbleSort()", setup="from __main__ import arr, length, bubbleSort")
print "bubbleSort took {} seconds to sort".format(t1)
print "Sorted list : {}".format(arr)

# output
# bubbleSort took 2.60335898399 seconds to sort
# Sorted list : [1, 2, 3, 4, 5, 7]

# Analysis of this Algorithm :
# The Time complexity is O(n*n)

# But, this Algorithm can be tweaked to give a best case to see if it is already sorted then let's not run it.

# Implementation with Flag to avoid run when already sorted :

# Python program for implementation of Bubble Sort
import timeit

arr = [1, 2, 3, 4, 5, 7]  # Already sorted List
length = len(arr)

def bubbleSort():
    for i in range(length-1):
        flag = 0
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag==0:
            break
        
t1 = timeit.timeit("bubbleSort()", setup="from __main__ import arr, length, bubbleSort")
print "bubbleSort took {} seconds to sort".format(t1)
print "Sorted list : {}".format(arr)

# output
# bubbleSort took 0.958528995514 seconds to sort
# Sorted list : [1, 2, 3, 4, 5, 7]

# Analysis of this Algorithm :
# The Time complexity is O(n)   # >> Best Case 
