import numpy as np
import time
import math


class Algorithm:

    def __init__(self, methodName, arr, k):
        self.arr = arr
        self.methodName = methodName
        self.kthsmallest = -1
        self.k = k
        self.elapsedTime = 0

    # Function to do insertion sort (1)

    def setKthElement(self,value):
        self.kthsmallest = value


    def insertionSort(self):
        # Traverse through 1 to len(arr)
        start_time = time.perf_counter()
        for i in range(1, len(self.arr)):

            key = self.arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

        elapsed_time = time.perf_counter() - start_time
        self.setKthElement(self.arr[self.k-1])
        self.elapsedTime = elapsed_time

        # Python program for implementation of MergeSort (2)

    def mergeSort(self,arr):
        start_time = time.perf_counter()
        if len(arr) > 1:
            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            self.mergeSort(L)

            # Sorting the second half
            self.mergeSort(R)

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
        self.elapsedTime = elapsed_time
        return arr


    def mergeFinal(self):
        self.arr = self.mergeSort(self.arr)
        self.setKthElement(self.arr[self.k - 1])

    def swap(self,list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]

    def quicksort(self,arr, left, right, pivot):
        # pivot = 0;
        start_time = time.perf_counter()
        if left < right:
            pivot = self.partition(arr, left, right, left)

            self.quicksort(arr, left, pivot - 1, left)
            self.quicksort(arr, pivot + 1, right, pivot + 1)
            self.setKthElement(self.arr[self.k - 1])

        elapsed_time = time.perf_counter() - start_time
        self.elapsedTime = elapsed_time

    def getMedian(self,arr, left, right):
        center = math.ceil((left + right) / 2);
        if arr[left] > arr[center]:
            self.swap(arr, left, center)

        if arr[left] > arr[right]:
            self.swap(arr, left, right)

        if arr[center] > arr[right]:
            self.swap(arr, center, right)

        self.swap(arr, center, left)

        return right

    def partition(self, arr, left, right, index):
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

        tmp = arr[storedIndex]
        arr[storedIndex] = arr[right]
        arr[right] = tmp

        return storedIndex

        # partial selection sort (4)

    def partialSelectionSort(self):
        start_time = time.perf_counter()
        for i in range(0, self.k):
            # minIndex = i
            minValue = self.arr[i]
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < minValue:
                    minIndex = j
                    minValue = self.arr[j]
                    temp = self.arr[i]
                    self.arr[i] = self.arr[minIndex]
                    self.arr[minIndex] = temp
        # print(arr)
        elapsed_time = time.perf_counter() - start_time
        self.setKthElement(self.arr[self.k - 1])
        self.elapsedTime = elapsed_time

        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index

        # finds the kth position (of the sorted array)
        # in a given unsorted array i.e this function
        # can be used to find both kth largest and
        # kth smallest element in the array.
        # ASSUMPTION: all elements in arr[] are distinct  (7)

    def quickSelect(self,arr, l, r, k, type):
        # if k is smaller than number of
        # elements in array
        start_time = time.perf_counter()
        if k > 0 and k <= r - l + 1:

            # Partition the array around last
            # element and get position of pivot
            # element in sorted array
            if type == "median":
                index = self.partition(arr, l, r, self.getMedian(arr, l, r))
            else:
                index = self.partition(arr, l, r, l)

            # if position is same as k
            if index - l == k - 1:
                self.setKthElement(arr[index])
                elapsed_time = time.perf_counter() - start_time
                self.elapsedTime = elapsed_time
                return arr[index]

            # If position is more, recur
            # for left subarray
            if index - l > k - 1:
                return self.quickSelect(arr, l, index - 1, k, type)

            # Else recur for right subarray
            return self.quickSelect(arr, index + 1, r, k - index + l - 1, type)
        print("Index out of bound")


