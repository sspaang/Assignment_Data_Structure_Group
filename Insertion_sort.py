
def insertion_sort(data_list):
    for i in range(1, len(data_list)):
        
        # element to be compared -- let index 0 is sorted position, so we initiate at the next position
        current = data_list[i]

        # comparing the current element with the sorted position and swap
        while i > 0 and data_list[i-1] > current:
            data_list[i] = data_list[i-1]
            i -= 1
            data_list[i] = current
            print(data_list)
        
    return data_list

alist = [11,1,50,65,77,25,44,30]

print('Unsorted data')
print(alist)
print('Sorting...')
insertion_sort(alist)
print('Sorted')
print(alist)
