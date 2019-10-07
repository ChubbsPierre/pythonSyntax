secret_word = "abdicate"

print("*****************WELCOME TO THE GUESS'O'RAMA*****************")
print("************You Must Guess the Secret Word in 3 tries************")
print("*************After 2 Guesses You Will Receive a Hint*************")
print("")

counter = 0
while counter < 3:
    if(counter == 2):
        print("Hint: A Regal Redundancy")
    player_guess = input("Please Input your Guess: ")
    if(player_guess == secret_word):
        print("********************WELL DONE YOU GUESSED THE WORD********************")
        exit()
    else:
        counter += 1
        print("That is not the correct word. You have " + str((3 - counter)) + " tries remaining.")
print("You did not guess correctly despite the easy hint. "
      "You're honestly really shit and should kill yourself, fucking swine")