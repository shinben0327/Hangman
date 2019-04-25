"""
Created on Mar 14 2019
@author: jihwanshin

This program will let users play Hangman, the classic guessing game, on their computer!

THINGS TO DO:
showMAN()
addMAN()
showWORD()
addLETTER()
showMISS()
addMISS()
inWORD()
input letter
make list of words in words.txt
"""

import random

print("Welcome to Hangman game!")  # initial welcome message

TheMan = [  # this will contain all possible states of hangman
    """
    ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|
""",
    """
    ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|
"""
          ]
fails = 0

with open("words.txt") as words:  # brings the words in words.txt to this python module
    words_string = words.read()
    words_list = words_string.split(", ")

rand_word_index = random.randint(0, len(words_list)-1)  # randomly chooses a word to be guessed
TheWord = words_list[rand_word_index]

TheLetters = []  # makes TheWord into a list of its characters
for letter in TheWord:
    TheLetters.append(letter)

TheEmpty = []
for i in range(len(TheLetters)):
    TheEmpty.append("_")

TheWrong = []

def showman():
    print(TheMan[fails])
    print("Here is the word:")
    print(*TheEmpty)
    print()
    print("Here are your incorrect guesses:")
    print(*TheWrong)


def guess(letter=input("Guess a letter! ")):
    if letter in TheLetters:
        None  # it should say it's a correct guess and add them to TheEmpty in the correct spot
    elif letter in TheWrong:
        None  # it should tell the user that he/she is being a little stupid, and let them guess again
    else:
        None  # it should tell the user that it is an incorrect guess and add one to fails


while "_" in TheEmpty:
    showman()
    guess(letter=input("Guess a letter! "))
