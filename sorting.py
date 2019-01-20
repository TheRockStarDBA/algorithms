""" Bubble Sort

This is a very simple sorting algorithm. Because it's also very inefficient, Bubble Sort is not practical
for real-world use and is generally only discussed in an academic context. The basic theory behind BubbleSort
is that you take an array of integers and iterate through it; for each element at some index  whose value
is greater than the element at the index following it (i.e., index i+1 ), you must swap the two values.
The act of swapping these values causes the larger, unsorted values to float to the back (like a bubble)
of the data structure until they land in the correct location.

Asymptotic Analysis
Worst Case: O(n^2)
Best Case: O(n)
Average: O(n^2)
 """

# Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:", arr)
""" Merge Sort

Topics: search and sorting

This is a very simple sorting algorithm. Because it's also very inefficient, Bubble Sort is not practical
for real-world use and is generally only discussed in an academic context. The basic theory behind BubbleSort
is that you take an array of integers and iterate through it; for each element at some index  whose value
is greater than the element at the index following it (i.e., index i+1 ), you must swap the two values.
The act of swapping these values causes the larger, unsorted values to float to the back (like a bubble)
of the data structure until they land in the correct location.

Asymptotic Analysis
Worst Case: O(n^2)
Best Case: O(n)
Average: O(n^2)
 """