# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 22:25:18 2015

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

def choice(question, option1, response1, option2=None,
           response2=None, option3=None, response3=None):
    userinput = input('%s', question)
    while userinput != option1 or userinput != option2:
        userinput = input('%s', question)
    if userinput == option1:
        print('%s', response1)
    elif userinput == option2:
        print('%s', response2)
    elif userinput == option3:
        print('%s', response3)
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
        a = str(input('Buy: <name> ' + 'or EXIT: '))
        if a.lower() in self.dictinv:
            a = input('Buy %s?' + '\n' + 'Y/N' % a)
            while a.lower() != 'y' or a.lower() != 'n':
                a = input('Buy: <name> ' + 'or EXIT: ')
            else:
                if a.lower() == 'y':
                    a = input('Buy %s?' + '\n' + 'Y/N' %a)
                    player.money -= self.dictinv[a]
                    self.dictinv.remove(self.dictinv[a])
                    print('%s bought', self.dictinv[a])
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
        
        
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
while a.lower() == "n" or a.lower() == "no":

    player.name = input("Enter your name: " + "\n")
    print("Hello %s!" % player.name)
    player.health = 100.0
    print("Set your character's ATTACK and DODGE stats!")
    print("You have 5 points to spend on both (the sum of both must be equal to 5)")

    player.attack = int(input("Attack: "))
    player.dodgeint = int(input("DODGE: "))
    while player.attack + player.dodgeint != 5.0:
        print("Please enter ATTACK and DODGE again")
        player.attack = float(input("Attack: "))
        player.dodgeint = float(input("Dodge: "))
    else:
        print("______________________________________")
        print("Name: %s" % player.name)
        print("Health: %i" % player.health)
        print("Attack: %i" % player.attack)
        player.dodge = player.dodgeint/5.0
        print("dodge: %i" % player.dodgeint + " --> %2.2f" % player.dodge + " chance to \
dodge enemy attacks")
        a = input("Are you ready to continue? Y/N: ")
        if a.lower() == "y" or a.lower() == "yes":
            print("______________________________________")
            print("**NOTE: Words in CAPS are for movement throughout the story**")
            a = input("\"Enter\" to continue")
            print("______________________________________")
            break
        else:
            a = "n"

if a == "":
    print()
    print("So the story begins...")
    print("Long ago, the Cat Kingdom and the Bird Kingdom were peacefully carrying\
out their everyday lives.")
    print()
    print("However, the Bird Kingdom got too carried away with the abundance of food\
during the year. The Birds' food storage amount was the highest they had in \
centuries. Among learning of this new abundance, the Birds got carried away \
and began eating more than usual. Soon enough the Birds ran out of food to \
eat. Upon learning of this horrifying event, the Birds had to accept this \
with dismay.")
    print()
    print("The Bird King had to take immediate action, for his loyal subjects were\
in grave danger of starvation. So, he planned an evil attack on the \
Cat Kingdom. ")
    print()
    print("Over at the Cat Kingdom, the Cat King was fast asleep. The Bird King's\
ninja birds snuck inside of the Cat Kingdoms's food storage. The ninja birds\
were greeted with bountiful amounts of fish and other foods. They quickly\
snatched up as much food as possible and transported them to the awaiting Bird King.")
print("______________________________________")
a = input("\"Enter\" to continue")
print("______________________________________")
print()
print("Once morning arrived, the Cat King awoke from his slumber and went ove.r to the Royal Food Storage for breakfast. But, instead of the shelves\
stockpiled with food, the Cat King's shelves were completely bare! Trails of feathers were left behind from the heist and the Cat King immediately\
launched into action. He ordered all of his royal subjects to call every cat who was willing to venture into the Bird Kingdom.")
print()
print()
print("Meanwhile on your farm, you were watering your plants when a nobleman\
came riding through. He stopped in front of you and handed you a letter:")
print("      |YOU HAVE BEEN SUMMONED|")
print("      |   BY THE CAT KING    |")
print()
print("The Bird Kingdom has attacked our storages of food and stolen a vast amount of it!")
print("We need your help to retrieve the lost food and bring the Birds to justice.")
print()
print("If you would like to aid the King:")
print("Arrive at the castle doors tomorrow at 4:00 PM to be given information for the quest.")
print("______________________________________")

a = input("==> Well, it's 11:00am now. You can EXPLORE the town or head back to the inn to SLEEP: ")
while a.lower() != "explore" and a.lower() != "sleep":
    print("Try another response")
    linebreak()
    a = input("==> Well, it's 11:00am now. You can EXPLORE the town or head back to the inn to SLEEP: ")
else:
    if a.lower() == "sleep":
        print("You lay in your bed for a couple of hours but can't seem to fall asleep. Thoughts about the quest keep\
circling in your mind. You decide to get up and explore.")
    else:
        print("You decide to explore the town for a while. On your walk aroud town, you spot a bakery.")
        linebreak()

a = input("==> You may VISIT the bakery or you may CONTINUE on your way.")
while a.lower() != "visit" and a.lower() != "continue":
    print("Try another response")
    linebreak()
else:
    if a.lower() == "continue":
        print("You continue to walk through the town. You see that almost every food eatery hangs a sign on their door \
\"Limited Food!! Temporarily Closed!!\" But you're too hungry. Gotta find that breakfast! You quickly locate a nearby bakery\
 and dash there for some grub.")
    else:
        print("You walk into the shop. The massive shelves that once displayed heaps of freshly baked bread and pastries are\
barren and dust covered. The head baker notices you and greets you with some saddening news. \" We only have bread in stock right\
now. Sorry.\" This place once was a bustling center of commerce. Now it's an abandoned shell. You're too hungry to think any\
 further. You order the bread and eat it on the spot.")
    linebreak()

print("You exit the bakery and check the time. The town's huge clock tower reads \"2:30\". You have one and a half hours to kill.\
 You decide to walk around the town a little more until 3:40. You hurry on to the castle. You notice a congregation of mercenary cats\
, vigilante cats, and wannabe heroes. Most seem to be locals. They all look furrious. They must have signed on for the job too. They don't \
seem to want to talk...")

linebreak()

print(
    "\"My loyal subjects! May I have your attention, please!\" Every cat in the courtyard quiets down. The Cat King continues..." + "\n" +
    "As you all know, the Bird King has stolen a great amount of food from us and I have called you here to help get our food back!” This statement\
    got a scattering of cheers. “Whoever brings the Bird King to justice and brings back our food will get 1,000,000 toy mice\"!!\
    However, I must warn you. This is a dangerous quest for you will encounter many enemies along your way. If you do not wish to be in danger, leave \
    leave now!\"")
linebreak()
print("Not a bad spread, ya think?")
