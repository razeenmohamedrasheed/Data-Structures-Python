# 0
# 01
# 012
# 0123
# 01234

# code for the above pattern

rows= int(input("enter the number of rows"))

for i in range(rows): #to print the number of rows
    for j in range(i+1):
        print(j,end="") #to print the pattern
    print()               #break after each each print to come to the next line   
