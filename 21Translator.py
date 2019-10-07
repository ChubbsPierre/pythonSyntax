from os.path import join


def translator(word):
    word_list = list(word)

    vowels = [
        ["a", "e", "i", "o", "u"],
        ["A", "E", "I", "O", "U"]
    ]
    counter = 0
    for letter in word_list:
        for row in vowels:
            for col in row:
                if letter == col:
                    word_list[counter] = "B"
        counter += 1
    word = ''.join(word_list) 

    return word


input_word = input("Please input a word to translate to meme language: ")
output_word = translator(input_word)

print(output_word)
