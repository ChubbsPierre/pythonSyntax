def raise_to_power(base_number, exponent):
    answer = base_number
    for counter in range(exponent - 1):
        answer *= base_number
        print(answer)

input_number = input("Please enter the base number")
exponent = input("Please enter the exponent")

raise_to_power(int(input_number), int(exponent))

