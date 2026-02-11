import random
import sys
c = 0
d = 0
e = 0

#show inventory
def b():
    global c
    global d
    global e
    print("your ballence of shark meat is " + str(c))
    print("your ballence of bandage is " + str(d))
    print("your health is " + str(e))

#choice 1-3
def acd():
    global c
    print("you punch the shark to death, now you have extra shark meat")
    c = c + 1
    b()
def acc():
    print("you punch the shark in the nose and it waddles away")
    b()
def acb():
    print("The shark eats you. tastes like chicken!")
    print("endgame")
    sys.exit()
def aca():
    print("you die")
    sys.exit()

#choice 1
def ac():
    print("you go into the water to fight the shark")
    b = random.randint(1,6)
    print ("you rolled a " + str(b))
    if b == 1:
        aca()
    elif b == 2 or b == 3:
        acb()
    elif b == 4:
        acc()
    else:
        acd()
def ab():
    print("you lay on the bath towel. but their is a crab on the bath toewl. it bites you and you start bleeding")
    b()
    print("would you like to apply a bandage?")
def aa():
    print("you grab the umbrell but it falls over and hits you on the head")
    b()
    print("you are now in a hospital waiting room")
    print("you see [1] a nurse [2] a vending mashine and [3] a distorted bed")
    a = input("which would you like to approach: ")



#start
def a():
    print("you see an umbrella and a bath towel and a sharhgh. would you like to [1] grab the umbrell, [2] lay on the bath towel, or [3] fight the shark")
    b()
    a = input("what is your choice: ")
    if a == "1":
        aa()
    elif a == "2":
        ab()
    elif a == "3":
        ac()

print("you are on the beach and you see rolling waves and crab")
a()