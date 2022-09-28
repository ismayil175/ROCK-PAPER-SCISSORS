#Computer gives a number and we try to guess between given numbers
# import random
# from re import X

# def guess(x): 
#     random_number = random.randint(1, x)  
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}:'))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')
#     print(f'Yay,You`ve guessed the number {random_number}.')
#guess(5)

#We think a number and the computer try to our guess number

# import random

# def computer_guess(x):
#     low = 1
#     high = x 
#     feedback = ''
#     while feedback != 'c':
#         guess = random.randint(low,high)
#         feedback = input(f'Is {guess} too low (L) or too High(H) or Correct (C)'.lower())
#         if feedback == 'h':
#             high = guess -1 
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'The computer guessed your the number {guess}')

# computer_guess(5)






