# Design-and-Analysis-of-Algorithms
design and analysis of algorithms, Big O complexity, and time and space complexity of algorithms 

Quick Sort:

Explanation: Quick Sort is a comparison-based sorting algorithm known for its efficiency and widely used in practice. It's based on the divide-and-conquer strategy. It selects a 'pivot' element and partitions the array into two subarrays – elements less than the pivot and elements greater than the pivot. The subarrays are then recursively sorted.

Quick Sort works by selecting a pivot, partitioning the array, and recursively sorting the subarrays. 

<img width="409" alt="quick sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/b68a93d5-d137-4cfa-b5ed-017d46cd9a0f">

Analysis: 
Quick Sort has an average-case time complexity of O(n log n) and is often faster than other sorting algorithms in practice. However, its worst-case time complexity is O(n^2) when poorly chosen pivots lead to unbalanced partitions.


Counting Sort:

Explanation: Counting Sort is a non-comparison-based sorting algorithm that works well for integers or values within a limited range. The algorithm works by counting the frequency of each element in the input array and using this information to place the elements in their correct sorted position.
It creates a "counting array" to store the count of each unique element in the input array.
Then, it uses the counting array to reconstruct the sorted output array.
It counts the occurrences of each element and uses this information to place elements in their correct sorted positions.

<img width="524" alt="counting sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/0e52961a-9b0d-43af-882d-f1906e82d39a">


Analysis: 
Counting Sort is efficient for sorting integers within a small range and has a time complexity of O(n + k), where n is the number of elements, and k is the range of input values.
Counting Sort is efficient when the range of input values (k) is not significantly larger than the number of elements (n)

Heap Sort:

Explanation: 
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. The algorithm consists of two main phases: heapification and sorting.
In the heapification phase, the input array is transformed into a binary heap, where each parent node is greater (for max-heap) or smaller (for min-heap) than its children.
Once the binary heap is built, the largest (for max-heap) or smallest (for min-heap) element (the root) is removed and placed at the end of the sorted array.
The heap property is then restored by sifting down the new root, and this process is repeated until the entire array is sorted.
It builds a max-heap (for ascending order) from the input array and repeatedly removes the maximum element (the root) and inserts it into the sorted portion of the array.

<img width="409" alt="heap sort" src="https://github.com/ATWIINETIRZAH/Design-and-Analysis-of-Algorithms/assets/117368965/1f3d4135-f2e4-42f0-a268-c740353309cd">


Analysis:
Time Complexity: Best-case - O(n log n), Average-case - O(n log n), Worst-case - O(n log n).
Heap Sort has a consistent time complexity, making it suitable for various scenarios.
It is an in-place sorting algorithm but not a stable one.
