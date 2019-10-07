from QuizTaker import QuizTaker
from QuizQuestions import QuizQuestions

question_prompts = [
    "When did WW1 start?\n(a) 1939\n(b) 1914\n(c) 1918\n\n",
    "What is the USA's northern neighbour?\n(a) Canada\n(b) Mexico\n(c) Alaska\n\n",
    "2 + 2 = ?\n(a) 2\n(b) 4\n(c) 5\n\n"
]

questions = [
    QuizQuestions(question_prompts[0], "b"),
    QuizQuestions(question_prompts[1], "a"),
    QuizQuestions(question_prompts[2], "b")
]

players = []
number_of_players = 0

def createQuiz():
    while True:
        try:
            number_of_players = int(input("Please enter the number of players: "))
            break
        except ValueError:
            print("You entered an incorrect value, please enter a number")
    counter = 1
    while counter <= number_of_players:
        name = input("Please enter Player " + str(counter) + "'s name: ")
        players.append(QuizTaker(name, 0))
        counter += 1
    return number_of_players

def runQuiz(number_of_players, players):
    for player in players:
        print("It is " + player.name + "'s turn. Please enter the correct letter")
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                player.score += 1

def declareWinner(players):
    counter = 1
    winner = players[0]
    for player in players:
        if(getattr(player, "score") > getattr(winner, "score")):
            winner = player

    print(getattr(winner, "name") + " is the winner. Their score was " + str(getattr(winner, "score")))

number_of_players = createQuiz()
runQuiz(number_of_players, players)
declareWinner(players)