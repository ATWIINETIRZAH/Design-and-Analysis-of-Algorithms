

Explanation of work

Question 1(1)
**Swap function**
the swap function is created by passing three parameters in it
1. the array -which is the array/list that needs to be sorted/ the list that contains the elements to be sorted 
2. the i parameter which is the first element to be swapped 
3. the j parameter which is the  other element to be swapped
the swap function gets the two elements i and j and swaps them together each taking the other's palce

Question 1(2)
**Working principle of the insertion sorting algorithm**

Insertion sort divides the array into two parts: the sorted part and the unsorted part.
Insertion sort builds the final sorted array one item at a time. It repeatedly takes each(one) element from the unsorted part and inserts it into its correct position within the sorted part.


**Best Case, Worst Case, Average Case**

Best-case of this algorithm is : O(n) - When the input array is already or nearly sorted, and no/few elements need to be moved.
Average-case of the insertion algorithm is : O(n^2) - In the average case, elements need to be compared and moved.Insertion sort algorithm has the same worst and average case/scenario.
Worst-case of the insertion algorithm is : O(n^2). This happens when the input array is sorted in reverse order.
Best-case scenario occurs when the input array is already sorted.

Question 1(3)
The list was not sorted properly becuase the line of code nextpos-=1 was missing. The line of code is used to decrement nextpos to check the next pair of elements.

Question 1 (4)
Comparison:
- Insertion Sort vs. Bubble Sort:
  - Efficiency: In general, both insertion sort and bubble sort are not the most efficient sorting algorithms. They have an average time complexity of O(n^2).However, insertion sort performs slig.htly better
  - Use Cases: Both insertion sort and bubble sort are rarely used in practical applications due to their inefficiency. They are mainly used for educational purposes

- Insertion Sort vs. Merge Sort:
  - Efficiency: Merge sort is significantly more efficient than insertion sort. Merge sort has an average and worst-case time complexity of O(n log n), which makes it suitable for sorting large datasets efficiently while insertion has a time complexity of O(n^2)
  - Use Cases: Merge sort is commonly used when a stable, efficient sorting algorithm is needed for large datasets. It's often the algorithm of choice for external sorting, where data doesn't fit entirely in memory. Insertion sort is rarely used for large datasets 

Question 1(5)
Insertion sort can be a good choice. The reason is that insertion sort performs well when the input data is already partially sorted. In this scenario, the average-case time complexity becomes O(n) because there are fewer elements that need to be moved. 


Question 2(1)
1. **Linear Search**:
   - **Definition**: Linear search is a simple search algorithm that finds the position of a target-value within a list. It checks each element of the listsequentially until a match is found.
   - **Relationship to Searching**: Linear search is a basic searching technique used to find a specific element within an array or list. It is often used for unsorted data 

2. **Binary Search**:
   - **Definition**: Binary search is an efficient search algorithm that only works on sorted arrays. It repeatedly divides the search list/array in half, reducing the number of elements to be searched, until the target value is found or the search interval becomes empty.
   - **Relationship to Searching**: Binary search is highly efficient but requires the input data to be sorted. It is faster than linear search for large datasets.

3. **Merge Sort**:
   - **Definition**: Merge sort is an efficient, comparison-based sorting algorithm. It keeps dividing the input array into two halves, sorts them separately, and then merges the sorted halves to produce a single sorted array.
   - **Relationship to Sorting**: Merge sort is used for sorting data. It is known for its stability and guarantees both time and space complexity. It is often used as the basis for external sorting algorithms.

4. **Quick Sort**:
   - **Definition**: Quick sort is a widely used sorting algorithm that works by selecting a "pivot" element from the array and partitioning/dividing the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
   - **Relationship to Sorting**: Quick sort is another efficient sorting algorithm. It is generally faster in practice compared to merge sort and is often used for in-place sorting of arrays.

Question 2
**Pseudo code**

function find_max(array):
    maximum_value = array[0]
    for i from 1 to length of array:
        if array[i] > maximum_value:
            maximum_value = array[i]
    return maximum_value

Question 2
The time complexity  is O(n) because it iterates/loops through the array once. 
The space complexity is O(1) since it only uses a constant amount of space regardless of the input size.It does not use any extra space for different input.
