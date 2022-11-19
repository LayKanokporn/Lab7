arr = [5,1,4,2,8]
limit = 2
while limit < len(arr)+1 :
    for i in range (len(arr)-(limit-2)):
        if arr[i] > arr[i+1]:
            Tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = Tmp
        if i==(len(arr)-limit):
            limit += 1
            break
print("BubbleSorted array is: ",arr)

for i in range(0,len(arr) -1):
    cur_min = i
    for j in range(i + 1,len(arr)):
        if arr[j] < arr[cur_min]:
            cur_min = j
    arr[i],arr[cur_min] = arr[cur_min],arr[i]

print("Selection Sort: ",arr)

for i in range(1,len(arr)):
    cur_num = arr[i]
    j = i-1
    while j >= 0 and cur_num < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
        arr[j+1] = cur_num
    
               
print("Insertion sort: ",arr)

