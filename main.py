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
        if type == 'sorted':
            input_array.sort()
        if type == 'reversed':
            input_array.reverse()

    return inputs

def sortthearrays(inputs):
    for input in inputs:
        input.sort()

def reversedsortthearrays(inputs):
    for input in inputs:
        input.sort()
        input.reverse()

def sortInvidiualComparision(k):
    ns = []
    inputs = inputsInt(ns, "none")

    xinsert = []
    xmerge = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input in input_sorted:
        # save the array
        n = len(input)
        insertionSort = Algorithm("insertionSort", input, k)
        insertionSort.insertionSort()
        print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        xinsert.append(insertionSort.elapsedTime)

        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        xmerge.append(mergeSort.elapsedTime)
        #xmerge.append(mergeSort.counter)

    xinsert2 = []
    xmerge2 = []
    # reversed
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input in input_reversed:
        # save the array
        n = len(input)

        insertionSort = Algorithm("insertionSort", input, k)
        insertionSort.insertionSort()
        print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        xinsert2.append(insertionSort.elapsedTime)

        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        xmerge2.append(mergeSort.elapsedTime)
        #xmerge2.append(mergeSort.counter)


    # none
    xinsert3 = []
    xmerge3 = []
    for input in inputs:
        # save the array
        n = len(input)

        insertionSort = Algorithm("insertionSort", input, k)
        insertionSort.insertionSort()
        print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        xinsert3.append(insertionSort.elapsedTime)

        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        xmerge3.append(mergeSort.elapsedTime)
        #xmerge3.append(mergeSort.counter)

    plt.figure(1)
    plt.plot(ns, xinsert, 'm-', label='insertionSort - sorted')
    plt.plot(ns, xinsert2, 'g-', label='insertionSort - reversed')
    plt.plot(ns, xinsert3, 'b-', label='insertionSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')

    plt.figure(2)
    plt.plot(ns, xmerge, 'm-', label='mergeSort - sorted')
    plt.plot(ns, xmerge2, 'g-', label='mergeSort - reversed')
    plt.plot(ns, xmerge3, 'b-', label='mergeSort - none')
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')

    plt.show()
    # plt.savefig('n-vs-time.png')
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

    sortInvidiualComparision(k)

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
