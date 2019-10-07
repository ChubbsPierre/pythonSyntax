employee_file = open("employees", "r")

employee_list = employee_file.readlines()
print(employee_list)

employee_file.close()

