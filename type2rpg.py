#! /usr/bin/env python3

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player Setup ###
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.location = 'f1'
        self.game_over = False
myPlayer = player()

#### Title Screen ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholde until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholde until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()

def title_screen():
    os.system('clear')
    print('###########################')
    print('#Pacific Highway Simulator#')
    print('###########################')
    print('           -Play-          ')
    print('           -Help-          ')
    print('           -Quit-          ')
    print('           -Placeholder-   ')
    title_screen_selections()

def help_menu():
    print("Help text place holder")
    title_screen_selections()



####### MAP ###########
    """
-----
|   | a1  
-----
|   | b1
-----
|   | c1
-----
|   | d1
-----
|   | e1
-----
|   | f1 #Player starts here
-----
|   | g1
-----
|   | h1
-----
|   | i1
-----
|   | j1
-----
"""

ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False,'b1': False,'c1': False,'d1': False,'e1': False,'f1': False,'g1': False,'h1': False,'i1': False,'j1': False,}

zonemap = {
    'a1': {
        ZONENAME: 'Tukwila Light Rail Station',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'j1',
        DOWN: 'b1',
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
    },
    'c1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
    },
    'd1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'e1',
    },
    'e1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'd1',
        DOWN: 'f1',
    },
    'f1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'e1',
        DOWN: 'g1',
    },
    'g1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'f1',
        DOWN: 'h1',
    },
    'h1': {
        ZONENAME: '',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'g1',
        DOWN: 'i1',
    },
    'i1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'h1',
        DOWN: 'j1',
    },
    'j1': {
        ZONENAME: 'Federal Way Transit Center',
        DESCRIPTION: 'descrtiption',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'i1',
        DOWN: 'a1' }}

#$$$$$$$$$$$$ GAME INTERACTIVITY  $$$$$$$$$$$$$$
def print_location():
    print('\n ' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + ' #')
    priint('#' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n ' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n") + "================================="
    print("What chu' gon do?")
    action = input("> " )
    acceptable_actions = ['move', 'go', 'travel', 'walk','quit','examine','inspect','interact', 'look',]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input ("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk',]:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + '"You have moved to the ' + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if [myPlayer.location][SOLVED]:
        print("Area already explored.")
    else:
        print("You can trigger puzzle here.")
    #$$$$$$$$$$$ GAME FUNCTIONALITY $$$$$$$$$$$$$$$$$

def start_game():
        setup_game()
        return

def main_game_loop():
        while myPlayer.game_over == False:
            prompt()

def setup_game():
        os.system('clear')
#$$$$$$$$$$$$$$ Name collecting $$$$$$$$$$$$$$$$$$$$$$$$$$$$
        question1 = "Hello, what's your name?\n"
        for character in question1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_name = input("> ")
        myPlayer.name = player_name

        #$$$$$$$$$$$$$$$ JOBS $$$$$$$$$$$$$
        question2 = "What role do you want to play?\n"
        question2added = "(You can be a dealer, hobo, worker)\n"
        for character in question2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_job = input("> ")
        valid_jobs = ['dealer','hobo','worker']
        myPlayer.job = player_job

        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job 
            print("You are now a " + player_job + "!\n")
     
        while player_job.lower() not in valid_jobs:
            player_job = input("> ")
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print("You are now a " + player_job + "!\n")

        if myPlayer.job == 'dealer':   
            self.hp = 100
            self.mp = 60

        elif myPlayer.job == 'hobo':
            self.hp = 80
            self.mp = 80

        elif myPlayer.job == 'worker':
            self.hp = 90
            self.mp = 70
        


#$$$$$$$$$ Introduction  $$$$$$$$$
        question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
        for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
player_name = input("> ")
myPlayer.name = player_name

speech1 = "Welcome to Pacific Highway, punk. \n"
speech2 = "Watch your step around here! \n"
speech3 = "Dont trust anybody! \n"
speech4 = "Maybe you'll make it alive Heheheheh...."

for character in speech1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
for character in speech2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
for character in speech3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
for character in speech4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.3)




    os.system('clear')
    print("###################")
    print(" Let's start now! #")
    print("###################")



title_screen()



