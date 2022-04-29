#! /usr/bin/env python3

from random import randint 
import dice
import sys
import os
from termcolor import colored, cprint

'''  Pacific highway simulator '''

enemies = [{'name' : 'vagrant', 'health' : 10, 'damage' : '1d5'},
           {'name' : 'tweaker', 'health' : 15, 'damage' : '1d8'},
           {'name' : 'mental patient', 'health' : 20, 'damage' : '1d12'},
           {'name' : 'mugger', 'health' : 10, 'damage' : '2d12'},
           {'name' : 'stray dog', 'health' : 5, 'damage' : '1d5'}]

weapons = {'bat': {'damage':'1d12'},
           'knife': {'damage' : '2d10'},
           'gun' :{'damage' : '10d10'}
          } 

special_powers = {'uzi' : {'damage' : '4d6'}}

player_health = 9999999999

inventory = ['gun']

specials = []

exp = 0
def combat():

    global player_health, inventory, weapons, enemies, exp
    
    enemycount= len(enemies) - 1 
    enemy_ID= randint(0,enemycount)

    round = 1
    enemies_health = enemies[enemy_ID]['health']  ##enemy_health / damage
    ##enemies_damage = enemy_health - sum(dice.roll(enemies[enemy_ID]['damage'])),
    print(f"Walking down Pac Highway you encounter a {enemies[enemy_ID]['name']} Get ready to FIGHT!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Enemy Health: [" + str(enemies_health) + "]")

        print("Type: RUN, CAST[spell] or USE[weapon]") #cast needs code
        move = input().lower().split()
        enemy_damage = sum(dice.roll(enemies[enemy_ID]['damage']))
        print("\n===================================================")


        if move[0] == 'use':
            if move[1] in inventory:  #checks for weapon in inventory
                player_damage = sum(dice.roll(weapons[move[1]]['damage']))
                cprint(f"You hit the {enemies[enemy_ID]['name']} for {player_damage} damage!", 'red')
            else:  #move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory")

        if move[0] == 'cast':
            if move[1] in special_powers:
               # if move[1].lower == 'uzi':
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
                    escapego

                    print("You got killed")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The enemy got in your way blocking your escape route")

        try:
            enemies_health -= int(player_damage)
        except:
            pass
        if enemies_health <= 0:
            print(f"The {enemies[enemy_ID]['name']} lies dead. You survive!\n")
            exp =+1
            wintext1 = colored('You gained ', 'cyan')
            wintext2 = colored('exp points!', 'cyan')
            
            print(wintext1), print(exp), print(wintext2)
       
        break

        #print(f"A {enemies[enemy_ID]['name']} hits you for {enemy_damage} damage!")

        print ("=========================\n")
        round += 1
        player_health -= int(enemy_damage)

        if player_health <= 0:
            gameovertext = colored("Wasted, Game Over", 'red')
            print(gameovertext)
            #print("Wasted, Game Over")
            sys.exit()

def showInstructions():
 



    text1 = colored('Pacific Highway Simulator','red',attrs=['blink','underline','bold'])
    text2 = colored('Find an orca card and take the rail to Seattle','blue')

    print(text1)
    print(text2)
    #cprint('Pacific Highway Simulator\n' + 
        #'Escape Pac Highway to win the game\n','green',attrs=['blink']
     #   )

def playerinfo():

    areatext1 = colored("You're in "+ currentStreet + '.', 'blue')
    areatext2 = colored("Your commands are: go - get - look - use - quit", 'green')
    areatext3 = colored('**************************************************************', 'yellow')
    
    print('')
    print(areatext1)
    print(areatext2)
    print(areatext3)
    print('Inventory :', str(inventory))
    print('Specials :', str(specials))


def showStatus(): # display the player's status
 #   if 'desc' in streets[currentStreet]]:
 #       print streets[currentStreet]]['desc'])
    if 'item' in streets[currentStreet]:
        print('You see a ' + streets[currentStreet]['item'])
        print(streets[currentStreet]['item_status'] + '.')
    if 'spell' in streets[currentStreet]:
        print('You see a magic scroll. On the ribbon it says "' + streets[currentStreet]['spell'] + '".')
    promptdivision = colored('**************************************************************','yellow')
    print(promptdivision)
    #print('=================')


def spellreceive(incantation):
    print("You received a special scroll. Be careful... This power is dangerous!")
 #   incantation = input("Create the magic word to summon your spell! >")
 #   if incantation not in spells:
    print("\nYou feel like a badass as unnatural wind sweeps your hair.")
    print("The power has been successfully added to your specials. Be careful...!")

def random_encounter():
    if ((int(streets[currentStreet]['randenc'])) + 5) >= 10:
        combat()

streets = {
        'Tukwila Rail Station' : {
            'south' : '176th street',
            #'east' : 'Southcenter Mall',
            'item' : 'bat',
            'item_status' : "As you walk by a homeless encampment you see a (bat) hidden in the bushes.",
            'randenc' : '20',
            'desc' : 'This is the Tukwila Rail Station.'
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
            'item_status' : 'As you walk through the sidewalk you find a bottle of (wine) in the bus stop'
            },
        '276th street' : {
            'north' : 'Kent/Des Moines rd',
            'south' : 'Federal Way Transit Center',
            'spell' : 'uzi',
            'randenc' : '0',
            },
        'Federal Way Transit Center' : {
            'north' : '276th street',
            'randenc' : '10',
            'item' : 'orca card',
            'item_status' : 'You can find an orca card here'

            }
        }

currentStreet = 'Kent/Des Moines rd'   # player start location

os.system('clear') # start game with a fresh screen
showInstructions()     # show instructions to the player


while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('What do you want to do now?\n>') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move[1] in streets[currentStreet]:
            currentStreet = streets[currentStreet][move[1]]
            if 'desc' in streets[currentStreet]:
                print(streets[currentStreet]['desc'])
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")

    if move[0] == 'use':
        if move[1].lower() == 'wine' and 'wine' in inventory:
            print("You drink the wine. Hic! Your health has been restored!")
            print("Your wine magically refills itself! Thank You Jesus!")
            player_health = 9999999999 
            
        else:
            print('YOU CANT USE ' + (move[1].upper()) + '!') 

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

    elif move[0] == 'quit':
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            exittext1 = colored('You have exited the game', 'red', 'on_white')
            print(exittext1)
            sys.exit()
        else:
            pass              

            ## Define how a player can win
    elif currentStreet == 'Tukwila Rail Station' and 'orca' in inventory and 'wine' in inventory:
        print('You took the rail to Seatlle and manage to survive Pacific Highway... YOU WIN!')
        break
