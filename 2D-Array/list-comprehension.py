# li = [1,2,3,4]
# new_li = [ele * 2 for ele in li]
# print(new_li)

li = [1,2,3,4,5,6,7,8,55,67,88,9]
new_list = [ele for ele in li if ele%2==0 or ele %3==0 ]
print(new_list)

list1 = [1,2,3,45,5]
list2 = [1,2,5]
final_list = [ele for ele in list1 for ele2 in list2 if ele == ele2]
print(final_list)

names = ['razeen','mohamed','rasheed']
new_name = [[ n for n in word] for word in names]
print(new_name)   