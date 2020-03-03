import random
def name():
    Name=input("Whats your name?")
    return Name

def Fork():
    print("There is a fork in the road")
    out=int(input("0:Left or 1:right"))
    if(out==1):
        print("You have gone Right")
    else:
        print("You have gone Left")
    return(out)

def villager():
    print("You have come to a Villager who wants to your food")
    out=int(input("Will you give Him food? 0:No, 1:Yes"))
    if(out==0):
        print("You kept your food")
    else:
        print("You gave the villager food")

def attacked(Attacker):
    print(f"you are being attacked by a {Attacker} will you run or fight?")
    out=int(input("0:Fight,1:Run"))
    if out==0:
        print("You are fighting")
        
    else: 
        print("You are running")

def killed(Attacker):
    print("You were killed by {Attacker}")

def fighting(Attacker):
    print(f"You are fighting a {Attacker}")
    out=random.rand(1,5)
Name=name()
