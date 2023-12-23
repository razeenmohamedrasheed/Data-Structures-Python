arr = [5,15,3,12,17,0]

for i in range(len(arr)):
    print(min_value)
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            min_value = j
            arr[i],arr[min_value] = arr[min_value],arr[i]
print(arr)