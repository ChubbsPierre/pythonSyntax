while True:
    try:
        #value = 10/0
        number = int(input("Please enter a number: "))
        print(number)
        break
    except ValueError as err:
        print("Invalid input " + str(err))
    except ZeroDivisionError:
        print("Divded by 0")