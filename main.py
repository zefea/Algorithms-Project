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


def convert(xlist,ns):
    types = ["random list","sorted list","reversed sorted list","duplicate list"]
    k = 0
    for x in xlist:
        i = 0
        n1 = []
        n2 = []
        n3 = []
        n4 = []
        for i in range(5):
            print("x is:",x)
            n1.append(x[i][0])
            n2.append(x[i][1])
            n3.append(x[i][2])
            n4.append(x[i][3])

        # print(n1)
        plt.figure(1)

        plt.plot(ns, n1, 's-', label='k=0')
        plt.plot(ns, n2, 's-', label='k=3')
        plt.plot(ns, n3, 's-', label='k=n/2')
        plt.plot(ns, n4, 's-', label='k=n-1')


        plt.legend(loc='upper left')
        plt.xlabel('input size')
        plt.ylabel('time')
        plt.title("Different k values of insertion sort in a " + types[k])
        k = k + 1

        plt.show()
        plt.close()

# --------------------------------- insertion ---------------------------------
def insertionSortAnalysis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xinsertlist = []
    xinsert = []
    klist = [1, k]
    xs = []
    for input1 in inputs:
        n = len(input1)
        klist.append(int(n / 2))
        klist.append(n - 1)
        x1 = []
        for k2 in klist:
            insertionSort = Algorithm("insertionSort", input1, k2)
            insertionSort.insertionSort()
            if k2 == k:
                xinsert.append(insertionSort.elapsedTime)

            x1.append(insertionSort.elapsedTime)
            # xinsert.append(insertionSort.counter)
        xs.append(x1)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xinsert2 = []
    klist2 = [1, k]
    xs2 = []
    sortthearrays(input_sorted)
    for input2 in input_sorted:
        # k = len(input2) - 1
        n = len(input2)
        klist2.append(int(n / 2))
        klist2.append(n - 1)
        x1 = []
        for k2 in klist2:
            insertionSort2 = Algorithm("insertionSort", input2, k2)
            insertionSort2.insertionSort()
            if k2 == k:
                xinsert2.append(insertionSort2.elapsedTime)

            x1.append(insertionSort2.elapsedTime)
        xs2.append(x1)
        # xinsert2.append(insertionSort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xinsert3 = []
    # reversed
    klist3 = [1, k]
    xs3 = []
    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        # k = len(input3) - 1
        n = len(input3)
        klist3.append(int(n / 2))
        klist3.append(n - 1)
        x1 = []
        for k2 in klist3:
            insertionSort3 = Algorithm("insertionSort", input3, k2)
            insertionSort3.insertionSort()
            if k2 == k:
                xinsert3.append(insertionSort3.elapsedTime)
            x1.append(insertionSort3.elapsedTime)

        xs3.append(x1)
        # xinsert3.append(insertionSort3.counter)

    input_dup = duplicateInput(ns)
    xinsert4 = []
    klist4 = [1, k]
    xs4 = []
    for input4 in input_dup:
        # k = len(input4) - 1
        n = len(input4)
        klist4.append(int(n / 2))
        klist4.append(n - 1)
        x1 = []
        for k2 in klist4:
            insertionSort4 = Algorithm("insertionSort", input4, k2)
            insertionSort4.insertionSort()
            if k2 == k:
                xinsert4.append(insertionSort4.elapsedTime)
            x1.append(insertionSort4.elapsedTime)

        xs4.append(x1)
        # xinsert4.append(insertionSort4.counter)

    avgArray = averageInput(ns)
    xinsert5 = []
    avg = 0
    klist5 = [1, k]
    xs5 = []
    for input_avg in avgArray:
        s = len(input_avg)
        x1 = []
        for k2 in klist5:
            for input5 in input_avg:
                # k = len(input4) - 1
                n = len(input5)
                klist5.append(int(n / 2))
                klist5.append(n - 1)
                insertionSort5 = Algorithm("insertionSort", input5, k2)
                insertionSort5.insertionSort()
                avg = avg + insertionSort5.elapsedTime

                klist5.remove(int(n / 2))
                klist5.remove(n - 1)
                # avg = avg + insertionSort5.counter
            if k2 == k:
                xinsert5.append(avg / s)
            x1.append(avg / s)

        xs5.append(x1)

    xinsertlist.append(xinsert)
    xinsertlist.append(xinsert2)
    xinsertlist.append(xinsert3)
    xinsertlist.append(xinsert4)
    xinsertlist.append(xinsert5)

    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)

    convert(klistfinal,ns)

    plotSort(ns, xinsertlist, "Insertion Sort")


def mergesortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xmerge = []
    for input in inputs:
        # save the array
        n = len(input)
        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        xmerge.append(mergeSort.elapsedTime)
        # xmerge.append(mergeSort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xmerge2 = []

    sortthearrays(input_sorted)
    for input2 in input_sorted:
        mergeSort2 = Algorithm("mergeSort", input2, k)
        mergeSort2.mergeFinal()
        xmerge2.append(mergeSort2.elapsedTime)
        # xmerge2.append(mergeSort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xmerge3 = []

    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        mergeSort3 = Algorithm("mergeSort", input3, k)
        mergeSort3.mergeFinal()
        xmerge3.append(mergeSort3.elapsedTime)
        # xmerge3.append(mergeSort3.counter)

    input_dup = duplicateInput(ns)
    xmerge4 = []
    for input4 in input_dup:
        mergeSort4 = Algorithm("mergeSort", input4, k)
        mergeSort4.mergeFinal()
        xmerge4.append(mergeSort4.elapsedTime)
        # xmerge4.append(mergeSort4.counter)

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

    xmergelist = []
    xmergelist.append(xmerge)
    xmergelist.append(xmerge2)
    xmergelist.append(xmerge3)
    xmergelist.append(xmerge4)
    xmergelist.append(xmerge5)

    plotSort(ns, xmergelist, "Merge Sort")


def quicksortAnalyis(k, inputs, ns):
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xquick = []
    for input in inputs:
        # save the array
        n = len(input)
        quicksort = Algorithm("quicksort", input, k)
        quicksort.quicksort(input, 0, n - 1, 0)
        xquick.append(quicksort.elapsedTime)
        # xquick.append(quicksort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xquick2 = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input2 in input_sorted:
        n = len(input2)
        quicksort2 = Algorithm("quicksort", input2, k)
        quicksort2.quicksort(input2, 0, n - 1, 0)
        xquick2.append(quicksort2.elapsedTime)
        # xquick2.append(quicksort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xquick3 = []
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        n = len(input3)
        quicksort3 = Algorithm("quicksort", input3, k)
        quicksort3.quicksort(input3, 0, n - 1, 0)
        xquick3.append(quicksort3.elapsedTime)
        # xquick3.append(quicksort3.counter)

    input_dup = duplicateInput(ns)
    xquick4 = []
    for input4 in input_dup:
        n = len(input4)
        quicksort4 = Algorithm("quicksort", input4, k)
        quicksort4.quicksort(input4, 0, n - 1, 0)
        xquick4.append(quicksort4.elapsedTime)
        # xquick4.append(quicksort4.counter)

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

    xquicklist = []
    xquicklist.append(xquick)
    xquicklist.append(xquick2)
    xquicklist.append(xquick3)
    xquicklist.append(xquick4)
    xquicklist.append(xquick5)

    plotSort(ns, xquicklist, "Quick Sort")


def partialSelectionSortAnalyis(k, inputs, ns):
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xp = []
    for input in inputs:
        partialSelectionSort = Algorithm("partialSelectionSort", input, k)
        partialSelectionSort.partialSelectionSort()
        xp.append(partialSelectionSort.elapsedTime)
        # xp.append(partialSelectionSort.counter)

    # --------------------------------- SORTED ARRAY ---------------------------------
    xp2 = []
    # sorted
    input_sorted = inputs.copy()
    sortthearrays(input_sorted)
    for input2 in input_sorted:
        n = len(input2)
        partialSelectionSort2 = Algorithm("partialSelectionSort", input2, k)
        partialSelectionSort2.partialSelectionSort()
        xp2.append(partialSelectionSort2.elapsedTime)
        # xp2.append(partialSelectionSort2.counter)

    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    xp3 = []
    input_reversed = inputs.copy()
    reversedsortthearrays(input_reversed)
    for input3 in input_reversed:
        n = len(input3)
        partialSelectionSort3 = Algorithm("partialSelectionSort", input3, k)
        partialSelectionSort3.partialSelectionSort()
        xp3.append(partialSelectionSort3.elapsedTime)
        # xp3.append(partialSelectionSort3.counter)

    input_dup = duplicateInput(ns)
    xp4 = []
    for input4 in input_dup:
        n = len(input4)
        partialSelectionSort4 = Algorithm("partialSelectionSort", input4, k)
        partialSelectionSort4.partialSelectionSort()
        xp4.append(partialSelectionSort4.elapsedTime)
        # xp4.append(partialSelectionSort4.counter)

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


def partialHeapSortAnalysis(k, inputs, ns):
    # --------------------------------- INITIAL ARRAY ---------------------------------
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
    inputs = inputsInt(ns, "none")

    k = 3

    # algorithms analysis
    insertionSortAnalysis(k, inputs, ns)
    shufflethearrays(inputs)
    mergesortAnalyis(k, inputs, ns)
    shufflethearrays(inputs)
    quicksortAnalyis(k, inputs, ns)
    shufflethearrays(inputs)
    partialSelectionSortAnalyis(k, inputs, ns)
    shufflethearrays(inputs)
    partialHeapSortAnalysis(k, inputs, ns)

    # comparision together
    generalComparision(k, inputs, ns)


if __name__ == "__main__":
    main()
