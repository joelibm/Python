print ("Welcome to Joel's 1089!")
stepOne= input("Please enter a 3 digit number where the 1st digit and the 3rd digit differ by at least 2: ")
if stepOne.isdigit():
    if len(stepOne) == 3:
        first_stepOne = int(stepOne[0])
        second_stepOne = int(stepOne[1])
        last_stepOne = int(stepOne[2])
        if abs(first_stepOne - last_stepOne) > 1:
            stepTwo = int(str(last_stepOne) + str(second_stepOne) + str(first_stepOne))
            stepOne = int(stepOne)
            stepThree = abs(stepOne - stepTwo)
            str_stepThree = str(stepThree)
            first_stepThree = int(str_stepThree[0])
            second_stepThree = int(str_stepThree[1])
            last_stepThree = int(str_stepThree[2])
            stepFour = int(str(last_stepThree) + str(second_stepThree) + str(first_stepThree))
            stepFive = stepThree + stepFour
            print(stepOne,"<>",stepTwo)
            print(stepOne,"-",stepTwo,"=",stepThree)
            print(stepThree,"<>",stepFour)
            print(stepThree,"+",stepFour,"=",stepFive)
        else:
            print("Invalid input. First and third digits must differ by at least 2!")
    else:
        print("Invalid Input. Number must be 3 digits long!")
else:
    print("Invalid Input. Number must be a number")

