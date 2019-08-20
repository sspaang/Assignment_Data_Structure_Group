'''
SELECTION SORT
'''

def selection_sort(A):
    
    for i in range(0,len(A)-1):
        n = len(A)   # round

        # initiate the first min value
        min_value = i

        for j in range(i+1,len(A)): # index for comparing
        
            n -= 1

            if A[j] < A[min_value]:
                min_value = j       # set a new min value


        #Swap the found number with the first number
        temp = A[i]
        A[i] = A[min_value]
        A[min_value] = temp

        print("Step", n, '--->', A)

data = [9,8,7,6,5,4,3,2]
print("Initiate -->", data, "\n")
print("Sorting...\n")
selection_sort(data)
for i in range(0,3):
        print(".")
print("Sorted -->", data)