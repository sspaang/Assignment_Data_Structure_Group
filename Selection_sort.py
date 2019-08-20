
def Selection_sort(A):
    for i in range(0,len(A)-1):

        # find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1,len(A)):
            if A[j] < A[min_index]:
                min_index = j
        
        # swap the found minimum element with the first element
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp

        print(A) 

alist = [11,1,50,65,77,25,44,30]

print("Unsorted")
print(alist)
print("Sorting...")
Selection_sort(alist)
print("Sorted")
print(alist)

'''
https://www.pythoncentral.io/selection-sort-implementation-guide/
'''