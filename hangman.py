import random
import time

username = input("WHAT IS YOUR NAME?")
print ('HELLO', username.upper(), "LET'S PLAY HANGMAN")
print(" READY ")
time.sleep(0.5)
print(3)
time.sleep(0.5)
print(2)
time.sleep(0.5)
print(1)
time.sleep(0.5)
print(' START ')


words = ['APPLE', 'CHERRY', 'PEAR', 'BANANA', 'PEACH', 'KIWI' ]
word = random.choice(words)
blanks = '_'* len(word)
print(blanks)
word_update = []

wrong_guess = 6
  
while wrong_guess != 0 and blanks != word:
    guess = input("ENTER A LETTER(hint: it's a fruit): ")
    if guess.upper() in word:        
        for i in range(len(word)):
            if word[i] in guess.upper():
                blanks = blanks[:i] + word[i] + blanks[i+1:]   
                print(blanks)    
    else:
        wrong_guess -= 1
        print ('you guessed wrong, tries left', wrong_guess )
    
else:
    if blanks == word:
        print('\n ----------------------\n      YOU WON!!!!!')
    else:
        print ('\n -----------YOU GOT HANGED------------------')