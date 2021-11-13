print (" ------------------------------------------------")
print ("|                                               |")
print ("|    06WhileLoop                                |")
print ("|    Name : Vicky                               |")
print ("|    Version : 01                               |")
print ("|                                               |")
print (" ------------------------------------------------")
x = input("What is the name of this subject ")
while x != "IST":
    x += 1
    if x != "IST":
        continue
    print("Not Correct - try again")
else:
    print("Congratualations")