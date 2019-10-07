while True:
    number1 = input("Please enter the 1st number: ")
    if number1.isnumeric() == True:
        number2 = input("Please enter the 2nd number: ")
        if number2.isnumeric() == True:
            answer = float(number1) + float(number2)
            print("The answer is " + str(answer))
            break
        else:
            print("You did not enter a number, please try again")
    else:
        print("You did not enter a number, please try again")
