import random
def name():
    Name=input("Whats your name?")
    Fork()

def randout():
    out=random.randint(1,2)
    if out==1:
        villager()
    elif out == 2:
        Hobbit()


def Fork():
    print("There is a fork in the road")
    out=int(input("0:Left or 1:right"))
    if(out==1):
        print("You have gone Right")
        randout()
    else:
        print("You have gone Left")
        randout()

def villager():
    print("You have come to a Villager who wants to your food")
    out=int(input("Will you give Him food? 0:No, 1:Yes"))
    if(out==0):
        print("You kept your food")
        if random.randint(1,3)==1:
            attacked("Villager")
        else:
            Fork()
    else:
        print("You gave the villager food")
        Fork()

def RPS():
    inp=int(input("Choose 1:Rock 2:Paper 3:Scissors"))
    out=random.randint(1,3)
    if out==1 & inp==1:
        print("Its a Draw")
        RPS()
    elif out==1 & inp==2:
        print("You Won")
        Fork()
    elif out ==1 & inp==3:
        print("You Lose")
        Fork()
    elif out ==2 & inp==1:
        print("You Win")
        Fork()
    elif out==2 & inp==2:
        print("Its a Draw")
        RPS()
    elif out ==2 & inp==3:
        print("you Lose")
        Fork()
    elif out == 3 & inp==1:
        print("You Lose")
        Fork()
    elif out == 3 & inp==2:
        print("You Win")
        Fork()
    elif out == 3 & inp==3:
        print("Its A Draw")
        RPS()
    else:
        RPS()


def Hobbit():
    print("You have come to a Hobbit who wants to play Rock Paper Scisors")
    RPS()

def attacked(Attacker):
    print(f"you are being attacked by a {Attacker} will you run or fight?")
    out=int(input("0:Fight,1:Run"))
    if out==0:
        print("You are fighting")
        
    else: 
        print("You are running")
        out=random.randint(1,5)
        if out==1:
            print(f"you were not fast enough and the {Attacker} caught up to you")
            fighting(Attacker)
        else:
            Fork()

def killed(Attacker):
    print("You were killed by {Attacker}")

def fighting(Attacker):
    print(f"You are fighting a {Attacker}")
    out=random.rand(1,5)
    if out==1:
        killed()
    else:
        Fork()

name()
