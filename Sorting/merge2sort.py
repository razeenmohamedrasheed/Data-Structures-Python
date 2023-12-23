def mergeSort(arr1,arr2,debug=False):
    i,j = 0,0
    len_1 = len(arr1)
    len_2 = len(arr2)
    new_arr = []
    while(i<len_1 and j<len_2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i = i + 1
        else:
            new_arr.append(arr2[j])
            j = j + 1
    while(i<len_1): 
        new_arr.append(arr1[i])
        i = i+1
    while(j<len_2):
        new_arr.append(arr2[j])
        j = j+1

