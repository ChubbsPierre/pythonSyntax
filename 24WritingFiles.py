employee_file = open("employees", "w")
#employee_list = ""
employee_list = ["Jim - Salesman\n", "Dwight - Salesman\n", "Pam - Receptionist\n", "Michael - Manager\n", "Oscer - Acounting\n "]
for employee in employee_list:
    employee_file.write(employee)

#print(employee_file.read())

employee_file.close()