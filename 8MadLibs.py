colour = input("Please enter a colour")
plural_noun = input("Please enter a plural noun")
celebrity = input("Please enter a celebrity")

while True:
    if colour.isalpha() == True and plural_noun.isalpha() == True and celebrity.isalpha() == True:
        print("Roses are " + colour)
        print(plural_noun + " are blue")
        print("I love " + celebrity + " and so should you!")
        break
    else:
        print("You have not inputed a correctly typed word, fucking idiot")