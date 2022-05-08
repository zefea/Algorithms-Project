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


def inputsInt(list):
    inputs = []
    n = 50
    for i in range(5):
        input_array = generateInputRandom(n)
        inputs.append(input_array)
        list.append(n)
        n = n * 2
    return inputs


def averageInput(ns):
    avg = []
    for n in ns:
        inputs = []
        for i in range(5):
            input_array = generateInputRandom(n)
            inputs.append(input_array)
        avg.append(inputs)
    return avg


def sortthearrays(inputs):
    for inputx in inputs:
        inputx.sort()


def reversedsortthearrays(inputs):
    for inputx in inputs:
        inputx.sort(reverse=True)


def shufflethearrays(inputs):
    for inputx in inputs:
        random.shuffle(inputx)


def duplicateInput(ns):
    arr = []
    i = 0
    for n in ns:
        print(n)
        arr1 = []
        for i in range(n):
            arr1.append(1)
        arr.append(arr1)

    return arr


def plotvsforK(ns, arr, names, k, arrType):
    i = 0
    print(arr)

    k = [1, k, "n/2", "n-1"]
    j = 0
    x1 = 0
    y1 = 0
    next = 0

    figure, axis = plt.subplots(2, 2)
    for j in range(4):
        i = 0
        for ar in arr:
            axis[x1, y1].plot(ns, arr[i][j], 's-', label=names[i])
            i = i + 1
            print(x1, y1)
            axis[x1, y1].set_title("k = " + str(k[j]))
            axis[x1, y1].legend(loc='upper left')

        x1, y1 = updatexandy(x1, y1, next)

    for ax in axis.flat:
        ax.set(xlabel='input size', ylabel='time')

    name = "Comparison of different algorithms based on k values in " + arrType + " array"
    figure.suptitle(name)
    plt.tight_layout()
    # plt.show()
    filename = name + ".png"
    plt.savefig(filename)
    plt.close()


def plotSort(ns, xinsert, sortname):
    plt.figure(1)

    plt.plot(ns, xinsert[0], 's-', label=sortname + '- None')
    plt.plot(ns, xinsert[1], 's-', label=sortname + '- Sorted')
    plt.plot(ns, xinsert[2], 's-', label=sortname + '- Reverse Sorted')
    plt.plot(ns, xinsert[3], 's-', label=sortname + '- Duplicate')
    plt.plot(ns, xinsert[4], 's-', label=sortname + '- Average')

    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    plt.title(sortname)

    # plt.show()
    filename = sortname + ".png"
    plt.savefig(filename)
    plt.close()


def updatexandy(x1, y1, next):
    if next == 1:
        y1 = y1 + 1

    x1 = x1 + 1
    if x1 == 2:
        y1 = y1 + 1
        x1 = 0
        next = 1

    if y1 == 2:
        y1 = 1

    return x1, y1


def convert(xlist, ns, name):
    types = ["random list", "sorted list", "reversed sorted list", "duplicate list"]
    k = 0
    figure, axis = plt.subplots(2, 2)
    x1 = 0
    y1 = 0
    next = 0

    arr_ret = []
    for x in xlist:
        arr = []
        i = 0
        n1 = []
        n2 = []
        n3 = []
        n4 = []

        for i in range(5):
            n1.append(x[i][0])
            n2.append(x[i][1])
            n3.append(x[i][2])
            n4.append(x[i][3])

        arr.append(n1)
        arr.append(n2)
        arr.append(n3)
        arr.append(n4)

        plt.figure(1)
        print(x1, "and", y1)
        axis[x1, y1].plot(ns, n1, 's-', label='k=1')
        axis[x1, y1].plot(ns, n2, 's-', label='k=3')
        axis[x1, y1].plot(ns, n3, 's-', label='k=n/2')
        axis[x1, y1].plot(ns, n4, 's-', label='k=n')

        axis[x1, y1].legend(loc='upper left')
        axis[x1, y1].set_title(types[k])

        x1, y1 = updatexandy(x1, y1, next)

        k = k + 1
        arr_ret.append(arr)

    for ax in axis.flat:
        ax.set(xlabel='input size', ylabel='time')

    figure.suptitle("Different k values of " + name + ' with different inputs')
    plt.tight_layout()
    # plt.show()
    filename = "Different k values of " + name + " with different inputs" + ".png"
    plt.savefig(filename)
    plt.close()

    return arr_ret


def insertionLoop(inputs, k, type):
    xinsert = []
    xs = []
    for input1 in inputs:
        klist = [1, k]
        n = len(input1)
        klist.append(int(n / 2))
        klist.append(n)
        x1 = []
        for k2 in klist:
            if type == 'sorted':
                input1.sort()
            elif type == 'reversed sorted':
                input1.sort(reverse=True)
            else:
                random.shuffle(input1)

            insertionSort = Algorithm("insertionSort", input1, k2)
            insertionSort.insertionSort()
            if k2 == k:
                xinsert.append(insertionSort.elapsedTime)

            x1.append(insertionSort.elapsedTime)
            # xinsert.append(insertionSort.counter)
        xs.append(x1)

    return xinsert, xs


# --------------------------------- insertion ---------------------------------
def insertionSortAnalysis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    xinsertlist = []

    # --------------------------------- INITIAL ARRAY ---------------------------------
    xinsert, xs = insertionLoop(inputs, k, "initial")
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xinsert2, xs2 = insertionLoop(input_sorted, k, "sorted")
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xinsert3, xs3 = insertionLoop(input_reversed, k, "reversed sorted")
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xinsert4, xs4 = insertionLoop(input_dup, k, "duplicate")

    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xinsert5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            insertionSort5 = Algorithm("insertionSort", input5, k)
            insertionSort5.insertionSort()
            avg = avg + insertionSort5.elapsedTime
            # avg = avg + insertionSort5.counter

        xinsert5.append(avg / s)

    # Plot for only insertion sort when k=given parameter (e.g. k=3)
    xinsertlist.append(xinsert)  # random
    xinsertlist.append(xinsert2)  # sorted array
    xinsertlist.append(xinsert3)  # reversed sorted
    xinsertlist.append(xinsert4)  # duplicate
    xinsertlist.append(xinsert5)  # average
    plotSort(ns, xinsertlist, "Insertion Sort")

    # Plot for only insertion sort when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)  # random
    klistfinal.append(xs2)  # sorted array
    klistfinal.append(xs3)  # reversed sorted
    klistfinal.append(xs4)  # duplicate
    randomn1 = convert(klistfinal, ns, "Insertion Sort")

    return randomn1


def mergesortLoop(inputs, k, type):
    xmerge = []
    xs = []
    for input in inputs:
        klist = [1, k]
        n = len(input)
        klist.append(int(n / 2))
        klist.append(n)
        x1 = []
        for k2 in klist:
            if type == 'sorted':
                input.sort()
            elif type == 'reversed sorted':
                input.sort(reverse=True)
            else:
                random.shuffle(input)
            mergeSort = Algorithm("mergeSort", input, k2)
            mergeSort.mergeFinal()
            if k2 == k:
                xmerge.append(mergeSort.elapsedTime)

            x1.append(mergeSort.elapsedTime)
        xs.append(x1)
        # xmerge.append(mergeSort.counter)

    return xmerge, xs


def mergesortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xmerge, xs = mergesortLoop(inputs, k, "initial")
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xmerge2, xs2 = mergesortLoop(input_sorted, k, "sorted")
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xmerge3, xs3 = mergesortLoop(input_reversed, k, "reversed sorted")
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xmerge4, xs4 = mergesortLoop(input_dup, k, "duplicate")
    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xmerge5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            # k = len(input4) - 1
            mergeSort5 = Algorithm("mergeSort", input5, k)
            mergeSort5.mergeFinal()
            avg = avg + mergeSort5.elapsedTime
            # avg = avg + mergeSort5.counter

        xmerge5.append(avg / s)

    # Plot for only merge sort when k=given parameter (e.g. k=3)
    xmergelist = []
    xmergelist.append(xmerge)
    xmergelist.append(xmerge2)
    xmergelist.append(xmerge3)
    xmergelist.append(xmerge4)
    xmergelist.append(xmerge5)
    plotSort(ns, xmergelist, "Merge Sort")

    # Plot for only merge sort when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn2 = convert(klistfinal, ns, "Merge Sort")

    return randomn2


def quicksortLoop(inputs, k, type):
    xquick = []
    xs = []
    for input in inputs:
        klist = [1, k]
        n = len(input)
        klist.append(int(n / 2))
        klist.append(n)
        x1 = []
        for k2 in klist:
            if type == 'sorted':
                input.sort()
            elif type == 'reversed sorted':
                input.sort(reverse=True)
            else:
                random.shuffle(input)
            quicksort = Algorithm("quicksort", input, k2)
            quicksort.quicksort(input, 0, n - 1, 0)
            if k2 == k:
                xquick.append(quicksort.elapsedTime)

            x1.append(quicksort.elapsedTime)
        xs.append(x1)
        # xquick.append(quicksort.counter)

    return xquick, xs


def quicksortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xquick, xs = quicksortLoop(inputs, k, "initial")
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xquick2, xs2 = quicksortLoop(input_sorted, k, sorted)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xquick3, xs3 = quicksortLoop(input_reversed, k, "reversed sorted")
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xquick4, xs4 = quicksortLoop(input_dup, k, "duplicate")
    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xquick5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            # k = len(input4) - 1
            n = len(input5)
            quicksort5 = Algorithm("quicksort", input5, k)
            quicksort5.quicksort(input5, 0, n - 1, 0)
            avg = avg + quicksort5.elapsedTime
            # avg = avg + quicksort5.counter

        xquick5.append(avg / s)

    # Plot for only quick sort when k=given parameter (e.g. k=3)
    xquicklist = []
    xquicklist.append(xquick)
    xquicklist.append(xquick2)
    xquicklist.append(xquick3)
    xquicklist.append(xquick4)
    xquicklist.append(xquick5)
    plotSort(ns, xquicklist, "Quick Sort")

    # Plot for only quick sort when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn3 = convert(klistfinal, ns, "Quick Sort")
    return randomn3


def partialSelectionSortLoop(inputs, k, type):
    xp = []
    xs = []
    for input in inputs:
        klist = [1, k]
        n = len(input)
        klist.append(int(n / 2))
        klist.append(n)
        x1 = []
        for k2 in klist:

            if type == 'sorted':
                input.sort()
            elif type == 'reversed sorted':
                input.sort(reverse=True)
            else:
                random.shuffle(input)

            partialSelectionSort = Algorithm("partialSelectionSort", input, k2)
            partialSelectionSort.partialSelectionSort()
            if k2 == k:
                xp.append(partialSelectionSort.elapsedTime)

            x1.append(partialSelectionSort.elapsedTime)
        xs.append(x1)

    return xp, xs


def partialSelectionSortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xp, xs = partialSelectionSortLoop(inputs, k, "initial")
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xp2, xs2 = partialSelectionSortLoop(input_sorted, k, "sorted")
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xp3, xs3 = partialSelectionSortLoop(input_reversed, k, "reversed sorted")
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xp4, xs4 = partialSelectionSortLoop(input_dup, k, "duplicate")

    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xp5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            n = len(input5)
            partialSelectionSort5 = Algorithm("partialSelectionSort", input5, k)
            partialSelectionSort5.partialSelectionSort()
            avg = avg + partialSelectionSort5.elapsedTime
            # avg = avg + partialSelectionSort5.counter

        xp5.append(avg / s)

    xplist = []
    xplist.append(xp)
    xplist.append(xp2)
    xplist.append(xp3)
    xplist.append(xp4)
    xplist.append(xp5)
    plotSort(ns, xplist, "Partial-Selection-Sort")

    # Plot for only this sort algorithm when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn4 = convert(klistfinal, ns, "partialSelectionSort")
    return randomn4


def heapLoop(inputs, k, type):
    xp = []
    xs = []
    for input in inputs:
        klist = [1, k]
        n = len(input)
        klist.append(int(n / 2))
        klist.append(n)
        x1 = []
        for k2 in klist:
            if type == 'sorted':
                input.sort()
            elif type == 'reversed sorted':
                input.sort(reverse=True)
            else:
                random.shuffle(input)
            maxHeapSort = Algorithm("PartialHeapSort", input, k2)
            maxHeapSort.maxHeapSort()
            if k2 == k:
                xp.append(maxHeapSort.elapsedTime)

            x1.append(maxHeapSort.elapsedTime)
            # xinsert.append(insertionSort.counter)
        xs.append(x1)

    return xp, xs


def partialHeapSortAnalysis(k, inputs, ns):
    '''input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xp,xs = heapLoop(inputs,k)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xp2, xs2 = heapLoop(inputs,k)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xp3, xs3 = heapLoop(inputs, k)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xp4, xs4 = heapLoop(inputs, k)
    '''

    xp = []
    for input in inputs:
        n = len(input)
        maxHeapSort = Algorithm("PartialHeapSort", input, k)
        maxHeapSort.maxHeapSort()
        xp.append(maxHeapSort.elapsedTime)
        # xp.append(maxHeapSort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xp2 = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input2 in input_sorted:
        n = len(input2)
        maxHeapSort2 = Algorithm("PartialHeapSort", input2, k)
        maxHeapSort2.partialSelectionSort()
        xp2.append(maxHeapSort2.elapsedTime)
        # xp2.append(maxHeapSort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xp3 = []
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        n = len(input3)
        maxHeapSort3 = Algorithm("PartialHeapSort", input3, k)
        maxHeapSort3.partialSelectionSort()
        xp3.append(maxHeapSort3.elapsedTime)
        # xp3.append(maxHeapSort3.counter)

    input_dup = duplicateInput(ns)
    xp4 = []
    for input4 in input_dup:
        n = len(input4)
        maxHeapSort4 = Algorithm("PartialHeapSort", input4, k)
        maxHeapSort4.partialSelectionSort()
        xp4.append(maxHeapSort4.elapsedTime)
        # xp4.append(maxHeapSort4.counter)

    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xp5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            n = len(input5)
            maxHeapSort5 = Algorithm("PartialHeapSort", input5, k)
            maxHeapSort5.partialSelectionSort()
            avg = avg + maxHeapSort5.elapsedTime
            # avg = avg + maxHeapSort5.counter

        xp5.append(avg / s)

    xplist = []
    xplist.append(xp)
    xplist.append(xp2)
    xplist.append(xp3)
    xplist.append(xp4)
    xplist.append(xp5)
    plotSort(ns, xplist, "PartialHeapSort")

    '''
    # Plot for only this sort algorithm when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn5 = convert(klistfinal, ns, "PartialHeapSort")
    return randomn5
    '''


def generalComparision(k, inputs, ns):
    ax = []
    bx = []
    cx = []
    dx = []
    ex = []
    fx = []
    gx = []
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

        maxHeapSort = Algorithm("PartialHeapSort", input, k)
        maxHeapSort.maxHeapSort()
        print(maxHeapSort.methodName, ":", maxHeapSort.kthsmallest, ",",
              f"{maxHeapSort.elapsedTime:0.9f}")
        gx.append(maxHeapSort.elapsedTime)

        # Plot - comparision of all
    plt.plot(ns, ax, 's-', label='insertionSort')
    plt.plot(ns, bx, 's-', label='mergeSort')
    plt.plot(ns, cx, 's-', label='quickSort')
    plt.plot(ns, dx, 's-', label='partialSelectionSort')
    plt.plot(ns, ex, 's-', label='quickSelect')
    plt.plot(ns, fx, 's-', label='quickSelectwithmedian')
    plt.plot(ns, gx, 's-', label='maxHeapSort')

    # plt.ylim([0, 0.02])
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    plt.title("Comparision of Algorithms")

    # plt.show()
    plt.savefig('n-vs-time.png')
    plt.close()


def main():
    # generate random input

    ns = []
    inputs = inputsInt(ns)

    k = 3
    rs = []
    # algorithms analysis
    r1 = insertionSortAnalysis(k, inputs, ns)
    rs.append(r1)
    shufflethearrays(inputs)

    r2 = mergesortAnalyis(k, inputs, ns)
    rs.append(r2)
    shufflethearrays(inputs)

    r3 = quicksortAnalyis(k, inputs, ns)
    rs.append(r3)
    shufflethearrays(inputs)

    r4 = partialSelectionSortAnalyis(k, inputs, ns)
    rs.append(r4)
    shufflethearrays(inputs)

    r5 = partialHeapSortAnalysis(k, inputs, ns)
    # rs.append(r5)

    # comparision together
    generalComparision(k, inputs, ns)

    array_types = ["insertion", "merge", "quick", "partial selection"]
    # comparison based on different k values
    plotvsforK(ns, [r1[0], r2[0], r3[0], r4[0]], array_types, k, "Random")
    plotvsforK(ns, [r1[1], r2[1], r3[1], r4[1]], array_types, k, "Sorted")
    plotvsforK(ns, [r1[2], r2[2], r3[2], r4[2]], array_types, k, "Reversed Sorted")
    plotvsforK(ns, [r1[3], r2[3], r3[3], r4[3]], array_types, k, "Duplicate")


if __name__ == "__main__":
    main()
