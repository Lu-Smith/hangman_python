# Hangman in Python

words = ("apple", "orange", "strawberry", "pear", 
         "banana", "pineapple", "grape", "mango", 
         "blueberry", "kiwi", "watermelon", "peach", 
         "cherry", "plum", "raspberry", "papaya")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

for line in hangman_art[5]:
  print(line)

def display_man(wrong_guesses):
  pass