def maximum(number1, number2):
    if(number1 < number2):
        return number2
    else:
        return number1

number1 = int(input("Please enter the first number"))
number2 = int(input("Please enter the second number"))
print("The maximum number is " + str(maximum(number1,number2)))