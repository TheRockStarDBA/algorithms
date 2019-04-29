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
