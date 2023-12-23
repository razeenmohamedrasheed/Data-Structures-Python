# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

rows = int(input("enter the number of rows"))
val = 1

for i in range(1,rows+1):
    for j in range(rows-i):
        print((i*2-1),end="")
    print()
 