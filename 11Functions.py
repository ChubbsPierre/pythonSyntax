import math

def say_hello(name):
    print("Hello " + name)

def cube_number(input):
    return input * input * input


name = input("Please input a name: ")
say_hello(name)

number = int(input("Now, input the number you want to have cubed: "))
print("The answer is " + str(cube_number(number)))