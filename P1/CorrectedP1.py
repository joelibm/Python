#1 Display Welcome Message
print ("Welcome to the 1089 trick!")
#2 Display About Message
about_message_1 = "This trick's sure to amaze your friends."
about_message_2 = """It's believed that the "1089 trick" was a favorite of Albert Einstein."""
about_message_3 = "To begin, enter a number with 3 digits, where the 1st digit and the3rd digit differ by at least 2."
print (about_message_1,"\n",about_message_2,"\n",about_message_3,sep='')
#3 Input a number from the user
stepOne= input("Enter a number: ")
#4 Check that the number has 3 digits, and do not continue if not
if stepOne.isdigit():
    if len(stepOne) == 3:
#5 Check that the 1st digit and the 3rd digit differ by at least 2, and do not continue ifnot
        first_stepOne = int(stepOne[0])
        last_stepOne = int(stepOne[2])
        if abs(first_stepOne - last_stepOne) > 1:
#6 Calculate the reverse of the input
            def reverse_int(n):
                return int(str(n)[::-1])#Extended slice
            stepTwo = reverse_int(stepOne)
            stepOne = int(stepOne)
#7 Calculate the difference of the input and its reverse
            stepThree = abs(stepOne - stepTwo)
#8 Calculate the reverse of the difference
            stepFour = reverse_int(stepThree)
#9 Calculate the sum of the difference and its reverse
            stepFive = stepThree + stepFour
#10 Output the results of the calculations
            print("The reverse of ",stepOne," is ",stepTwo,".",sep='')
            print("The difference of ",stepOne," and ",stepTwo," is ",stepThree,".",sep='')
            print("The reverse of ",stepThree," is ",stepFour,".",sep='')
            print("The sum of ",stepThree," and ",stepFour," is ",stepFive,"!",sep='')
        else:
            print("The 1st digit and the 3rd digit must differ by at least 2")
    else:
        print("You must enter a 3-digit number.")
else:
    print("Invalid Number. Number must be an integer.")

