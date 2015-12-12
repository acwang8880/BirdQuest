# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:12:44 2015

@author: Alex
"""

import random
#user answer
a = "no"
#modified attack from Berserk Potion
modattack = 0
global g_modattack


def linebreak():
    print ("______________________________________")
    print()

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
        player.health = 25 + player.health
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
                            #Fight

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
#Test Battle
#player [Name, Health, Attack, DodgeInt, Money]
player = Character("PLAYER 1",20,2.0,3.0,100)
pack = {"hpotion": 2, "bpotion": 1}

thief = Enemy("Thief", 10, 2, 1, random.randint(2,5))
wolf = Enemy("Wolf", 5, 3, 2, random.randint(2,5))


print(battle(thief))

'''
#In-Gaming Trading System

#shopitems = ["Gilded Sword": 10, "Silver Helm]


inv = {"asdf": 5, "another weapon": 10, "super weapon": 30}
invdesc = {"asdf": "A basic asdf weapon", "another weapon": "This is just \
another really basic weapon", "super weapon": "we call it a super weapon but it really isn't"}
print ("Welcome to the Shoppe!" + "\n" + "Here are my wares!")
print ("Or ENTER \"Q\" to exit the shop")
print
player.printdisplay()
displayshop()

itemselect = input("Enter an ITEM NAME: " + "\n")
if itemselect.lower() == "q":
    print ("Leave shop")
else:
    print (invdesc[itemselect])
    a = input("Buy item? Y/N: " + "\n")
    if player.money - inv[itemselect] < 0:
        print ("You don't have enough money!")
    else:
        while a.lower() != "y" and a.lower() != "n":
            a = input("Buy item? Y/N: " + "\n")
        else:
            if a.lower() == "y":
                print ("%s bought!" % itemselect)
                player.money -= inv[itemselect]
                print ("Remaining currency: %s" % player.money)
                del inv[itemselect]
            else:
                print ("ok")


print (inv)
'''








