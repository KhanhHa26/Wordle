import random

#get the list of words
def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

#check if the user enters a 5-letter word
def correct(wordOfUser):
    if len(wordOfUser) == 5:
        return True
    else:
        print("The word must be 5-letter long")


# comparing letters to letters
def checkWord(wordOfUser, wordChoice):
    for i in range(len(wordChoice)):
        if wordOfUser[i] == wordChoice[i]:
            output[i] = "*"
        elif (wordOfUser[i] != wordChoice[i]) and (wordOfUser[i] in wordChoice):
            output[i] = "?"
        else:
            output[i] = "_"
    return (output)


# count the number of attempts
def guessCount(wordChoice):
    count = 0
    while count < 5:
        wordOfUser = input("Guess the word: ")
        if correct(wordOfUser):
            if wordOfUser.lower() == wordChoice:
                print("You won! Hurrayyyy! It took you " + str(count + 1) + " guesses")
                break
            else:
                print(checkWord(wordOfUser, wordChoice))
                count += 1
    else:
        print("You lost due to running out of guesses :( \nThe word is: " + random_word)


# instruction
words = get_list_of_words('/usr/share/dict/words')

random_word = random.choice(words)
while len(random_word) != 5: 
    random_word = random.choice(words)

print(
    "Welcome to WORDLE! Guess the 5-letter word. \nOnly 5 attempts allowed. \n * for correct letter and order. \n ? for letter in incorrect order.\n _ for letter not in the word.\n ")

wordChoice = random_word
output = ["_"] * len(wordChoice)
print(output)

guessCount(wordChoice)



