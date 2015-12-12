# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:57:59 2015

@author: Alex
"""


class Item(object):
    def __init__(self, value):
        self.value = value


# item1 = Item(2.0)
#
#
# d = {"a" : 3, "b" : 2, "c" : 1, "d" : 0}
#
# var = raw_input("Dict key")
#
# if item1.value - d[var] < 0:
#     print "less than 0"
# elif item1.value - d[var] == 0:
#     print "equals 0"
# else:
#     print "more than 0"

import random
#user answer
a = "no"
#modified attack from Berserk Potion
modattack = 0
global g_modattack

def linebreak():
    print ("______________________________________")
    print()

def choice(question, option1, response1, option2=None,
           response2=None, option3=None, response3=None):
    userinput = input('%s' % question)
    while userinput != option1 or userinput != option2:
        userinput = input('%s' % question)
    if userinput == option1:
        print('%s' % response1)
    elif userinput == option2:
        print('%s' % response2)
    elif userinput == option3:
        print('%s' % response3)
    else:
        userinput = input('%s' % question)

class Shop(object):
    def __init__(self, location, dictinv):
        self.location = location
        self.dictinv = dictinv

    def printshop(self):
        print('Welcome to the %s shop!' % self.location)
        for i in self.dictinv:
            print ("Item: %s" % i)
            print ("Cost: %i" % self.dictinv[i])
            print ("-" * 10)

    def buy(self):
        self.printshop()
        a = input('Buy: <name>' + '\n' + 'or EXIT')
        if a.lower() in self.dictinv:
            while a.lower() != 'y' or a.lower() != 'n':
                a = input('Buy: <name>' + '\n' + 'or EXIT')
            else:
                if a.lower() == 'y':
                    a = input('Buy %s?' + '\n' + 'Y/N' % a)
                    player.money -= self.dictinv[a]
                    self.dictinv.remove(self.dictinv[a])
                    print('%s bought' % self.dictinv[a])
                else:
                    self.buy()

        elif a.lower() == 'exit':
            a = input('Exit? Y/N')
            if a.lower() == 'n':
                self.buy()
            else:
                print('Safe Travels')



class Character(object):
    def __init__(self, name, health, attack, dodgeint, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.dodge = float(dodgeint/5.0)
        self.money = money
        self.modattack = 0
    def printdisplay(self):
        print ("Name: %s" % self.name + "\n" + \
               "HP: %i" % self.health + "\n" \
                                        "Attack: %i" % self.attack + "\n" + \
               "Dodge: %.2f" % self.dodge + "\n" \
                                            "Money: %i" % self.money + "\n")
        #"======================================"
        #Enemy attacks Player - takes enemy.attack
    def gethurt(self, attack):
        if random.random() > self.dodge:
            self.health = self.health - attack
            print()
            print("-" * 10)
            print("You were hit for %.2f damage!" % attack)
        else:
            print()
            print("Enemy attack missed!")

#enemy (will also allow loot drops but only on certain battles)
class Enemy(object):
    def __init__(self, name, health, attack, dodgeint, money):
        self.name = name
        self.health = float(health)
        self.attack = attack
        self.dodge = dodgeint/5.00
        self.money = money
    def printdisplay(self):
        print ("Name: %s" % self.name + "\n" + \
               "HP: %.2f" % self.health + "\n" \
                                          "Attack: %i" % self.attack + "\n" + \
               "Dodge: %.2f" % self.dodge + "\n")
        #"======================================"
        print()
        #Player attacks Enemy - takes player.attack
    #Player attacks Enemy - takes player.attack
    def gethurt(self, attack):
        if random.random() > self.dodge:
            if player.modattack > player.attack:
                self.health = self.health - player.modattack
                print()
                print("-" * 10)
                print("You hit for %.2f damage!" % player.modattack)
                print("Enemy HP: %.2f" %thief.health)
                print("\n")
            else:
                if random.random() > self.dodge:
                    self.health = self.health - attack
                    print()
                    print("-" * 10)
                    print("You hit for %.2f damage!" % attack)
                    print("*" * 28)
                    print("Enemy HP: %.2f" %thief.health)
                    print("*" * 28 + "\n")
        else:
            print("Your attack missed!")
            print("\n")

#Consumables (come up with descriptions of potions)
def hpotion():
    if pack["hpotion"] > 0:
        player.health += 25
        if player.health > 30:
            player.health = 30
        pack["hpotion"] -= 1
    else:
        print ("You have no more Health Potions!")

def bpotion():
    if pack["bpotion"] > 0:
        player.modattack = float(player.attack * 1.25)
        pack["bpotion"] -= 1
    else:
        print ("You have no more Berserk Potions!" )
#at end of battle, modattack gets set to 0 (reset)
#monster encounters -??? how to set up??
#thief = Enemy("Thief", 10, random.randint(1,2), (random.randint(1,3)), random.randint(2,5))

def battle(enemy):
    print ("You are challenged to fight!")
    player.printdisplay()
    print ("=====VS=====")
    print ()
    enemy.printdisplay()
    while player.health > 0:
        if enemy.health > 0:
            a = input("FIGHT or use POTION:" + "\n")
            while a.lower() != "fight" and a.lower() != "potion":
                a = input("FIGHT or use POTION:" + "\n")
                #Potion

            else:
                if a.lower() == "potion":
                    print ("\n")
                    print ("^" * 28)
                    print ("YOUR BACKPACK: ")
                    print (pack)
                    print ("v" * 28)
                    print ("\n")
                    a = input("HPOTION = increase HP by 25" + "\n" + "BPOTION = temporarily increase attack by 25%" + "\n" \
                              + "or FIGHT" + "\n")
                    while a.lower() != "hpotion" and a.lower() != "bpotion" and a.lower() != "fight":
                        a = input("Select a POTION" + "\n")
                    else:
                        if a.lower() == "hpotion":
                            print ("\n" + "HPotion USED")
                            hpotion()
                            print ("*" * 28)
                            print ("Your health: %.2f" %player.health)
                            print ("*" * 28)
                        elif a.lower() == "bpotion":
                            print ("\n" + "BPotion USED")
                            bpotion()
                            print ("*" * 28)
                            print ("Attack power: %.2f" %player.modattack)
                            print ("*" * 28)
                        else:
                            enemy.gethurt(player.attack)
                            print ("*" * 28)
                            print ("Your health: %.2f" %player.health)
                            print ("Enemy health: %.2f" %enemy.health)
                            print ("*" * 28)

                else:
                    enemy.gethurt(player.attack)
                    player.gethurt(enemy.attack)
                    print ("*" * 28)
                    print ("Your health: %.2f" %player.health)
                    print ("Enemy health: %.2f" %enemy.health)
                    print ("*" * 28)
        else:
            print ("Enemy Defeated" + "\n")
            print ("Loot Gained: %.2f" %enemy.money)
            player.money += enemy.money
            print ("Total money: %.2f" %player.money)
            input("YOU WIN! Press ENTER to QUIT")
            exit()
    else:
        print ("You have died. Final stats:" + "\n")
        player.printdisplay()

# ---------Characters--------- #
#player [Name, Health, Attack, DodgeInt, Money]
player = Character("PLAYER 1",20,2.0,3.0,100)
pack = {"hpotion": 2, "bpotion": 1}

thief = Enemy("Thief", 10, 2, 1, random.randint(2,5))
wolf = Enemy("Wolf", 5, 3, 2, random.randint(2,5))
# ---------------------------- #
# ------------Shop------------ #
shop1 = Shop('Town1', {'a':1, 'b':2, 'c':3})

shop1.buy()