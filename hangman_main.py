import random
import hangman_art
import hangman_words

def format_list(my_list):
    formatted_list = []
    for item in my_list:
        if item == '[':
            formatted_list.append('_')
        else:
            formatted_list.append(item)
    return formatted_list

word = random.choice(hangman_words.word_list)
print(word)
wordl = list(word)
guessl = []
for i in range(1, len(word)+1):
    guessl += "["

lives = 7
answer = ""

print(hangman_art.logo)

#print(wordl) #print(guessl)
print("\nYou have 7 lives to guess the word by using letters")

while lives > 0 and guessl != wordl:
    uguess = input("\nGuess a letter: ")
    if uguess in wordl:
        indices_to_replace = [i for i, elem in enumerate(wordl) if elem == uguess]
        for index in indices_to_replace:
            guessl[index] = uguess
        print(' '.join(format_list(guessl)))
    else:
        print(f"\nYou guessed {uguess}, that's not in the word. You lost a life.")
        lives -= 1
        #print("\n", guessl)
        print(' '.join(format_list(guessl)))
        print(f"\nYou have {lives} lives remaining")
        print(hangman_art.stages[lives])
        

if wordl == guessl:
    print(f"\nCongrats you guessed the word. It is {answer.join(guessl)}")
else:
    print(f"\nYou lost the game. The word was: {word}")