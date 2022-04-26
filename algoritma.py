#
# CSE 2046 Analysis of Algorithms - Project 1
#
# Zeynep Ferah Akkurt - 150119824
# Merve Rana Kızıl - 150119825
#
# 1) Insertion-sort and return the 𝑘’th element in the list,
# 2) Merge-sort and return the 𝑘’th element in the list,
# 3) Quick-sort and return the 𝑘’th element in the list. While partitioning choose the pivot element as the first element in an array.
# 4) partial selection-sort, i.e. find the minimum element 𝑘 times to find the 𝑘’th smallest element.
# 5) partial heap-sort, i.e. store all elements in a max-heap and apply 𝑛−𝑘 times max removal. Return the max element in the root.
# 6) Not sort the list, but apply quick select algorithm, which is based on array partitioning, as described in the class. While partitioning, choose the pivot element as the first element in an array,
# 7) Apply quick select algorithm, but this time use median-of-three pivot selection1,
#


import numpy as np
import time


# Function to do insertion sort (1)
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    start_time = time.perf_counter()
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


# Python program for implementation of MergeSort (2)
def mergeSort(arr):
    start_time = time.perf_counter()
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


# Function to do Quick sort (3)
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[low]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    start_time = time.perf_counter()
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


# partial selection sort (4)
def partialSelectionSort(arr, k):
    start_time = time.perf_counter()
    for i in range(0, k):  # k + 1 or k ???
        minIndex = i
        minValue = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < minValue:
                minIndex = j
                minValue = arr[j]
                temp = arr[i]
                arr[i] = arr[minIndex]
                arr[minIndex] = temp
    #print(arr)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index


# finds the kth position (of the sorted array)
# in a given unsorted array i.e this function
# can be used to find both kth largest and
# kth smallest element in the array.
# ASSUMPTION: all elements in arr[] are distinct  (7)
def quickSelect(arr, l, r, k):
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return quickSelect(arr, l, index - 1, k)

        # Else recur for right subarray
        return quickSelect(arr, index + 1, r,
                           k - index + l - 1)
    print("Index out of bound")


def printKthElement(arr, k):
    print(arr[k - 1])


def saveArray(input_array):
    arr_list = []
    arr_array = input_array.copy()

    i=0
    #for seven algorithms saved array for each of them
    for i in range(7):
        arr_list.append(arr_array)

    print(len(arr_list))
    return arr_list

def plot_nvstime(timeList,nlist):
    pass



# do not consider best or worst cases, just a random input for now
def generateInputRandom(n):
    randnums = np.random.randint(1, 1001, n)
    #print(randnums)

    return list(randnums)

def inputsInt():
    inputs = []
    i = 0
    n = 10
    for i in range(3):
        input_array = generateInputRandom(n)
        inputs.append(input_array)
        n = n * 10

    return inputs

def main():
    k = 3
    #input_array = [12, 11, 13, 6, 4, 2, 19]
    inputs = inputsInt()

    for input in inputs:
        # save the array
        n = len(input)
        print("************************************")
        print("n = ", n)
        #print(input)
        sortArrayList = saveArray(input)

        timeList = []

        time0 = quickSort(sortArrayList[0], 0, n - 1)
        timeList.append(time0)
        printKthElement(sortArrayList[0], k)

        time1 = insertionSort(sortArrayList[1])
        timeList.append(time1)
        printKthElement(sortArrayList[1], k)

        time2 = mergeSort(sortArrayList[2])
        timeList.append(time2)
        printKthElement(sortArrayList[2], k)

        time3 = partialSelectionSort(sortArrayList[3], k)
        timeList.append(time3)
        printKthElement(sortArrayList[3], k)

        start_time = time.perf_counter()
        quickSelect(sortArrayList[4], 0, n - 1, k)
        time4 = time.perf_counter() - start_time
        timeList.append(time4)
        printKthElement(sortArrayList[4], k)

        print(f"Elapsed time quickSort: {timeList[0]:0.9f} seconds")
        print(f"Elapsed time insertionSort: {timeList[1]:0.9f} seconds")
        print(f"Elapsed time mergeSort: {timeList[2]:0.9f} seconds")
        print(f"Elapsed time partialSelectionSort: {timeList[3]:0.9f} seconds")
        print(f"Elapsed time quickSelect: {timeList[4]:0.9f} seconds")


if __name__ == "__main__":
    main()
