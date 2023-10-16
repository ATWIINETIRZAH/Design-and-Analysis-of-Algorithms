# Design-and-Analysis-of-Algorithms
design and analysis of algorithms, Big O complexity, and time and space complexity of algorithms 

**Quick Sort:**

**What it is**: Quick Sort is a comparison-based sorting algorithm known for its efficiency and widely used in practice. It's based on the divide-and-conquer strategy. It selects a 'pivot' element and partitions the array into two subarrays – elements less than the pivot and elements greater than the pivot. The subarrays are then recursively sorted.

**Explanation**:

The quick_sort function takes an array as input and is designed to sort it using the Quick Sort algorithm.
It begins by checking the length of the array. If the array contains one element or no elements, it's considered already sorted, and the original array is returned.
The pivot element is chosen as the middle element of the array (pivot = array[len(array) // 2]).
Three subarrays are created:
left: Contains elements that are less than the pivot.
middle: Contains elements that are equal to the pivot. This is important when there are multiple occurrences of the pivot value.
right: Contains elements that are greater than the pivot.
Recursion is used to sort the left and right subarrays. The quick_sort function is called recursively on these subarrays.
The sorted subarrays (left, middle, and right) are concatenated to form the final sorted array.
Finally, the sorted array is returned, and the code demonstrates how to use the quick_sort function to sort a test list (test_list)

Quick Sort works by selecting a pivot, partitioning the array, and recursively sorting the subarrays. 

<img width="409" alt="quick sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/b68a93d5-d137-4cfa-b5ed-017d46cd9a0f">

**Analysis:** 
Quick Sort has an average-case time complexity of O(n log n) and is often faster than other sorting algorithms in practice. However, its worst-case time complexity is O(n^2) when poorly chosen pivots lead to unbalanced partitions.


**Counting Sort:**

**What it is:** Counting Sort is a non-comparison-based sorting algorithm that works well for integers or values within a limited range. The algorithm works by counting the frequency of each element in the input array and using this information to place the elements in their correct sorted position.
It creates a "counting array" to store the count of each unique element in the input array.
Then, it uses the counting array to reconstruct the sorted output array.
It counts the occurrences of each element and uses this information to place elements in their correct sorted positions.

**Explanation**
The counting_sort function takes an array as input and is designed to sort it using the Counting Sort algorithm.
It begins by finding the maximum and minimum values in the input array using the max and min functions.
The range of elements is calculated by subtracting the minimum value from the maximum value and adding 1.
Two arrays are created:
count_array: This array is used to count how many times each element appears in the input array. It is initialized with zeros.
output_array: This will store the sorted elements and is initially filled with zeros.
A loop iterates through the input array and increments the count in the count_array for each element. The adjustment of num - min_val ensures that the counts are stored at the correct positions in the count_array.
Another loop modifies the count_array to contain the correct positions of each element. This step ensures that the elements will be placed in the correct order in the output array.
A final loop iterates backward through the input array, placing elements in their sorted positions in the output_array based on the counts stored in the count_array.
The function returns the output_array, which contains the sorted elements.
The example usage at the end of the code demonstrates how to use the counting_sort function to sort a test list (test_list).

<img width="524" alt="counting sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/0e52961a-9b0d-43af-882d-f1906e82d39a">


**Analysis:**
Counting Sort is efficient for sorting integers within a small range and has a time complexity of O(n + k), where n is the number of elements, and k is the range of input values.
Counting Sort is efficient when the range of input values (k) is not significantly larger than the number of elements (n)

**Heap Sort:**

**What it is:**
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. The algorithm consists of two main phases: heapification and sorting.
In the heapification phase, the input array is transformed into a binary heap, where each parent node is greater (for max-heap) or smaller (for min-heap) than its children.
Once the binary heap is built, the largest (for max-heap) or smallest (for min-heap) element (the root) is removed and placed at the end of the sorted array.
The heap property is then restored by sifting down the new root, and this process is repeated until the entire array is sorted.
It builds a max-heap (for ascending order) from the input array and repeatedly removes the maximum element (the root) and inserts it into the sorted portion of the array.

**Explanation:**

heapify is a helper function that maintains the max-heap property of a subtree rooted at a given index i.
It takes three arguments: array (the array to be sorted), n (the size of the heap or subtree), and i (the index of the current root of the subtree).
It initializes largest with the current root index i, left as the index of the left child, and right as the index of the right child.
It checks if the left child exists (left < n) and if it's greater than the current largest. If so, it updates largest to the left child's index.
Similarly, it checks if the right child exists (right < n) and if it's greater than the current largest. If so, it updates largest to the right child's index.
If largest is not equal to the original i, it means that a swap is needed to maintain the max-heap property. So, it swaps the elements at indices i and largest and recursively calls heapify on the subtree rooted at the new largest index.
heap_sort Function:
heap_sort is the main sorting function that takes an array (array2) as input.
It starts by calculating the length of the input array array2 and assigns it to n.
Next, it builds a max heap from the input array by iterating over the elements from the middle of the array to the beginning (index n // 2 - 1 to 0) using a loop.
After building the max heap, it enters another loop to extract elements one by one. In each iteration of this loop:
It swaps the first element (the root of the max heap) with the current element at index i.
Then, it calls heapify on the reduced heap (with size i) to restore the max-heap property.
This process repeats until the entire array is sorted.
Example Usage:
The example usage at the end of the code demonstrates how to use the heap_sort function to sort a test list (test_list).
After sorting, the code prints the sorted list.

<img width="409" alt="heap sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/1f3d4135-f2e4-42f0-a268-c740353309cd">


**Analysis:**
Time Complexity: Best-case - O(n log n), Average-case - O(n log n), Worst-case - O(n log n).
Heap Sort has a consistent time complexity, making it suitable for various scenarios.
It is an in-place sorting algorithm but not a stable one.

**Graphical representation of merge, selection and insertion sorting algorithms.**

These sorting algorithms were implemented on the same list of size 30.(as shown in their respective files in the repository)
<img width="453" alt="image" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/90b1e7b1-4591-49f5-9509-17d51a0024e3">

The above was implemented on google collab(Link below)
https://colab.research.google.com/drive/1Ov0Im_27O7rLwhXLDVFXGXZHZGPwp-2H


