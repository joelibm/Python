#1 Display Welcome Message
print ("Welcome to the 1089 trick!")
#2 Display About Message
about_message_1 = "This trick's sure to amaze your friends."
about_message_2 = """It's believed that the "1089 trick" was a favorite of Albert Einstein."""
about_message_3 = "To begin, enter a number with 3 digits, where the 1st digit and the 3rd digit differ by at least 2."
print (about_message_1,"\n",about_message_2,"\n",about_message_3,sep='')

again = "y"
while again.lower()[0] == "y":
#3 Input a number from the user
    number = input("Enter a number: ")
    goodToGo = False
    while not goodToGo:
        if not (number.isdigit() and len(number) == 3):
            while not (number.isdigit() and len(number) == 3):
                if not number.isdigit():
                    print("Invalid Input. Number must be an integer.")
                    number = input("Enter a number: ")
#4 Check that the number has 3 digits, and do not continue if not
                elif not len(str(number)) == 3:
                    print("You must enter a 3-digit number.")
                    number = input("Enter a number: ")
#5 Check that the 1st digit and the 3rd digit differ by at least 2, and do not continue ifnot
        numberInt = int(number)
        firstNumber = numberInt // 100
        lastTwo = numberInt % 100
        secondNumber = lastTwo // 10
        thirdNumber = lastTwo % 10
        if not abs(firstNumber - thirdNumber) > 1:
            print("The 1st digit and the 3rd digit must differ by at least 2")
            number = input("Enter a number: ")
        else:
            goodToGo = (number.isdigit() and len(number) == 3 and abs(firstNumber - thirdNumber) > 1)
    else:
#6 Calculate the reverse of the input
        reversed = int(str(thirdNumber) + str(secondNumber) + str(firstNumber))
#7 Calculate the difference of the input and its reverse
        difference = abs(numberInt - reversed)
#8 Calculate the reverse of the difference
        firstDifference = difference // 100
        lastTwo = difference % 100
        secondDifference = lastTwo // 10
        thirdDifference = lastTwo % 10
        reversed_difference = int(str(thirdDifference) + str(secondDifference) + str(firstDifference))
#9 Calculate the sum of the difference and its reverse
        sum = reversed_difference + difference
#10 Output the results of the calculations
        print("The reverse of ",number," is ",reversed,".",sep='')
        print("The difference of ",number," and ",reversed," is ",difference,".",sep='')
        print("The reverse of ",difference," is ",reversed_difference,".",sep='')
        print("The sum of ",difference," and ",reversed_difference," is ",sum,"!",sep='')
    again = input ("Again? y/n: ")

