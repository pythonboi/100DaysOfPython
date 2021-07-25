# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."` . "-    /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')

print('''


                ,|'-._
              ,' |  | '-._
            ,' ,'|  |' ,' '-,
          ,' ,'  |  |,' ,' ,||
         ||._  ,'|  | ,' ,',||
         ||._'-._|  |' ,',',||
         ||._'-._'-.|,',',',||
         ||._'-._'-|||',',',|'
         '|._'-._'-|||',','
             '-._'-|||','
                 '-|||'         
                    
''')

print('''

    ! ! ! ! ! ! ! ! !
    ! ! ! ! ! ! ! ! !
    ! ! ! ! ! ! ! ! !
    ! ! ! ! ! ! ! ! !
    ! ! ! ! ! ! ! ! ! 

''')

print("Welcome to the Matrix")

print("The Matrix is everywhere...it is what we breadth, eat, sleep. it is in your tv and your environment watching you ")

print("Choose a pill carefully, this is your last chance:\n ")

print("You choose the blue pill, you wake-up and believe whatever you want and nothing happens")
print("You choose the red pill, Welcome to the Matrix you stay in wonderland and I will show you how deep the rabbit hole goes:\n")

pill = input("Choose your destiny: Red pill or Blue pill?\n ")

lowPill = pill.lower()

if lowPill == "red":
    print("follow me!")
    rm = input("Do you want to Enter the Room? Y for yes and N for no ")
    if rm == "Y":
        print("Jacket off and sit down")
        mirror = input("Do you want to touch the mirror? Y or N ")
        if mirror == "Y":
            print("How are you able to tell the difference between a dream and a real one")
            print("***-Going to a shock state-***")
            print("!!!--- System initializing...tank, we going to need a signal soon---!!!")
            print("Got him and he's locked him...Congratulation you're now part of the Matrix ")
            fight = input("Do you want to learn KungFu? Y for yes and N for No ").lower()
            if fight == "Y" or fight == "y":
                print("System KungFu downloaded")
                kungFuPractice = input("Do you want to practice your KungFu? Y or N ").lower()
                if kungFuPractice == "Y" or kungFuPractice == "y":
                    print("Now, you have to move to defend yourself from your enemy")
                    move = input("You need to move right, left, forward or back to defend yourself against the enemy ").lower()
                    if move == "right":
                        print("Sorry the enemy already knew and read your move, you are too slow and get defected")
                        print("Game Ove!!!")
                    elif move == "left":
                        print("Wrong move, the agent has eaten your head off! Game Over")
                    elif move == "forward":
                        print("You are too forward, now the enemy use his spare to stab you. Game Over")
                    elif move == "back":
                        print("Good Move, your enemy did not see that coming, "
                              "enemy trapped and capture... You Won!!!")
                        print(''' 
                                    ***********
                                     *********
                                      *******
                                       *****
                                        *** 
                                         *
                                            ''')
                    else:
                        print("You're too weak to move, you loose. Game Over")
                if kungFuPractice == "N" or kungFuPractice == "n":
                    print("You did not polish your kungFu knowledge enough to defect the enemy, Game Over")
            if fight == "N" or fight == "n":
                print("You are week to fight the enemy...Game Over")
        elif mirror == "N":
            print("""This is another part of Matrix where you are mortal...Anything happens here
            interrupt with the universe and the system""")
            lastChance = input("Last chance to go back to the beginning and start over? Y or N ")
            if lastChance == "Y":
                print("System reinitializing, Apak location....system reforming")
                print("%%% System Completed %%%")
                print("Jacket off and sit down")
                mirror = input("Do you want to touch the mirror? Y or N ")
                if mirror == "Y":
                    print("How are you able to tell the difference between a dream and a real one")
                    print("***-Going to a shock state-***")
                    print("!!!--- System initializing tank we going to need a signal soon---!!!")
                    print("Got him and he's locked him...Congratulation you're now in the Matrix ")
                elif mirror == "N":
                    print("Last chance fortified...Game Over")
            elif lastChance == "N":
                print("Phone ring")
                phAnswer = input("Pick the phone call? Y or N ")
                if phAnswer == "Y":
                    print("Run to the cubical, you are safe for now")
                    print("Go right or left toward to the end of the road to the office ")
                    goPath = input("Take Right or Left? ")
                    lowPath = goPath.lower()
                    if lowPath == "right" or lowPath == "r":
                        print("Sorry wrong choice you are now been capture. Game Over")
                    elif lowPath == "left" or lowPath == "l":
                        print("Good!, you are safe for now in the room, outside, there is scaffolder")
                        print("Take the Scaffholder on your right or open the window on your left")
                        outsidePath = input("Right = Scaffholder or left = Window? ")
                        lowOutsidePath = outsidePath.lower()
                        if lowOutsidePath == "right" or lowOutsidePath == 'r':
                            print("Use Scaffholder to get to the roof")
                            print("You are now able to get to the roof and Agent will come to get your")
                        elif lowOutsidePath == "left" or lowOutsidePath == "l":
                            print("Sorry you are not strong enough to make the Jump")
                            print("You will need an Agent to help you train on your jump")
                        else:
                            print("You are now been seen and capture!!! Game Over")
                else:
                    print("You are now capture by the Agent and you are part of the enemy...Game Over!!!")
    else:
        print("You are now part of the enemy and eliminated... Kill code. Game Over")

else:
    print("Game Over, Go back to your dream world")


