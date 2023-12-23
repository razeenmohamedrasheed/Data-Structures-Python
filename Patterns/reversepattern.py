
# *****
# ****
# ***
# **
# *

# code for the reverse pattern

rows= int(input("enter the number of rows"))

for i in range(rows):               #to print the number of rows
    for j in range(rows-i):
        print("*",end="")           #to print the pattern
    print()                         #break after each each print to come to the next line   
