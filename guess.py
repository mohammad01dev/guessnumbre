import random
points = 0

def isUserGuess(user,rands):
    if user == rands:
        print("You Win")
        return True
    else:
        print("You Not Win")
        return False

def checkUserGuess():
    result = 0
    for i in range(0,5):
        randNums = random.randint(0,100)
        print(randNums)
        userGuess = int(input("Please Enter The Number In Between 0 and 4"))

        if isUserGuess(userGuess,randNums):
            result = result + 1

    print("Your Points %i of %i" % (result,5))

checkUserGuess()

reGame = input("Ended Game\nAre Your Regame")

if reGame == "yess" or reGame == "Yess" or reGame == "yes" or reGame == "Yes":
    checkUserGuess()
elif reGame == "1":
    int(reGame)
    checkUserGuess()
