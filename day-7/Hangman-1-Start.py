#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)


#-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Pick a letter you believe is in the word: \n").lower()


#-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess in chosen_word:
    print("yes")
else:
    print("no")
