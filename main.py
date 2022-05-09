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
    randarray = []
    i = 0
    while i != n:
        randnum = random.randint(0, 1000)
        if randnum not in randarray:
            randarray.append(randnum)
            i = i + 1

    return randarray


# do not consider best or worst cases, just a random input for now
def generateInputRandom2(n):
    randnums = np.random.randint(1, 1000, n)
    return list(randnums)


def inputsInt(list):
    inputs = []

    i = 0
    n = 60
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
        # print(n)
        arr1 = []
        for i in range(n):
            arr1.append(1)
        arr.append(arr1)

    return arr


def plotvsforK(ns, arr, names, k, arrType):
    i = 0
    # print(arr)

    k = [1, k, "n/2", "n"]
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
            # print(x1, y1)
            axis[x1, y1].set_title("k = " + str(k[j]))
            #axis[x1, y1].legend(loc='upper left')

        x1, y1 = updatexandy(x1, y1, next)

    for ax in axis.flat:
        ax.set(xlabel='input size', ylabel='time')

    name = "Comparison of different algorithms\nbased on k values in " + arrType + " array"
    figure.suptitle(name)
    plt.tight_layout()
    lines, labels = figure.axes[-1].get_legend_handles_labels()
    figure.legend(lines, labels, loc="upper left",fontsize = 'x-small',labelspacing=0.)

    # plt.show()
    filename = "Comparison of different algorithms based on k values in " + arrType + " array" + ".png"
    print(filename)
    plt.savefig(filename)
    plt.close()


def plotSort(ns, xinsert, sortname):

    print("plotting ",sortname)
    plt.figure(1)

    plt.plot(ns, xinsert[0], 's-', label='Distinct random')
    plt.plot(ns, xinsert[1], 's-', label='Sorted')
    plt.plot(ns, xinsert[2], 's-', label='Reverse Sorted')
    plt.plot(ns, xinsert[3], 's-', label='Duplicate')
    plt.plot(ns, xinsert[4], 's-', label='Average')

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
    types = ["Distinct random", "Sorted", "Reverse sorted", "Duplicate"]
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
        # print(x1, "and", y1)
        axis[x1, y1].plot(ns, n1, 's-', label='k=1')
        axis[x1, y1].plot(ns, n2, 's-', label='k=3')
        axis[x1, y1].plot(ns, n3, 's-', label='k=n/2')
        axis[x1, y1].plot(ns, n4, 's-', label='k=n')
        axis[x1, y1].set_title(types[k])
        x1, y1 = updatexandy(x1, y1, next)

        k = k + 1
        arr_ret.append(arr)

    for ax in axis.flat:
        ax.set(xlabel='input size', ylabel='time')

    figure.suptitle("Different k values of " + name + '\nwith different inputs')
    plt.tight_layout()
    lines, labels = figure.axes[-1].get_legend_handles_labels()
    figure.legend(lines, labels, loc='upper left', labelspacing=0.)

    # plt.show()
    # print(name)
    filename = "Different k values of " + name + " with different inputs" + ".png"
    plt.savefig(filename)
    plt.close()

    return arr_ret


def insertionLoop(inputs, k, f):
    xinsert = []

    for input in inputs:
        f.write("\nn= " + str(len(input)))
        f.write("\ninput: \n" + str(input))
        insertionSort = Algorithm("insertionSort", input, k)
        insertionSort.insertionSort()
        xinsert.append(insertionSort.elapsedTime)
        f.write("\nelapsed times: \n" + str(insertionSort.elapsedTime))

    return xinsert


# --------------------------------- insertion ---------------------------------
def insertionSortAnalysis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    xinsertlist = []
    with open('output.txt', 'w') as f:
        f.write("Insertion Sort Analyis\n")

        f.write("\n--------------------------------- INITIAL ARRAY ---------------------------------\n")
        xinsert = insertionLoop(inputs, k, f)
        f.write("\n--------------------------------- SORTED ARRAY ---------------------------------\n")
        sortthearrays(input_sorted)
        xinsert2 = insertionLoop(input_sorted, k, f)
        f.write("\n--------------------------------- REVERSED SORTED ARRAY ---------------------------------\n")
        reversedsortthearrays(input_reversed)
        xinsert3 = insertionLoop(input_reversed, k, f)
        f.write("\n--------------------------------- DUPLICATE ARRAY ---------------------------------\n")
        input_dup = duplicateInput(ns)
        xinsert4 = insertionLoop(input_dup, k, f)

        f.write("\n--------------------------------- AVERAGE ---------------------------------\n")
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

        f.write("\nAverage when k:" + str(k))
        f.write("\nelapsed times: \n" + str(xinsert5))
        # Plot for only insertion sort when k=given parameter (e.g. k=3)
        xinsertlist.append(xinsert)  # random
        xinsertlist.append(xinsert2)  # sorted array
        xinsertlist.append(xinsert3)  # reversed sorted
        xinsertlist.append(xinsert4)  # duplicate
        xinsertlist.append(xinsert5)  # average
        plotSort(ns, xinsertlist, "Insertion-Sort")


def mergesortLoop(inputs, k):
    xmerge = []

    for input in inputs:
        mergeSort = Algorithm("mergeSort", input, k)
        mergeSort.mergeFinal()
        xmerge.append(mergeSort.elapsedTime)
        # xmerge.append(mergeSort.counter)

    return xmerge


def mergesortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xmerge = mergesortLoop(inputs, k)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xmerge2 = mergesortLoop(input_sorted, k)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xmerge3 = mergesortLoop(input_reversed, k)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xmerge4 = mergesortLoop(input_dup, k)
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
    plotSort(ns, xmergelist, "Merge-Sort")


def quicksortLoop(inputs, k):
    xquick = []

    for input in inputs:
        n = len(input)
        quicksort = Algorithm("quicksort", input, k)
        quicksort.quicksort(input, 0, n - 1, 0)
        xquick.append(quicksort.elapsedTime)
        # xquick.append(quicksort.counter)

    return xquick


def quicksortAnalyis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xquick = quicksortLoop(inputs, k)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xquick2 = quicksortLoop(input_sorted, k)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xquick3 = quicksortLoop(input_reversed, k)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xquick4 = quicksortLoop(input_dup, k)
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
    xquicklist.append(xquick3 )
    xquicklist.append(xquick4)
    xquicklist.append(xquick5)
    plotSort(ns, xquicklist, "Quick-Sort")


def partialSelectionSortLoop(inputs, k):
    xp = []
    xs = []
    for input in inputs:
        n = len(input)
        klist = [1, k, int(n / 2), n]
        x1 = []
        for k2 in klist:

            input_k = input.copy()
            partialSelectionSort = Algorithm("partialSelectionSort", input_k, k2)
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
    xp, xs = partialSelectionSortLoop(inputs, k)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xp2, xs2 = partialSelectionSortLoop(input_sorted, k)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xp3, xs3 = partialSelectionSortLoop(input_reversed, k)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xp4, xs4 = partialSelectionSortLoop(input_dup, k)

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
    plotSort(ns, xplist, "Partial Selection-Sort")

    # Plot for only this sort algorithm when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn4 = convert(klistfinal, ns, "Partial Selection-Sort")
    return randomn4


def quickselectLoop(inputs, k, type):
    ex = []
    xs = []
    for input in inputs:
        n = len(input)
        klist = [1, k, int(n / 2), n]
        x1 = []
        for k2 in klist:
            input_k = input.copy()
            quickSelect = Algorithm("quickSelect", input_k, k2)
            quickSelect.quickSelect(input_k, 0, n - 1, k, type)

            if k2 == k:
                ex.append(quickSelect.elapsedTime)

            x1.append(quickSelect.elapsedTime)
        xs.append(x1)
        # xquick.append(quicksort.counter)
    return ex, xs


def quickselectsortAnalyis(k, inputs, ns, fun_type):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xselect, xs = quickselectLoop(inputs, k, fun_type)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xselect2, xs2 = quickselectLoop(input_sorted, k, fun_type)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xselect3, xs3 = quickselectLoop(input_reversed, k, fun_type)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xselect4, xs4 = quickselectLoop(input_dup, k, fun_type)
    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xselect5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            # k = len(input4) - 1
            n = len(input5)
            quickSelect = Algorithm("quickSelect", input5, k)
            quickSelect.quickSelect(input5, 0, n - 1, k, fun_type)
            avg = avg + quickSelect.elapsedTime
            # avg = avg + quicksort5.counter

        xselect5.append(avg / s)

    # Plot for only quick sort when k=given parameter (e.g. k=3)
    xselectlist = []
    xselectlist.append(xselect)
    xselectlist.append(xselect2)
    xselectlist.append(xselect3)
    xselectlist.append(xselect4)
    xselectlist.append(xselect5)
    name = "Quick Select: " + fun_type
    plotSort(ns, xselectlist, f"Quick Select - {fun_type}")

    # Plot for only quick sort when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn6 = convert(klistfinal, ns, f"Quick Select - {fun_type}")
    return randomn6


def heapLoop(inputs, k):
    xp = []
    xs = []
    for input in inputs:
        n = len(input)
        klist = [1, k, int(n / 2), n]
        x1 = []
        for k2 in klist:
            input_k = input.copy()
            maxHeapSort = Algorithm("PartialHeapSort", input_k, k2)
            maxHeapSort.maxHeapSort()
            if k2 == k:
                xp.append(maxHeapSort.elapsedTime)

            x1.append(maxHeapSort.elapsedTime)
            # xinsert.append(insertionSort.counter)
        xs.append(x1)

    return xp, xs


def partialHeapSortAnalysis(k, inputs, ns):
    input_sorted = inputs.copy()
    input_reversed = inputs.copy()
    # --------------------------------- INITIAL ARRAY ---------------------------------
    xp, xs = heapLoop(inputs, k)
    # --------------------------------- SORTED ARRAY ---------------------------------
    sortthearrays(input_sorted)
    xp2, xs2 = heapLoop(input_sorted, k)
    # --------------------------------- REVERSED SORTED ARRAY ---------------------------------
    reversedsortthearrays(input_reversed)
    xp3, xs3 = heapLoop(input_reversed, k)
    # --------------------------------- DUPLICATE ARRAY ---------------------------------
    input_dup = duplicateInput(ns)
    xp4, xs4 = heapLoop(input_dup, k)

    # --------------------------------- AVERAGE ---------------------------------
    avgArray = averageInput(ns)
    xp5 = []
    avg = 0
    for input_avg in avgArray:
        s = len(input_avg)
        for input5 in input_avg:
            n = len(input5)
            maxHeapSort5 = Algorithm("PartialHeapSort", input5, k)
            maxHeapSort5.maxHeapSort()
            avg = avg + maxHeapSort5.elapsedTime
            # avg = avg + maxHeapSort5.counter

        xp5.append(avg / s)

    xplist = []
    xplist.append(xp)
    xplist.append(xp2)
    xplist.append(xp3)
    xplist.append(xp4)
    xplist.append(xp5)
    plotSort(ns, xplist, "Partial Heap-Sort")

    # Plot for only this sort algorithm when k = [1,k,n/2,n] for every array type
    # Ex: Random array (xs) --> comparision when k=1,k=3,k=n/2,k=n
    klistfinal = []
    klistfinal.append(xs)
    klistfinal.append(xs2)
    klistfinal.append(xs3)
    klistfinal.append(xs4)
    randomn5 = convert(klistfinal, ns, "Partial Heap-Sort")
    return randomn5


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
        input_k = input.copy()
        # sortArrayList = saveArray(input)
        print("************************************")

        print("n = ", n)
        print(input)

        insertionSort = Algorithm("insertionSort", input_k, k)
        insertionSort.insertionSort()
        print(insertionSort.methodName, ":", insertionSort.kthsmallest, ",", f"{insertionSort.elapsedTime:0.9f}")
        ax.append(insertionSort.elapsedTime)

        input_k = input.copy()
        mergeSort = Algorithm("mergeSort", input_k, k)
        mergeSort.mergeFinal()
        print(mergeSort.methodName, ":", mergeSort.kthsmallest, ", ", f"{mergeSort.elapsedTime:0.9f}")
        bx.append(mergeSort.elapsedTime)

        input_k = input.copy()
        quicksort = Algorithm("quicksort", input_k, k)
        quicksort.quicksort(input_k, 0, n - 1, 0)
        print(quicksort.methodName, ":", quicksort.kthsmallest, ",", f"{quicksort.elapsedTime:0.9f}")
        cx.append(quicksort.elapsedTime)

        input_k = input.copy()
        partialSelectionSort = Algorithm("partialSelectionSort", input_k, k)
        partialSelectionSort.partialSelectionSort()
        print(partialSelectionSort.methodName, ":", partialSelectionSort.kthsmallest, ",",
              f"{partialSelectionSort.elapsedTime:0.9f}")
        dx.append(partialSelectionSort.elapsedTime)

        input_k = input.copy()
        quickSelect = Algorithm("quickSelect", input_k, k)
        quickSelect.quickSelect(input_k, 0, n - 1, k, "none")
        print(quickSelect.methodName, ":", quickSelect.kthsmallest, ",", f"{quickSelect.elapsedTime:0.9f}")
        ex.append(quickSelect.elapsedTime)

        input_k = input.copy()
        quickSelectwithmedian = Algorithm("quickSelectwithmedian", input_k, k)
        quickSelectwithmedian.quickSelect(input_k, 0, n - 1, k, "median")
        print(quickSelectwithmedian.methodName, ":", quickSelectwithmedian.kthsmallest, ",",
              f"{quickSelectwithmedian.elapsedTime:0.9f}")
        fx.append(quickSelectwithmedian.elapsedTime)

        input_k = input.copy()
        maxHeapSort = Algorithm("PartialHeapSort", input_k, k)
        maxHeapSort.maxHeapSort()
        print(maxHeapSort.methodName, ":", maxHeapSort.kthsmallest, ",",
              f"{maxHeapSort.elapsedTime:0.9f}")
        gx.append(maxHeapSort.elapsedTime)

        # Plot - comparision of all
    plt.plot(ns, ax, 's-', label='Insertion-sort')
    plt.plot(ns, bx, 's-', label='Merge-sort')
    plt.plot(ns, cx, 's-', label='Quick-sort')
    plt.plot(ns, dx, 's-', label='Partial Selection-sort')
    plt.plot(ns, ex, 's-', label='Quick Select')
    plt.plot(ns, fx, 's-', label='Quick Select with median of three')
    plt.plot(ns, gx, 's-', label='Partial Heap-sort')

    # plt.ylim([0, 0.02])
    plt.legend(loc='upper left')
    plt.xlabel('input size')
    plt.ylabel('time')
    plt.title("Comparision of Algorithms")

    #plt.show()
    plt.savefig('n-vs-time.png')
    plt.close()


def main():
    # generate random input

    ns = []
    inputs = inputsInt(ns)

    k = 3

    # algorithms analysis
    inputs_k = inputs.copy()
    insertionSortAnalysis(k, inputs_k, ns)
    shufflethearrays(inputs)

    inputs_k = inputs.copy()
    mergesortAnalyis(k, inputs_k, ns)
    shufflethearrays(inputs)

    inputs_k = inputs.copy()
    quicksortAnalyis(k, inputs_k, ns)
    shufflethearrays(inputs)

    inputs_k = inputs.copy()
    r4 = partialSelectionSortAnalyis(k, inputs_k, ns)
    shufflethearrays(inputs)

    inputs_k = inputs.copy()
    r5 = quickselectsortAnalyis(k, inputs_k, ns, "first")

    shufflethearrays(inputs)
    inputs_k = inputs.copy()
    r6 = quickselectsortAnalyis(k, inputs_k, ns, "median")

    shufflethearrays(inputs)
    r7 = partialHeapSortAnalysis(k, inputs, ns)
    shufflethearrays(inputs)

    # comparision together
    inputs_k = inputs.copy()
    generalComparision(k, inputs_k, ns)

    array_types = ["Partial Selection-sort", "Quick Select", "Quick Select with median of three","Partial Heap-sort"]
    # comparison based on different k values

    plotvsforK(ns, [r4[0], r5[0], r6[0],r7[0]], array_types, k, "Random")
    plotvsforK(ns, [r4[1], r5[1], r6[1],r7[1]], array_types, k, "Sorted")
    plotvsforK(ns, [r4[2], r5[2], r6[2],r7[2]], array_types, k, "Reverse Sorted")
    plotvsforK(ns, [r4[3], r5[3], r6[3],r7[3]], array_types, k, "Duplicate")

if __name__ == "__main__":
    main()
