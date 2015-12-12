# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:44:07 2015

@author: Alex
"""
#set up---------------------------------------------------------------------------------------------------------
import random
#user answer
a = "no"
#modified attack from Berserk Potion
modattack = 0
global g_modattack


def linebreak():
    print "______________________________________"
    print

class Character(object):
    def __init__(self, name, health, attack, dodgeint, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.dodge = float(dodgeint/5.0)
        self.money = money
        self.modattack = 0
    def printdisplay(self):
        print "Name: %s" % self.name + "\n" +\
        "HP: %i" % self.health + "\n"\
        "Attack: %i" % self.attack + "\n" +\
        "Dodge: %.2f" % self.dodge + "\n"\
        "Money: %i" % self.money + "\n"\
        #"======================================"
#Enemy attacks Player - takes enemy.attack
    def gethurt(self, attack):
        if random.random() > self.dodge:
            self.health = self.health - attack
            print
            print "You were hit for %.2f damage!" %attack
        else:
            print
            print "Enemy attack missed!"
#enemy (will also allow loot drops but only on certain battles)
class Enemy(object):
    def __init__(self, name, health, attack, dodgeint, money):
        self.name = name
        self.health = float(health)
        self.attack = attack
        self.dodge = dodgeint/5.00
        self.money = money
    def printdisplay(self):
        print "Name: %s" % self.name + "\n" +\
        "HP: %.2f" % self.health + "\n"\
        "Attack: %i" % self.attack + "\n" +\
        "Dodge: %.2f" % self.dodge + "\n"\
        #"======================================"
        print
#Player attacks Enemy - takes player.attack
    def gethurt(self, attack):
        if random.random() > self.dodge:
            if player.modattack > player.attack:
                self.health = self.health - player.modattack
                print "You hit for %.2f damage!" % player.modattack
                print "Enemy HP: %.2f" %thief.health
                print "\n"
            else:
                if random.random() > self.dodge:
                    self.health = self.health - attack
                    print "You hit for %.2f damage!" % attack
                    print "*" * 28
                    print "Enemy HP: %.2f" %thief.health
                    print "*" * 28 + "\n"
        else:
            print "Your attack missed!"
            print "\n"
#player [Name, Health, Attack, DodgeInt, Money]
player = Character("PLAYER 1",20,2.0,3.0,100)
pack = {"hpotion": 2, "bpotion": 1}

#Consumables (come up with descriptions of potions)
def hpotion():
    if pack["hpotion"] > 0:
        player.health = 25 + player.health
        if player.health > 100:
            player.health = 100
        pack["hpotion"] -= 1
    else:
        print "You have no more Health Potions!"

def bpotion():
    if pack["bpotion"] > 0:
        player.modattack = float(player.attack * 1.25)
        pack["bpotion"] -= 1
    else:
        print "You have no more Berserk Potions!"


#In-Gaming Trading System----------------------------------------------------------------------------------------------

#shopitems = ["Gilded Sword": 10, "Silver Helm]

inv = {"asdf": 5, "another weapon": 10, "super weapon": 30}
invdesc = {"asdf": "A basic asdf weapon", "another weapon": "This is just \
another really basic weapon", "super weapon": "we call it a super weapon but it really isnt"}
print "Welcome to the Shoppe!" + "\n" + "Here are my wares!"
print ("Or ENTER \"Q\" to exit the shop")
print
player.printdisplay()
print "-" * 10
for i in inv:
    print "Item: %s" % i
    print "Cost: %i" % inv[i]
    print "-" * 10

itemselect = raw_input("Enter an ITEM NAME: " + "\n")
if itemselect.lower() == "q":
    print "Leave shop"
else:
    print invdesc[itemselect]
    a = raw_input("Buy item? Y/N: " + "\n")
    if player.money - inv[itemselect] < 0:
        print "You don't have enough money!"
    else:
        while a.lower() != "y" and a.lower() != "n":
            a = raw_input("Buy item? Y/N: " + "\n")
        else:
            if a.lower() == "y":
                print "%s bought!" % itemselect
                player.money -= inv[itemselect]
                print "Remaining currency: %s" % player.money
            else:
                print "ok"