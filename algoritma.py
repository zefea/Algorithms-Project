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
import math


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


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def quicksort(arr, left, right, pivot):
    # pivot = 0;

    if left < right:
        pivot = partition(arr, left, right, left)

        quicksort(arr, left, pivot - 1, left)
        quicksort(arr, pivot + 1, right, pivot + 1)


def getMedian(arr, left, right):
    center = math.ceil((left + right) / 2);
    if arr[left] > arr[center]:
        swap(arr, left, center)

    if arr[left] > arr[right]:
        swap(arr, left, right)

    if arr[center] > arr[right]:
        swap(arr, center, right)

    swap(arr, center, left)

    return right


def partition(arr, left, right, index):
    pivotValue = arr[index]
    storedIndex = left

    tmp = arr[index]
    arr[index] = arr[right]
    arr[right] = tmp

    for i in range(left, right):
        if arr[i] <= pivotValue:
            tmp = arr[i]
            arr[i] = arr[storedIndex]
            arr[storedIndex] = tmp;

            storedIndex = storedIndex + 1

    tmp = arr[storedIndex];
    arr[storedIndex] = arr[right];
    arr[right] = tmp;

    return storedIndex


# partial selection sort (4)
def partialSelectionSort(arr, k):
    start_time = time.perf_counter()
    for i in range(0, k):
        minIndex = i
        minValue = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < minValue:
                minIndex = j
                minValue = arr[j]
                temp = arr[i]
                arr[i] = arr[minIndex]
                arr[minIndex] = temp
    # print(arr)
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
def quickSelect(arr, l, r, k, type):
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        if type == "median":
            index = partition(arr, l, r, getMedian(arr, l, r))
        else:
            index = partition(arr, l, r,l)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return quickSelect(arr, l, index - 1, k,type)

        # Else recur for right subarray
        return quickSelect(arr, index + 1, r, k - index + l - 1,type)
    print("Index out of bound")


def printKthElement(arr, k):
    print(arr[k - 1])


def saveArray(input_array):
    arr_list = []
    arr_array = input_array.copy()

    i = 0
    # for seven algorithms saved array for each of them
    for i in range(7):
        arr_list.append(arr_array)

    return arr_list


def plot_nvstime(timeList, nlist):
    pass


# do not consider best or worst cases, just a random input for now
def generateInputRandom(n):
    randnums = np.random.randint(1, 1001, n)
    # print(randnums)

    return list(randnums)


def inputsInt():
    inputs = []
    i = 0
    n = 10
    for i in range(3):
        input_array = generateInputRandom(n)
        inputs.append(input_array)
        # n = n * 10

    return inputs


def main():
    k = 3
    # input_array = [12, 11, 13, 6, 4, 2, 19]
    inputs = inputsInt()

    for input in inputs:
        # save the array
        n = len(input)
        print("************************************")
        # print("n = ", n)
        # print(input)
        sortArrayList = saveArray(input)
        timeList = []

        time0 = quicksort(sortArrayList[0], 0, n - 1, 0)
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
        kthsmallest = quickSelect(sortArrayList[4], 0, n - 1, k,"median")
        time4 = time.perf_counter() - start_time
        timeList.append(time4)
        print(kthsmallest)

        start_time = time.perf_counter()
        kthsmallest = quickSelect(sortArrayList[5], 0, n - 1, k, "none")
        time5 = time.perf_counter() - start_time
        timeList.append(time5)
        print(kthsmallest)
        # printKthElement(sortArrayList[4], k)
        """  print(f"Elapsed time quickSort: {timeList[0]:0.9f} seconds")
        print(f"Elapsed time insertionSort: {timeList[1]:0.9f} seconds")
        print(f"Elapsed time mergeSort: {timeList[2]:0.9f} seconds")
        print(f"Elapsed time partialSelectionSort: {timeList[3]:0.9f} seconds")
        print(f"Elapsed time quickSelect: {timeList[4]:0.9f} seconds")"""


if __name__ == "__main__":
    main()