#!/usr/bin/env python3

#Digital Gains 1.0
import random
round= 1

roll= random.randint(1, 10)

print("You rolled:",roll)

while round < 10:

    if roll == 1:
        print("10 pushups")

    elif roll == 2:
        print("25 situps")
    
    elif roll == 3:
        print("20 squats")

    elif roll == 4:
        print("25 jumping jacks")

    elif roll == 5:
        print("30 seconds high knees")

    elif roll == 6:
        print("10 burpees")

    elif roll == 8:
        print("10 8-count bodybuilders")

    elif roll == 9:
        print("20 mountain climbers")

    elif roll == 10:
        print("Take a break")
 
    if round == 10:
        print("Circuit Complete!")

   



