##################Output##################

# enter the number of roes :10
# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

num = int(input("enter the number of roes :"))

for i in range(1,num+1):
    for j in range(num-i,0,-1):
        print(j,end= " ")
    print()