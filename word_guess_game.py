import random

with open ("Games/words.txt",'r') as f :
    words = f.read().splitlines()
    
word = random.choice(words)

total_chances = 10
guesssed_word = "-" *len(word)
guessed_letters = []

print(" ***** WELCOME TO THE HANGMAN GAME OF GUESSING WORD , CHECK YOUR INTUITION ! BEST OF LUCK ! :) *****")

while total_chances!=0 :
    
    print("                   ------BEGIN------                  ")
    print(guesssed_word)

    letter = input("Guess the letter :").upper()
    print()
    
    
    if len(letter) != 1:
        print("Please enter single letter")
        print()
        continue
    
    if letter in guessed_letters:
        print("You have already guessed this letter")
        print()
        continue
    else:
        guessed_letters.append(letter)
    
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guesssed_word = guesssed_word[:i] + letter + guesssed_word[i +1:] #appending the letter at the correct position
        if guesssed_word == word:
            print("CONGO !! You won")
            print()
            break
    else:
        total_chances -= 1 # chances reduces
        print("Wrong guess")
        print("You have",total_chances,"chances left")
        print()
else:
    print(" GAME OVER !! ")
    print(" YOU LOSE !!")
    print(" ALL CHANCES ARE EXHAUSTED !!")
    print()
    
print(" The correct word is : " , word)


