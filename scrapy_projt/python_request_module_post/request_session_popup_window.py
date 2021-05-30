import random

player = input("Type R or P or S  : ")


RandomNumber = random.randint(1, 3)

if RandomNumber == 1:
    computer = "R"

elif  RandomNumber == 2:
    computer = "P"

elif RandomNumber == 3:
    computer = "S"

def GameOver(computer, player):
    if computer == player:
        return ("Draw ")

    elif computer == "R":
        if player == "S":
            return("computer ")
        elif player == "p":
            return("computer")

    elif  computer  == "P":
        if player =="s":
            return("player")
        elif computer =="R":
            return("computer")

    elif computer =="S":
        if player == "R":
            return("player")
        elif computer =="P":
            return("computer")



    x = GameOver()
    print(x)
