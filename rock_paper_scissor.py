# -*- coding: utf-8 -*-

# jose perez
# 8/21/19
# updated 7/13/2020
# rock paper scissors

# modules 
from random import choice

# function calls 
def rock_paper_scissors():
    print('Rock Paper Scissors')
    the_input = user_input()
    ai_choice = random_choice()
    result(the_input, ai_choice)
    rematch()

# accepts user input, validates and returns the_input    
def user_input():
    # choices for user input
    choices = ['rock', 'paper', 'scissors']
    valid = False
    # while loop for validation, use try/catch
    while valid == False:
        try:
            the_input = input('choose: rock, paper or scissors ')
            if the_input in choices:
                valid = True
        except ValueError:
            print('choose rock, paper or scissors')
    return the_input

# random choice for AI and returns the_choice
def random_choice():
    # choices for AI
    ai_choices = ['rock', 'paper', 'scissors']
    the_choice = choice(ai_choices)
    return the_choice
            
# game logic, displays user and AI choices and result            
def result(the_input, ai_choice):
    print(f'your choice is {the_input.title()} and opponent\'s choice was {ai_choice.title()}')
    if the_input == ai_choice:
        print(f'It is a tie, you chose {the_input} and your opponent also chose {ai_choice}')
    elif the_input == 'paper' and ai_choice == 'rock':
        print('You Win, Paper beats Rock!')
    elif the_input == 'rock' and ai_choice == 'scissors':
        print('You Win, Rock beats Scissors!')
    elif the_input == 'scissors' and ai_choice == 'paper':
        print('You Win, Scissors beats Paper!')
    else:
        print(f'You Lose, {ai_choice} beats {the_input}')
    
# prompt user for rematch, validates input
def rematch():
    # user choices for rematch
    options = ['yes', 'no']
    valid = False
    # while loop for validation, try/ catch used
    while valid == False:
        try:
            a_rematch = input('Wanna play again? yes or no ').lower()
            if a_rematch in options:
                valid = True
        except ValueError:
            print('enter either yes or no')
    # runs main function again if user wants rematch
    if a_rematch == 'yes':
        rock_paper_scissors()
    else:
        print('Better luck next time, Loser.')
        
        
rock_paper_scissors()

        

