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

from Algorithm import *
import matplotlib.pyplot as plt
import random


# do not consider best or worst cases, just a random input for now
def generateInputRandom(n):
    randnums = np.random.randint(1, 1000, n)

    return list(randnums)


def inputsInt(list, type):
    inputs = []

    i = 0
    n = 50
    for i in range(5):
        input_array = generateInputRandom(n)
        inputs.append(input_array)
        list.append(n)
        n = n * 2
    return inputs


def sortthearrays(inputs):
    for inputx in inputs:
        inputx.sort()


def reversedsortthearrays(inputs):
    for inputx in inputs:
        inputx.sort(reverse=True)


# --------------------------------- insertion ---------------------------------
def insertionSortAnalysis(k):
    ns = []
    inputs = inputsInt(ns, "none")
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xinsert3 = []
    for input1 in inputs:
        insertionSort3 = Algorithm("insertionSort", input1, k)
        insertionSort3.insertionSort()
        # print(insertionSort3.methodName, ":", insertionSort3.kthsmallest, ",", f"{insertionSort3.elapsedTime:0.9f}")
        # xinsert3.append(insertionSort3.elapsedTime)
        xinsert3.append(insertionSort3.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xinsert = []
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input2 in input_sorted:
        insertionSort = Algorithm("insertionSort", input2, k)
        insertionSort.insertionSort()
        # print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        # xinsert.append(insertionSort.elapsedTime)
        xinsert.append(insertionSort.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xinsert2 = []
    # reversed
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        insertionSort2 = Algorithm("insertionSort", input3, k)
        insertionSort2.insertionSort()
        # print(insertionSort2.methodName, ":", insertionSort2.kthsmallest, ",", f"{insertionSort2.elapsedTime:0.9f}")
        # xinsert2.append(insertionSort2.elapsedTime)
        xinsert2.append(insertionSort2.counter)

    plt.figure(1)
    plt.plot(ns, xinsert, 'm-', label='insertionSort - sorted')
    plt.plot(ns, xinsert2, 'g-', label='insertionSort - reversed')
    plt.plot(ns, xinsert3, 'b-', label='insertionSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')

    # plt.show()
    plt.savefig('insertionSort-n-vs-time.png')
    plt.close()


def mergesortAnalyis(k):
    ns = []
    inputs = inputsInt(ns, "none")

    # --------------------------------- INITIAL ARRAY ---------------------------------
    xmerge3 = []
    for input in inputs:
        # save the array
        n = len(input)
        mergeSort3 = Algorithm("mergeSort", input, k)
        mergeSort3.mergeFinal()
        # print(mergeSort3.methodName, ":", mergeSort3.kthsmallest, ", ", f"{mergeSort3.elapsedTime:0.9f}")
        # xmerge3.append(mergeSort3.elapsedTime)
        xmerge3.append(mergeSort3.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xinsert = []
    xmerge = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input in input_sorted:
        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        # print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        # xmerge.append(mergeSort.elapsedTime)
        xmerge.append(mergeSort.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xmerge2 = []
    # reversed
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input in input_reversed:
        mergeSort2 = Algorithm("mergeSort", input, k)
        mergeSort2.mergeFinal()
        # print(mergeSort2.methodName, ":", mergeSort2.kthsmallest, ", ", f"{mergeSort2.elapsedTime:0.9f}")
        # xmerge2.append(mergeSort2.elapsedTime)
        xmerge2.append(mergeSort2.counter)

    plt.figure(1)
    plt.plot(ns, xmerge, 'm-', label='mergeSort - sorted')
    plt.plot(ns, xmerge2, 'g-', label='mergeSort - reversed')
    plt.plot(ns, xmerge3, 'b-', label='mergeSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    # plt.show()
    plt.savefig('mergeSort-n-vs-time.png')
    plt.close()


def quicksortAnalyis(k):
    ns = []
    inputs = inputsInt(ns, "none")

    # --------------------------------- INITIAL ARRAY ---------------------------------
    xquick3 = []
    for input in inputs:
        # save the array
        n = len(input)
        quicksort = Algorithm("quicksort", input, k)
        quicksort.quicksort(input, 0, n - 1, 0)
        # print(quicksort.methodName, ":", quicksort.kthsmallest, ",", f"{quicksort.elapsedTime:0.9f}")
        # xquick3.append(quicksort.elapsedTime)
        xquick3.append(quicksort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------

    xquick = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input in input_sorted:
        n = len(input)
        quicksort2 = Algorithm("quicksort", input, k)
        quicksort2.quicksort(input, 0, n - 1, 0)
        # print(quicksort2.methodName, ":", quicksort2.kthsmallest, ",", f"{quicksort2.elapsedTime:0.9f}")
        # xquick.append(quicksort2.elapsedTime)
        xquick.append(quicksort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xquick2 = []
    # reversed
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input in input_reversed:
        n = len(input)
        quicksort3 = Algorithm("quicksort", input, k)
        quicksort3.quicksort(input, 0, n - 1, 0)
        # print(quicksort3.methodName, ":", quicksort3.kthsmallest, ",", f"{quicksort3.elapsedTime:0.9f}")
        # xquick2.append(quicksort3.elapsedTime)
        xquick2.append(quicksort3.counter)

    plt.figure(1)
    plt.plot(ns, xquick, 'm-', label='quickSort - sorted')
    plt.plot(ns, xquick2, 'g-', label='quickSort - reversed')
    plt.plot(ns, xquick3, 'b-', label='quickSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    # plt.show()
    plt.savefig('quickSort-n-vs-time.png')
    plt.close()


def partialSelectionSortAnalyis(k):
    ns = []
    inputs = inputsInt(ns, "none")

    # --------------------------------- INITIAL ARRAY ---------------------------------
    xp3 = []
    for input in inputs:
        # save the array
        n = len(input)
        partialSelectionSort = Algorithm("partialSelectionSort", input, k)
        partialSelectionSort.partialSelectionSort()
        # print(partialSelectionSort.methodName, ":", partialSelectionSort.kthsmallest, ",",
        # f"{partialSelectionSort.elapsedTime:0.9f}")
        # print("counter 1:",partialSelectionSort.counter)
        # xp3.append(partialSelectionSort.elapsedTime)
        xp3.append(partialSelectionSort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------

    xp = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input in input_sorted:
        n = len(input)
        partialSelectionSort2 = Algorithm("partialSelectionSort", input, k)
        partialSelectionSort2.partialSelectionSort()
        # print(partialSelectionSort2.methodName, ":", partialSelectionSort2.kthsmallest, ",",
        # f"{partialSelectionSort2.elapsedTime:0.9f}")
        # xp.append(partialSelectionSort2.elapsedTime)
        # print("counter 2:", partialSelectionSort.counter)
        xp.append(partialSelectionSort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xp2 = []
    # reversed
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input in input_reversed:
        n = len(input)
        partialSelectionSort3 = Algorithm("partialSelectionSort", input, k)
        partialSelectionSort3.partialSelectionSort()
        # print(partialSelectionSort3.methodName, ":", partialSelectionSort3.kthsmallest, ",",
        # f"{partialSelectionSort3.elapsedTime:0.9f}")
        # xp2.append(partialSelectionSort3.elapsedTime)
        # print("counter 3:", partialSelectionSort3.counter)
        xp2.append(partialSelectionSort3.counter)

    plt.figure(1)
    plt.plot(ns, xp, 'm-', label='partialSelectionSort - sorted')
    plt.plot(ns, xp2, 'g-', label='partialSelectionSort - reversed')
    plt.plot(ns, xp3, 'b-', label='partialSelectionSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    # plt.show()
    plt.savefig('partialSelectionSort-n-vs-time.png')
    plt.close()


def main():
    k = 3
    # input_array = [12, 11, 13, 6, 4, 2, 19]
    ns = []
    # inputs = inputsInt(ns, "none")
    # inputs = inputsInt(ns,"sorted")
    inputs = inputsInt(ns, "reversed")

    ax = []
    bx = []
    cx = []
    dx = []
    ex = []
    fx = []

    insertionSortAnalysis(k)
    mergesortAnalyis(k)
    quicksortAnalyis(k)
    partialSelectionSortAnalyis(k)

    for input in inputs:
        # save the array
        n = len(input)

        # sortArrayList = saveArray(input)
        print("************************************")

        print("n = ", n)
        print(input)

        insertionSort = Algorithm("insertionSort", input, k)
        insertionSort.insertionSort()
        print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        ax.append(insertionSort.elapsedTime)

        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        bx.append(mergeSort.elapsedTime)

        quicksort = Algorithm("quicksort", input, k)
        quicksort.quicksort(input, 0, n - 1, 0)
        print(quicksort.methodName, ":", quicksort.kthsmallest, ",", f"{quicksort.elapsedTime:0.9f}")
        cx.append(quicksort.elapsedTime)

        partialSelectionSort = Algorithm("partialSelectionSort", input, k)
        partialSelectionSort.partialSelectionSort()
        print(partialSelectionSort.methodName, ":", partialSelectionSort.kthsmallest, ",",
              f"{partialSelectionSort.elapsedTime:0.9f}")
        dx.append(partialSelectionSort.elapsedTime)

        quickSelect = Algorithm("quickSelect", input, k)
        quickSelect.quickSelect(input, 0, n - 1, k, "none")
        print(quickSelect.methodName, ":", quickSelect.kthsmallest, ",", f"{quickSelect.elapsedTime:0.9f}")
        ex.append(quickSelect.elapsedTime)

        quickSelectwithmedian = Algorithm("quickSelectwithmedian", input, k)
        quickSelectwithmedian.quickSelect(input, 0, n - 1, k, "median")
        print(quickSelectwithmedian.methodName, ":", quickSelectwithmedian.kthsmallest, ",",
              f"{quickSelectwithmedian.elapsedTime:0.9f}")
        fx.append(quickSelectwithmedian.elapsedTime)

    # Plot - comparision of all
    plt.plot(ns, ax, 'c-', label='insertionSort')
    plt.plot(ns, bx, 'b-', label='mergeSort')
    plt.plot(ns, cx, 'y-', label='quickSort')
    plt.plot(ns, dx, 'r-', label='partialSelectionSort')
    plt.plot(ns, ex, 'm-', label='quickSelect')
    plt.plot(ns, fx, 'g-', label='quickSelectwithmedian')

    # plt.ylim([0, 0.02])
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')

    plt.show()
    # plt.savefig('n-vs-time.png')
    plt.close()


if __name__ == "__main__":
    main()
