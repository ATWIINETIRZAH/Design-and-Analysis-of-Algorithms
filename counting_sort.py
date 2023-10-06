

def counting_sort(array):
    
    #gets the maximum and minum values in the array
    max_val = max(array)
    min_val = min(array)

    range_of_elements = max_val - min_val + 1

    #creates the array starting with 0
    count_array = [0] * range_of_elements
    output_array = [0] * len(array)

    #counts how many times an element appears in the array(array)
    for num in array:
        count_array[num - min_val] += 1

    #modifies count_array to contain correct positions
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    #place elements in the right positions
    for i in range(len(array) - 1, -1, -1):
        output_array[count_array[array[i] - min_val] - 1] = array[i]
        count_array[array[i] - min_val] -= 1

    return output_array

test_list = [8, 3, 2, 8, 9, 3, 0]
sorted_list = counting_sort(test_list)
print(sorted_list)
