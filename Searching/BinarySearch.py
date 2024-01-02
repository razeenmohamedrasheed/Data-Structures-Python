def binarySearch(data,key):
    low = 0
    high = len(data) - 1
    
    while (low<=high ):
        mid_value = (low + high)//2
        if data[mid_value] == key:
            return mid_value
        elif  key>data[mid_value]:
            low = mid_value + 1
        else:
            high = mid_value - 1
    return -1
        


dataset = [1,2,3,4,5,6,7,8,9,10,11]
key = int(input('enter the key to be found'))
result = binarySearch(dataset,key)

if result != -1:
    print(f'Key {key} found at index {result}')
else:
    print(f'Key {key} not found in the dataset')
