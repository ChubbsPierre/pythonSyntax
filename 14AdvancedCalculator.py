def add(number1, number2):
    return number1 + number2

def subract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return  number1 * number2

def divide(number1, number2):
    return number1 / number2


number1 = int(input("Please enter the first number: "))
mode = input("Please enter the operation")
print("You entered " + mode)
number2 = int(input("Please enter the second number: "))

if(mode == "+"):
    print(str(add(number1, number2)))
elif(mode == "-"):
    print(str(subract(number1, number2)))
elif(mode == "*"):
    print(str(multiply(number1, number2)))
elif(mode == "\\"):
    print(str(divide(number1, number2)))
else:
    print("Bad input")