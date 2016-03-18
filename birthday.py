def new_user():
    name = input("Name: ")
    bday = input("Bday: ")
    
    birthday = open("birthday.txt", "w")
    birthday.write(name +'\n')
    birthday.write(bday)
    birthday.close()
try:
    birthday = open("birthday.txt", "r")
except FileNotFoundError:
    new_user()
else:
    name = birthday.readline()
    name = name.rstrip('\n')
    bday = birthday.readline()
    birthday.close()

print("Hi, ", name, ", what is the date?", sep='')
date = input()

if date == bday:
	print("Happy birthday!")


