array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test = [[1,2],[5,6,7],[13,14,15,16]]
# print(array[2][3])
# print(array[2])

array[2][3] =1000
print(array)  

print(id(array))
print(id(array[0]))
print(id(array[1]))
print(id(array[2]))
print(id(array[3]))
print(test[1][3])