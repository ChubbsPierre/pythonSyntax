import useful_tools

print(useful_tools.roll_dice(6))

for band_members in useful_tools.beatles:
    print(band_members)

while True:
    try:
        kilometres = int(input("How many metres would you like to know are in kilometres"))
        print("There are " + str(kilometres * useful_tools.metres_in_kilometer) + " metres in " + str(kilometres) + " kilometres")
        break
    except ValueError:
        print("Bad input, please enter a number")
