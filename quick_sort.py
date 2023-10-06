
def quick_sort(array):

    #check if the length of the array is bigger than 1
    if len(array) <= 1:
        return array
    
    #choose pivot point in array
    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    #is put in array incase there is more than one middle value
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    #recursion
    #call the function again to do it to the left and right 
    return quick_sort(left) + middle + quick_sort(right)

test_list = [3, 5, 8, 23, 1, 2, 1]
sorted_list = quick_sort(test_list)
print(sorted_list)
