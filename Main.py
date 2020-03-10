import random
def name():
    Name=input("Whats your name?")
    Fork()

def randout():
    out=random.randint(1,6)
    if out==1:
        villager()
    elif out == 2:
        Hobbit()
    elif out == 3:
        Doors()
    elif out == 4:
        dragon()
    elif out == 5:
        lava()
    elif out ==6:
        cliff()


def Fork():
    print("There is a fork in the road")
    out=int(input("0:Left or 1:right"))
    if(out==1):
        print("You have gone Right")
        randout()
    else:
        print("You have gone Left")
        randout()

def Doors():
    print("you have entered a room with lots of doors")
    inp=int(input("Which door will you choose?:1,2,3"))
    if(inp==1):
        print("There is a monster")
        attacked("Monster")
    elif(inp==2):
        print("There is an exit")
        Fork()
    else:
        villager()
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
    if (out==1 and inp==1):
        print("Its a Draw")
        RPS()
    elif (out==1 and inp==2):
        print("You Won")
        Fork()
    elif (out ==1 and inp==3):
        print("You Lose")
        Fork()
    elif (out ==2 and inp==1):
        print("You Win")
        Fork()
    elif (out==2 and inp==2):
        print("Its a Draw")
        RPS()
    elif (out ==2 and inp==3):
        print("you Lose")
        Fork()
    elif (out == 3 and inp==1):
        print("You Lose")
        Fork()
    elif (out == 3 and inp==2):
        print("You Win")
        Fork()
    elif (out == 3 and inp==3):
        print("Its A Draw")
        RPS()
    else:
        print("Error")
        #RPS()
        Fork()
        


def Hobbit():
    print("You have come to a Hobbit who wants to play Rock Paper Scisors")
    RPS()

def attacked(Attacker):
    print(f"you are being attacked by a {Attacker} will you run or fight?")
    out=int(input("0:Fight,1:Run"))
    if out==0:
        print("You are fighting")
        fighting()
        
    else: 
        print("You are running")
        out=random.randint(1,5)
        if out==1:
            print(f"you were not fast enough and the {Attacker} caught up to you")
            fighting(Attacker)
        else:
            Fork()

def killed(Attacker):
    print(f"You were killed by {Attacker}")

def fighting(Attacker):
    print(f"You are fighting a {Attacker}")
    out=random.rand(1,5)
    if out==1:
        killed()
    else:
        Fork()

def dragon():
    print("You have come upon a dragon, walk quietly so it does not see you")
    inp=random.randint(1,3)
    if inp==1:
        print("The Dragon has seen you and is attacking")
        attacked("Dragon")
    else:
        print("You have made it out alive")
        Fork()

def lava():
    print("There is a pool of lava, walk carefully so that you do not fall in")
    inp=random.randint(1,10)
    if inp==1:
        print("you have fallen in")
        killed("Lava")
    else:
        print("You made it")
        Fork()

def cliff():
    print("You have come to a cliff")
    inp=int(input("Will you climb over it:1 or go arround it:2"))
    if inp==1:
        print("You are climbing over, be careful")
        out=random.randint(1,3)
        if out==1:
            print("you made it over")
            Fork()
        else:
            print("you fell back to the ground")
            cliff()
    else:
        print("you are going arround")
        out=random.randint(1,3)
        if out ==1:
            print("you went the wrong way")
            cliff()
        else:
            print("You made it arround")
            Fork()
name()
