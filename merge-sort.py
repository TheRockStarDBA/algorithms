""" Merge Sort

This is a very simple sorting algorithm. Because it's also very inefficient,
Bubble Sort is not practical for real-world use and is generally only discussed
in an academic context. The basic theory behind BubbleSort is that you take an
array of integers and iterate through it; for each element at some index  whose
value is greater than the element at the index following it (i.e., index i+1 ),
you must swap the two values. The act of swapping these values causes the larger,
unsorted values to float to the back (like a bubble) of the data structure until
they land in the correct location.

Asymptotic Analysis
Worst Case: O(n^2)
Best Case: O(n)
Average: O(n^2)
 """


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  #Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

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


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
