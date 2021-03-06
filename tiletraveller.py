"""player starts at 1,1
possible travel directions are 1,2 / north
if player enters n then travel options are 2,2 / east, 1,3 / north, 1,1 / south
if player enters an invalid direction the program should print "Not a valid direction" and lets the player choose again
player in 1,1: you can travel: (N)orth
Direction: x
player in 1,2: you can travel: (N)orth or (E)ast or (S)outh
player in 1,3: you can travel: (E)ast or (S)outh
player in 2,2: you can travel: (S)outh or (W)est
player in 2,3: you can travel: (E)ast or (W)est
player in 3,3: you can travel: (S)outh or (W)est
player in 3,2: you can travel (N)orth or (S)outh
player in 3,1: Victory!
"""
#https://github.com/pildurr/tiletraveller.git

x = 1
y = 1

while (x, y) != (3, 1):

    if (x, y) == (1, 1):
        validpos = "n"
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction in validpos:
            x = 1
            y = 2
        else:
            print("Not a valid direction!")

    elif (x, y) == (1, 2):
        validpos = ("nes")
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 1
            y = 3
        elif direction in validpos[1]:
            x = 2
            y = 2
        elif direction in validpos[2]:
            x = 1
            y = 1
        else:
            print("Not a valid direction!")

    elif (x, y) == (1, 3):
        validpos = "se"
        print("You can travel: (S)outh or (E)ast.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 1
            y = 2
        elif direction in validpos[1]:
            x = 2
            y = 3
        else:
            print("Not a valid direction!")

    elif (x, y) == (2, 1):
        validpos = "n"
        print("You can travel: (N)orth")
        direction = input("Direction: ")
        if direction in validpos:
            x = 2
            y = 2
        else:
            print("Not a valid direction!")

    elif (x, y) == (2, 2):
        validpos = "sw"
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 2
            y = 1
        elif direction in validpos[1]:
            x = 1
            y = 2
        else:
            print("Not a valid direction!")

    elif (x, y) == (2, 3):
        validpos = "ew"
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 3
            y = 3
        elif direction in validpos[1]:
            x = 1
            y = 3
        else:
            print("Not a valid direction!")

    elif (x, y) == (3, 3):
        validpos = "sw"
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 3
            y = 2
        elif direction in validpos[1]:
            x = 2
            y = 3
        else:
            print("Not a valid direction!")

    elif (x, y) == (3, 2):
        validpos = "ns"
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ")
        if direction in validpos[0]:
            x = 3
            y = 3
        elif direction in validpos[1]:
            x = 3
            y = 1
        else:
            print("Not a valid direction!")
    
if (x, y) == (3, 1):
    print("Victory!")
