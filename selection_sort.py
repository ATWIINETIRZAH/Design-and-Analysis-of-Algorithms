


import timeit

# Time complexity-O(n^2)
#createing selection sort algorithms
def Selection_sort(array):
    
    #for i in the array let the minimum index be i
    for i  in range (len(array)-1):
        min_index=i

        #for a different index in the array, if the index is less than the previous minimum index
        #then let the minimum index be that index
        for index in range(i+1,len(array)):

            if array[index]<array[min_index]:
                min_index=index

        #swap the elements 
        array[i],array[min_index]=array[min_index],array[i]

    return array
   

list1=[4,7,324,78,546,899,32,55,0,11,57,20,23,65,80,11,1,38,63,49,13,44,70,78,5,12,79,28,777,54]
Selection_sort(list1)
print(list1)

execution_time=timeit.timeit(lambda: Selection_sort(list1),number=1000)
print(f"Selection Sort Execution Time: {execution_time} seconds")