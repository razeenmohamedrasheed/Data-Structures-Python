def linearSearch(data:list,key:int):
    for i in range(len(data)):
        if data[i] == key:
           return f'Element found at position {i + 1}'
        
    return -1







my_list = [1, 2, 3, 45, 67, 12, 98, 23, 56, 78, 34, 89, 43, 21]
key = int(input("enter the key to be search"))
result = linearSearch(my_list,key)
print(result)

