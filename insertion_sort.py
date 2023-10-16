
import timeit

#complexity class is 0(n^2)
def Insertion(array):
    for a in range(1,len(array)):
        b=a
        while b>0 and array[b] <array[b-1]:
            array[b],array[b-1]=array[b-1],array[b]
            b-=1
    # print(array)

list1=[4,7,324,78,546,899,32,55,0,11,57,20,23,65,80,11,1,38,63,49,13,44,70,78,5,12,79,28,777,54]

Insertion(list1)
print(list1)

execution_time = timeit.timeit(lambda: Insertion(list1), number=1000)  # Number of repetitions
print(f"Insertion Sort Execution Time: {execution_time} seconds")