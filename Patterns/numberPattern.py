# 1
# 22
# 333
# 4444
# 55555

# code for the above pattern

rows= int(input("enter the number of rows"))

for i in range(1,rows): #to print the number of rows
    for j in range(i):
        print(i,end="") #to print the pattern
    print()               #break after each each print to come to the next line   
