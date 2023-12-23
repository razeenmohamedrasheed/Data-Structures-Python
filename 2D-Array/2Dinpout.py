# # test = [[j for j in x] for x in range(1,100)]
# # print(test)

# test = [j for j in input().split()]
# print(test)

# my_name="razeenmohamedrasheed"
# new_list =[x for x in my_name]
# print(new_list)

# my_name =["razeen","mohamed","rasheed"]
# twod_list = [ [j for j in x] for x in my_name]
# print(twod_list)

# sample = [int(j) for j in input().split()]
# print(sample)

# str = input().split()
# n,m = int(str[0]),int(str[1])
# li = [[int(j) for j in input().split()]for i in range(n)] 
# print(li)

# sample = [[int(j) for j in input().split()] for i in range(10)]
# print(sample)
i = int(input("enter number of rows"))
j = int(input("enter number of column"))
test2d = [ [y for y in range(j)]for x in range(i)]
print(test2d)