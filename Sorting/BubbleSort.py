def bubbleSort(arr:list):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    
    return arr


arr = [2,35,6,7,0,8,1]
res = bubbleSort(arr)
print(res)