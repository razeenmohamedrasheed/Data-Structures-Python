#      *
#     **
#    ***
#   ****
# *****

# code for the reverse pattern

rows= int(input("enter the number of rows"))

for i in range(1,rows+1):               
    for j in range(rows+1,i,-1):
        print(" ",end="")   
    for k in range(1,i+1):
        print("*",end="")        
    print()                        


    rows= int(input("enter the number of rows"))

for i in range(1,rows+1):               
    for j in range(rows+1,i,-1):
        print(" ",end="")   
    for k in range(1,i+1):
        print("*",end="")        
    print()                        
    rows= int(input("enter the number of rows"))

         