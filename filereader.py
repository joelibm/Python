name = input("What is your name?" )
birthday = input("Bday?")
file = open("name_n_bday.txt",'w')
file.write(name + '\n' + birthday)
file.close()
file = open("name_n_bday.txt",'r')
name2 = file.readline()
print ("welcome,", name2.rstrip('\n'))
date = input("what is todays date? " )
if date == file.readline():
    print("Happy Birthday!")
else:
    print("A very merry un-birthday to you!")
file.close()
