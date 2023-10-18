


#finding the maximum value in an array
def find_max(array):
    #check if array is not empty
    if not array:  
        return None

    #initialize the maximum element to be the first 
    maximum_value = array[0]
    for item in array:
        #if the item is greater than the maximum value make the maximum value the item
        if item > maximum_value:
            maximum_value = item
    return maximum_value

arr1=[]#empty list
arr2=[9]#single element
arr3=[4,7,23,98,354,389,865,444,234,728]#multiple elements

sol1=find_max(arr1)
sol2=find_max(arr2)
sol3=find_max(arr3)

print(sol1)
print(sol2)
print(sol3)