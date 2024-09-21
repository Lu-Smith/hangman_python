# Hangman in Python
import random

words = ("apple", "orange", "strawberry", "pear", 
         "banana", "pineapple", "grape", "mango", 
         "blueberry", "kiwi", "watermelon", "peach", 
         "cherry", "plum", "raspberry", "papaya")

hangman_art = {0: ("       ",
                   "       ",
                   "       "),
               1: ("   o   ",
                   "       ",
                   "       "),
               2: ("   o   ",
                   "   |   ",
                   "      "),
               3: ("   o   ",
                   "  /|   ",
                   "       "),
               4: ("   o   ",
                   "  /|\\  ",
                   "       "),
               5: ("   o   ",
                   "  /|\\  ",
                   "  /    "),
               6: ("   o   ",
                   "  /|\\  ",
                   "  / \\  ")}

def display_man(wrong_guesses):
  print("*******")
  for line in hangman_art[wrong_guesses]:
    print(line)
  print("*******")

def display_hint(hint):
  print(" ".join(hint))

def display_answer(answer):
  print(" ".join(answer))

def main():
  answer = random.choice(words)
  hint = ["_"] * len(answer)
  wrong_guesses = 0
  gussed_letter = set()
  is_running = True
  
  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    display_answer(answer)
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
      print("*******")
      print("Invalid input")
      continue
    
    if guess in gussed_letter:
      print("*******")
      print(f"{guess} is already guessed.")
      continue
    
    gussed_letter.add(guess)
    
    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          hint[i] = guess

if __name__ == "__main__":
  main()