import random
gamestyle = int(input ("Would you like to have a random board or read from a file? (1 = random, 2 = file) "))
while (gamestyle != 1 and gamestyle !=2):
    print("That is not a valid input")
    order = int (input ("Would you like to have a random board or read from a file? (1 = random, 2 = file) "))
if gamestyle ==1:
    numrows = int (input ("How many rows would you like the game to have? "))
    while ((numrows) < 0):
        print("That is not a valid input")
        numrows = int (input ("How many rows would you like the game to have? "))
    maxsquares = int (input ("What is the maximum number of squares per row that you want? "))
    while ((maxsquares) < 0):
        print("That is not a valid input")
        maxsquares = int (input ("What is the maximum number of squares per row that you want? "))
    game = []
    for i in range(numrows):
        squares = int(random.random() * maxsquares) + 1
        game.append(squares)
else:
    game = []
    with open("sqgame_test7.txt") as file:
        for line in file:
            if line[0] != "P":
                game.append(int(line))
    print(game)
def printgame():
    counter = 1
    for i in game:
        print ("Row " + str(counter) + ": ", end = "")
        for j in range(i):
            print ("□ ", end = "")
        print ("\n")
        counter +=1
printgame()
order = int (input ("Would you like to be Player 1 or Player 2? (enter 1 or 2) "))
while (order != 1 and order !=2):
    print("That is not a valid input")
    order = int (input ("Would you like to be Player 1 or Player 2? (enter 1 or 2) "))
def otherplayer():
    row = int (input ("Which row number would you like to choose from? "))
    while ((row) < 0) or ((row) > len(game)) or (game[row-1] == 0):
        print("That is not a valid input")
        row = int (input ("Which row number would you like to choose from? "))
    number = int (input ("How many squares do you want to remove? "))
    while ((number) < 1) or ((number) > (game[row-1])):
        print("That is not a valid input")
        number = int (input ("How many squares do you want to remove? "))
    game[row-1] = game[row-1] - number
    printgame()
def computermove():
    print("Computer has made a move")
    binary = []
    totalzero = 0
    for i in game:
        if int(i) == 0:
            totalzero +=1
        a = (str(bin(i)))
        a = a[2:len(a)]
        if a[0] == "b":
            a = a[1:len(a)]
        j = -1
        k = 0
        while abs(j)<len(a) + 1:
            if len(binary) > k:
                binary[k] = binary[k] + int(a[j])
            else:
                binary.append(int(a[j]))
            j -= 1
            k += 1
    totalodd = 0
    for x in binary:
        if x%2 !=0:
            totalodd+=1
    if totalzero == len(game) -1:
        for i in range(len(game)):
            if game[i] != 0:
                print(game[i])
                game[i] = 0
    else:
        if totalodd != 0:
            updated = False
            while not updated:
                for i in range(len(game)):
                    temp = game[i]
                    while game[i]>=0:
                        game[i] = game[i] - 1
                        if game[i] < 0:
                            game[i] = temp
                            break
                        binary = []
                        for b in game:
                            a = (str(bin(b)))
                            a = a[2:len(a)]
                            if a[0] == "b":
                                a = a[1:len(a)]
                            x = -1
                            k = 0
                            while abs(x)<len(a) + 1:
                                if len(binary) > k:
                                    binary[k] = binary[k] + int(a[x])
                                else:
                                    binary.append(int(a[x]))
                                x -= 1
                                k += 1
                        totalodd2 = 0
                        for x in binary:
                            if x%2 !=0:
                                totalodd2+=1
                        if totalodd2==0:
                            updated = True
                            break
                    if updated:
                        break
                    else:
                        game[i] = temp
                if updated:
                    break
            for j in range(len(binary)):
                if binary[j]%2 !=0:
                    for i in range(len(game)):
                        a = (str(bin(game[i])))
                        a = a[2:len(a)]
                        if a[0] == "b":
                            a = a[1:len(a)]
                        if (int(a) != 0) and (int(a) > 2**j):
                            a = a[- (j + 1)]
                        if int(a) == 1:
                            game[i] = game[i] - 2**j
                            updated = True
                            break
                if updated:
                    break
        else:
            for i in range(len(game)):
                if game[i] !=0:
                    game[i] = 0
                    break                  
    printgame()
def gameover():
    for i in game:
        if i != 0: 
            return False
    return True
if (order == 1):
    while(gameover()!=True):
        otherplayer()
        if (gameover() == True):
            print("You won!")
            break
        else:
            computermove()
            if (gameover() == True):
                print("The computer won")
                break
elif (order == 2):
    while(gameover()!=True):
        computermove()
        if (gameover() == True):
            print("The computer won")
            break
        else:
            otherplayer()
            if (gameover() == True):
                print("You won!")
                break