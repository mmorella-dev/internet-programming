# global variables
# ================

secretWord = "FOX" # the word to be guessed
guessedLetters = ['_' for letter in secretWord]

# letter guesser function
# =======================

def guessLetter(letter):
  print("Guessed:", letter)
  found = False
  win = False
  for i in range(len(secretWord)):
    if letter == secretWord[i] and guessedLetters[i] != letter:
      guessedLetters[i] = letter
      found = True
    if checkWin():
      win = True
  # print the current guessed letters
  print(*guessedLetters)
  # if found a new letter, congratulate the user
  if found:
    print("Found a letter!")
  # if no letters remaining, congratulate for winning
  if win:
    print("Congrats! You guessed the word!")

def checkWin():
  for i in range(len(secretWord)):
    if secretWord[i] != guessedLetters[i]:
      return False
  return True

# Sample input
# ============

guessLetter("E")
guessLetter("A")
guessLetter("O")
guessLetter("B")
guessLetter("F")
guessLetter("O")
guessLetter("X")
guessLetter("X")
