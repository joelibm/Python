##age = int(input("What is your age? "))
##salary = float(input("What is your salary? "))
##for age in range (age, 65):
##    age += 1
##    salary *= 1.012
##print ("At ",age," your salary will be ",format(salary,'.0f'),".",sep='')

again = "y"
while again.lower()[0] == "y":
    minC = int(input("Min: "))
    maxC = int(input("Max: "))
    tempC = minC
    print ("C      F")
    for minC in range (minC, (maxC+1)):
        f = 9/5 * tempC + 32
        print (tempC,format(f,"9.2f"))
        tempC += 1
    again = input ("Again? y/n: ")
