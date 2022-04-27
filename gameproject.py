#! /usr/bin/env python3

from random import randint 
import dice
import sys
import os

'''  Pacific highway simulator '''

enemies = [{'name' : 'vagrant', 'health' : 10, 'damage' : '1d5'},
           {'name' : 'meth-head', 'health' : 15, 'damage' : '1d8'},
           {'name' : 'mental patient', 'health' : 20, 'damage' : '1d12'},
           {'name' : 'mugger', 'health' : 10, 'damage' : '1d12 * 2'}]

weapons = {'bat': {'damage' : '1d12'},'knife' : {'damage' : '2d10'},}     
special_powers = {'uzi' : 'damage : 4d6'}
player_health = 9999999999
inventory = ['bat','knife']
specials = ['uzi']

def combat():
    enemy_ID= randint(0,4)

    global player_health, inventory, weapons, enemies
    round = 1
    enemies_health = enemies[enemy_ID]['health']  ##enemy_health / damage
    ##enemies_damage = enemy_health - sum(dice.roll(enemies[enemy_ID]['damage'])),
    print(f"Walking down Pac Highway you encouner a {enemies[enemy_ID]['name']} Get ready to FIGHT!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Enemy Health: [" + str(enemy_health) + "]")

        print("Type: RUN, CAST[spell] or USE[weapon]") #cast needs code
        move = input().lower().split()
        enemy_damage = sum(dice.roll(enemies[enemy_ID]['damage']))
        print("\n===================================================")


        if move[0] == 'use bat':
            if move[0] in inventory:  #checks for weapon in inventory
                player_damage = dice.roll(weapons[move[1]]['damage'])
                print(f"You hit the {enemies[enemy_ID]['name']} for {player_damage} damage!")
            if move not in inventory:
                print(f"There is no {move} in your inventory")

        if move[1] == 'cast':
            if move[1] in specials:
                if move[1].lower == 'uzi':
                    player_damage = sum(dice.roll(special_powers[move[1]]['damage']))
                    print(f"You conjure an Uzi and RATATATATATATA!!! hitting the {enemies[enemy_ID]['name']} for {player_damage} damage!")
                if move[1] not in specials:
                    print(f"You dont have the {move[1]} power")

        if move[0] == 'run':
            escape_chance= randint(1, 10)

            if escape_chance >= 10:
                print(f"You were to fast for them, you get away!")
                break
            if escape_chance >= 5:
                print(f"You turned around to run and got hit in the back")
                print(f"A {enemies[enemy_ID]['name']} hits you for {enemy_damage} damage!")
                player_health -= int(enemy_damage)
                if player_health >= 1:
                    print("You escaped.")
                    break
                if player_health < 1:
                    print("You got killed")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The enemy got in your way blocking your escape route")

        try:
            enemy_health -= int(player_damage)
        except:
            pass
        if enemy_health <= 0:
            print(f"The {enemies[enemy_ID]['name']} lies dead. You survive!\n")
            break

        print(f"A {enemies[enemy_ID]['name']} hits you for {enemy_damage} damage!")
        print ("=========================\n")
        round += 1
        player_health -= int(enemy_damage)

        if player_health <= 0:
            print("You got killed sucka!")
            sys.exit()

def showInstructions():
    print('''
Pacific Highway Simulator
OBJECTIVE: Survive Pac Highway
--------
Actions:
    GO[north, south, east, west, up, down]
    GET[item, spell]
    USE[item, spell]
    LOOK
    INV/INVENTORY

Type 'help' at any time! Type 'q' to quit.''')

def playerinfo():
    print('')
    print('YOU ARE IN THE ' + currentStreet + '.')
    print('=================================')
    print('Inventory :', str(inventory))
    print('Specials :', str(specials))
    print('=================================')

def showStatus(): # display the player's status
 #   if 'desc' in streets[currentStreet]]:
 #       print streets[currentStreet]]['desc'])
    if 'item' in streets[currentStreet]:
        print('You see a ' + streets[currentStreet]['item'] + streets[currentStreet]['item_status'] + '.')
    if 'spell' in streets[currentStreet]:
        print('You see a magic scroll. On the ribbon it says "' + streets[currentStreet]['spell'] + '".')
    print('=================')


def spellreceive(incantation):
    print("You received a special scroll. Be careful... This power is dangerous!")
 #   incantation = input("Create the magic word to summon your spell! >")
 #   if incantation not in spells:
    print("\n Yoy feel like a badass as unnatural wind sweeps your hair.")
    print("The power has been successfully added to your specials. Be careful...!")

def random_encounter():
    if ((int(streets[currentStreet]['randenc'])) + 5) >= 10:
        combat()

streets = {
        'Tukwila Rail Station' : {
            'south' : '176th street',
            #'east' : 'Southcenter Mall',
            'item' : 'bat',
            'item_status' : " Someone left a bat here 'Tony Armas, Slugger ",
            'randenc' : '20',
            'desc' : 'You are at Tukwila Rail Station, you see people coming and going if youre not getting on the rail you can go back south'
            },
        '176th street' : {
            'north' : 'Tukwila Rail Station',
            'randenc' : '0',
            'south' : '200th street',
            'desc' : 'Here is the local food bank. You see the staff handing out food to the homeless. There is a manhole open on the sidewalk. Where it leads you have no idea.'
            },
        '200th street' : {
            'spell' : 'uzi',
            'desc' : 'You are at Angle Lake Station. Minimart is to the left.',
            'randenc' : '0',
            'south' : 'Kent/Des Moines rd',
            #'left': 'Minimart',
            'north' : '176th street'
            },
        'Kent/Des Moines rd' : {
            #'west' : 'Downtown',
            'south' : '276th street',
            'north' : '200th street',
            'desc' : 'This is the Kent/Des Moines intersection. This is the hub for homeless people. You see a tent encampent and vagrants everywhere. North is 200th street. To the south 276th street.',
            'randenc' : '0',
            'item' : 'wine',
            'item_status' : ' You find a bottle of wine near the bus stop'
            },
        '276th street' : {
            'north' : 'Kent/Des Moines rd',
            'south' : 'Federal Way Transit Center',
            'spell' : 'uzi',
            'randenc' : '0',
            },
        'Federal Way Transit Center' : {
            'north' : '276th street',
            'randenc' : '0',
            'item' : 'McChicken'
            }
        }

currentStreet = 'Tukwila Rail Station'   # player start location

os.system('clear') # start game with a fresh screen
showInstructions()     # show instructions to the player


while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '>What do you want to do now? ':
        move = input('>What do you want to do now? ') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move in streets[currentStreet]:
            currentStreet = streets[currentStreet][move[1]]
            if 'desc' in streets[currentStreet]:
                print(streets[currentStreet]['desc'])
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")

    if move[0] == 'use wine':
        if move[1].lower() == 'wine' and 'wine' in inventory:
            print("You drink the wine. Hic! Your health has been restored!")
            print("Your wine magically refills itself! Thank You Jesus!")
            player_health = 9999999999 

    if move[0] == 'get':
        if 'item' in streets[currentStreet] and move[1] in streets[currentStreet]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            del streets[currentStreet]['item'] # deletes that item from the dictionary
        elif 'spell' in streets[currentStreet] and move[1] in streets[currentStreet]['spell']:
                spellreceive('spell')
                specials += [move[1]]  # add spell to specials
                del streets[currentStreet]['spell'] 

        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!') 


    if move[0] == 'look':
        if 'desc' in streets[currentStreet]:
            print(streets[currentStreet]['desc']) # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass              