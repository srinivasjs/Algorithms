# Python program for implementation of Bubble Sort
import time

arr = [2, 7, 4, 1, 5, 3]
length = len(arr)

def bubbleSort():
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
start = time.time()
bubbleSort()
end = time.time()
print "bubbleSort took {} seconds to run".format(end-start)

# output
# bubbleSort took 1.31130218506e-05 seconds to run

# Analysis of this Algorithm :
# The Time complexity is O(n*n)

# But, this Algorithm can be tweaked to give a best case to see if it is already sorted then let's not run it.

# Implementation with Flag to avoid run when already sorted :

def bubbleSort():
    for i in range(length-1):
        flag = 0
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag==0:
            break
        
# The effect of above algorithm with flag could be seen if array given is already sorted

# Analysis of this Algorithm :
# The Time complexity is O(n)   # >> Best Case 

# bubbleSort is an in-place and stable Algorithm
