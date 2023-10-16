

import timeit


# O(log(n))
# Merges the left/right elements into a sorted result.
# Precondition: left/right are sorted
def merge(result, left, right):
    i1 = 0   # index into left list
    i2 = 0   # index into right list

    for i in range(0, len(result)):
        if i2 >= len(right) or (i1 < len(left) and left[i1] <= right[i2]):
            result[i] = left[i1]    # take from left
            i1 += 1
        else:
            result[i] = right[i2]   # take from right
            i2 += 1

# Rearranges the elements of a into sorted order using
# the merge sort algorithm.
def merge_sort(a):
    if len(a) >= 2:
        # split list into two halves
        left  = a[:len(a)//2]
        right = a[len(a)//2:]

        # sort the two halves
        merge_sort(left)
        merge_sort(right)

        # merge the sorted halves into a sorted whole
        merge(a, left, right)


list1=[4,7,324,78,546,899,32,55,0,11,57,20,23,65,80,11,1,38,63,49,13,44,70,78,5,12,79,28,777,54]
merge_sort(list1)
print(list1)


execution_time = timeit.timeit(lambda: merge_sort(list1), number=1000)  # Number of repetitions
print(f"Merge Sort Execution Time: {execution_time} seconds")