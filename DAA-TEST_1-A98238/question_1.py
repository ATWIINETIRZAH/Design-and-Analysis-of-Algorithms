

#swap function created- used to swap two elements in a list/array
def swap(arr,i,j):

    arr[i],arr[j]=arr[j],arr[i]


def insertionSort(A,n):
    for pos in range(1,n):
        nextpos=pos
        while nextpos>0 and A[nextpos]<A[nextpos-1]:
            swap (A, nextpos, nextpos-1)
            
    return A

lst=[3,65,2,89,3,4,90,22,44,63,12,6,0,15,76]
sorted=insertionSort(lst,15)
print("Sorted list:",sorted)
