class item:
    def __init__(self,name):
        print(f"testing init{name}")
    def totalmarks(self,x,y):
        return x + y

item1= item("razeen")
item2= item("rasheed")

item1.name = "razeen"
item1.mark1 = 100
item1.mark2 =  99

item2.name = "rasheed"
item2.mark1 = 20
item2.mark2 =  99

# print(item1.totalmarks(item1.mark1,item1.mark2))
# print(item2.totalmarks(item2.mark1,item2.mark2))

print(f"the total mark of student {item1.name} is {item1.totalmarks(item1.mark1,item1.mark2)} ")
print(f"the total mark of student {item2.name} is {item2.totalmarks(item2.mark1,item2.mark2)} ")

