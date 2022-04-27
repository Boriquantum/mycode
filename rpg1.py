#! /usr/bin/env python3
from random import randint

#Hero Classes
class worker(object):
    health = 100
    strength = 7
    defence = 7
    magic = 10

class homeless(object):
    health = 80
    strength = 9
    defence = 9
    magic = 10

class toughguy(object):
    health = 150
    strength = 10
    defence = 10
    magic = 10


# Enemies

class vagrant(object):
    name = 'vagrant'
    health = 50
    strength = 5
    defence = 5
    loot = randint(0,2)

class mental_patient(object):
    name = 'mental patient'
    health = 70
    strength = 7
    defence = 7
    loot = randint(0,2)

class scammer(object):
    name = 'scammer'
    health = 90
    strength = 9
    defence = 9
    loot = randint(0,2)