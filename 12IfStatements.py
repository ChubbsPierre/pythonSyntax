import null as null

gender = input("What gender are you? Male or Female: ")
male = null
if(gender == "Male"):
    male = True
    print(str(male))
elif(gender == "Female"):
    male = False
    print(str(male))
else:
    print("bad input")