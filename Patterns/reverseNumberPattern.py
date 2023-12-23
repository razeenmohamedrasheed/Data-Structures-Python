# 012345
# 01234
# 0123
# 012
# 01
# 01

# code for the above pattern

rows= int(input("enter the number of rows"))

for i in range(rows): #to print the number of rows
    for j in range(rows - i):
        print(j,end="") #to print the pattern
    print()               #break after each each print to come to the next line   
