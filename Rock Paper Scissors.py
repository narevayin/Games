
# -------------------- ROCK PAPER SCISSORS -----------------------

import random

user_points = 0
pc_points = 0
while True:
    user = input('Enter Rock/Paper/Scissors: ').title()
    pc_chars = 'Rock', 'Paper', 'Scissors'
    pc = random.choice(pc_chars)
    if user_points == 2:
        print('Win user')
        break
    elif pc_points == 2:
        print ('Win PC')
        break
    else:
        if user == 'Rock' and pc == 'Scissors':
            user_points += 1
            print ("PC is", pc, "User is", user, "user win")
        elif user == 'Rock' and pc == "Paper":
            pc_points += 1
            print ("PC is", pc, "User is", user, 'pc win' )
        elif user == pc:
            print ("PC is", pc, "User is", user, 'Tie' )
        elif user == 'Paper' and pc == "Scissors":
            pc_points += 1
            print ("PC is", pc, "User is", user, 'pc win' )
        elif user == 'Paper' and pc == 'Rock':
            user_points += 1
            print ("PC is", pc, "User is", user, "user win")
        elif user == 'Scissors' and pc == 'Paper':
            user_points += 1
            print ("PC is", pc, "User is", user, "user win")
        elif user == 'Scissors' and pc == "Rock":
            pc_points += 1
            print ("PC is", pc, "User is", user, 'pc win' )
