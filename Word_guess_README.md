Hangman Game Description
This Python script is a command-line implementation of the classic Hangman game. The objective is for the player to guess a hidden word by suggesting letters within a limited number of attempts.

Features:
Word Selection:
  The script reads a list of words from a file (words.txt).
  A random word is selected from this list as the target word for the game.
  
Game Initialization:
  The player starts with a fixed number of chances (10) to guess the word.
  The word to be guessed is initially represented by dashes (-), indicating the number of letters.
  
Gameplay Loop:

  The player guesses one letter at a time.
  Input validation ensures that the player enters a single letter and does not guess the same letter more than once.
  Correct guesses reveal the letter in its correct position(s) in the word.
  Incorrect guesses reduce the number of remaining chances.
  The game ends when the player either guesses the entire word correctly or runs out of chances.
  
Winning and Losing:

  If the player guesses the word correctly within the allotted chances, a congratulatory message is displayed.
  If the player exhausts all chances without guessing the word, a game-over message is shown along with the correct word.
