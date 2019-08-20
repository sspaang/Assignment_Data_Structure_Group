import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'information.txt')

file = open(my_file,"r")
dataMap = {}

for line in file:
    column = line.split(',')    # Split each information
    student_id = column[0]
    student_name = column[1]
    student_faculty = column[2]
    student_status = column[3]
    dataMap.update({student_id:[student_name,student_faculty,student_status]})
file.close()

def Bubble_sort(data_list):
    for i in range(len(data_list)-1, -1, -1):
        swapped = False
        # Last i element are already in place
        for j in range(i):

            #Swap if the found element is greater than the next element
            if data_list[j][1] < data_list[j+1][1]:
                data_list[j], data_list[j+1] = data_list[j+1],data_list[j]
                swapped = True
                print(data_list)
        if not swapped:
            break
            
    return data_list

def insertion_sort(data_list_1):

    for i in data_list_1:
        j = data_list_1.index(i)
        # i is not the first element
        while j > 0:
            if data_list_1[j-1][1] < data_list_1[j][1]:
                # Swap
                data_list_1[j-1],data_list_1[j] = data_list_1[j],data_list_1[j-1]
            else:
                # in order
                break
            j -= 1
        print(data_list_1)
    return data_list_1
        
def Selection_sort(data_list_2):
    for i in range(0,len(data_list_2)-1):

        # find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1,len(data_list_2)):
            if data_list_2[j][1] > data_list_2[min_index][1]:
                min_index = j
               
        # swap the found minimum element with the first element
        data_list_2[i],data_list_2[min_index] = data_list_2[min_index],data_list_2[i]
        print(data_list_2) 
    return data_list_2

Grade_map = {}
while True:
    
    search_input = input("Enter student ID: ") 
    if search_input == 'Q' or search_input == 'q' or search_input == 'quit':
        break  
    
    details = dataMap[search_input]

    status = details[2].replace('10','กำลังศึกษา')

    print(f"ชื่อ-นามสกุล: {details[0]} \nหลักสูตร: {details[1]} \nสถานะ: {status}")
    
    grade_input = float(input("Enter GPA: "))
    Grade_map.update({search_input:grade_input})
    print('Saved!\n')

print('Initiate sorting...')

Grade_list = list(Grade_map.items())
print(Grade_list)
print(' ')
print('Bubble sort')
Bubble_sort(Grade_list)
print(' ')
print('Insertion sort')
insertion_sort(Grade_list)
print(' ')
print('Selection sort')
Selection_sort(Grade_list)
print(' ')
print('Ranking')
for i in range(len(Grade_list)):
    j = i + 1
    print(f'{j} --> Student code: {Grade_list[i][0]} GPA: {Grade_list[i][1]}\n')
    j += 1
