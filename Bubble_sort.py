
def Bubble_sort(A):
    n = len(A)
    for i in range(n):

        # Last i element are already in place
        for j in range(0, n-i-1):

            #Swap if the found element is greater than the next element
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        print(A)

        
alist = [11,1,50,65,77,25,44,30]

print("Unsorted")
print(alist)
print("Sorting...")
Bubble_sort(alist)
print("Sorted")
print(alist)