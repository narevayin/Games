import time
import random
Q1 = "What is the smallest country in the world?\n A) THE NETHERLANDS \n B) VATICAN \n C) MEXICO \n D) MONACO"
Q2 = "What is the name of the largest ocean on earth?\n A) ATLANTIC \n B) INDIAN\n C) PACIFIC\n D) ARCTIC" 
Q3 = "What is Earth's largest continent?\n A) ASIA \n B) EUROPE\n C) AFRICA \n D) AMERICA"
Q4 = "How many states are in the United States?\n A) 49 \n B) 52\n C) 50 \n D) 38"
Q5 = "Which country borders 14 nations and crosses 8 time zones? \n A) ARGENTINA \n B) USA \n C) RUSSIA \n D) CHINA "
money = 10
questions = {Q1 : 'B',
    Q2 : 'C',
    Q3 : 'A',
    Q4 : 'C',
    Q5 : 'C'
}  

help_options = {
    'A' : 'THE 50/50',
    'B' : 'THE TELEPHONE',
    'C' : 'THE AUDIENCE'
}
name = input('What is your name?: ')
time.sleep(0.5)
print('\nHELLO', name.upper(), 'WELCOME TO THE GAME WHO WANTS TO BE A MILLIONARE\n\n-----------------------REMINDER!---------------------\n YOU HAVE 3 OPTIONS FOR HELP \n', help_options)
time.sleep(1)
print ('----------------GET READY---------------')
print('3')
time.sleep(0.5)
print('2')
time.sleep(0.5)
print('1')
print('----------------START-----------------')

for i in questions:
    print (i)
    answer = input('enter your answer(PRINT H FOR HELP):')
    if answer.upper() == questions[i]:
        money *= 10
        print('Your answer is correct. You won', money, '$\n-------------------------------------------\n')
        if money == 1000000:
            print ('CONGRATULATIONS! YOU ARE A MILLIONARE')
    elif answer.upper() == 'H':  #?????
        if len(help_options) == 0:
            print ('you have no help options left. \n')
            answer4 =  input('please enter the answer: ')
            if answer4.upper() ==  questions[i]:
                money *= 10            
                print ('Your answer is correct. You won', money, '$\n-----------------------------------------\n')
                if money == 1000000:
                    print ('CONGRATULATIONS! YOU ARE A MILLIONARE')
            else:
                print('\n\n\n--------------------------YOUR ANSWER WAS WRONG--------------\n--------------------------YOU LOSE ALL YOUR MONEY--------------------------')
                break
        else:
            print('\nWhich option would you like to use?\n',help_options)
            option = input('Enter the option: ')
            help_options.pop(option.upper())
            if option.upper() == 'A':
                answers = ["A", "B", "C", "D"]
                helper_answer = []
                forhelp = helper_answer.append(questions[i])
                answers.remove(questions[i]) 
                helper_answer.append(random.choice(answers))
                helper_answer.sort()
                print('The answers left are ', helper_answer)
                answer3 = input('enter your answer: ')
                if answer3.upper() == questions[i]:
                    money *= 10
                    print ('Your answer is correct. You won', money, '$\n---------------------------------------------\n')
                    if money == 1000000:
                        print ('CONGRATULATIONS! YOU ARE A MILLIONARE')
                else:
                    print('\n\n\n--------------------------YOUR ANSWER WAS WRONG--------------\n--------------------------YOU LOSE ALL YOUR MONEY--------------------------')
                    break
            elif option.upper()== 'B':
                print('We called your friend, the thinks the answer is', questions[i])
                answer1 = input('\nenter your answer: ')
                if answer1.upper() == questions[i]:
                    money *= 10
                    print ('Your answer is correct. You won', money, '$\n--------------------------------------------\n')
                    if money == 1000000:
                        print ('CONGRATULATIONS! YOU ARE A MILLIONARE')
                else:
                    print('\n\n\n--------------------------YOUR ANSWER WAS WRONG--------------\n--------------------------YOU LOSE ALL YOUR MONEY--------------------------')
                    break
            elif option.upper() == 'C':
                print ('The audience voted for answer', questions[i])
                answer2 = input('enter your answer: ')
                if answer2.upper() == questions[i]:
                    money *= 10
                    print ('Your answer is correct. You won', money, '$\n----------------------------------------\n')
                    if money == 1000000:
                        print ('CONGRATS')
                else:
                    print('\n\n\n--------------------------YOUR ANSWER WAS WRONG--------------\n--------------------------YOU LOSE ALL YOUR MONEY--------------------------')        
                    break
    else:
        print('\n\n\n--------------------------YOUR ANSWER WAS WRONG--------------\n--------------------------YOU LOSE ALL YOUR MONEY--------------------------')
        break

