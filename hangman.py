# Hangman python game 
# © made by SomeKristi on github


# You can add words into the words.txt file or
# use your own file by changing the path of WordsDirectory
WordsDirectory="words.txt"


import time,os,random
os.system("")
hangman=("   _________    \n   | /    |     \n   |/    (X)    \n   |    /| |\   \n   |   / | | \  \n   |     / \    \n  _|_   /   \   \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |     / \    \n  _|_   /   \   \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |     /      \n  _|_   /       \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |    \n   |   / | |    \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |     | |    \n   |     | |    \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/           \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   |            \n   |            \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","                \n   |            \n   |            \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","                \n                \n                \n                \n                \n                \n  ___           \n /   \          \n/-----\         \n","                \n                \n                \n                \n                \n                \n                \n                \n                \n")

def refresh():
    print("\x1b[2J\x1b[H",end="")
def pause(nextLine:bool):
    if nextLine:
        print("")
    end=input("press enter to continue... ")

refresh()
print("Loading",end="",flush=True)
time.sleep(1)
print(".",end="",flush=True)
time.sleep(1)
print(".",end="",flush=True)
time.sleep(1)
print(".",end="",flush=True)
time.sleep(1)
refresh()
print("wasnt loading just wasting your time :P")
time.sleep(3)
refresh()

def gameSingle():
    hangman=("   _________    \n   | /    |     \n   |/    (\x1b[31mX\x1b[0m)    \n   |    /| |\   \n   |   / | | \  \n   |     / \    \n  _|_   /   \   \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |     / \    \n  _|_   /   \   \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |     /      \n  _|_   /       \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |\   \n   |   / | | \  \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |    /| |    \n   |   / | |    \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |     | |    \n   |     | |    \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/    ( )    \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   | /    |     \n   |/           \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","   _________    \n   |            \n   |            \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","                \n   |            \n   |            \n   |            \n   |            \n   |            \n  _|_           \n /   \          \n/-----\         \n","                \n                \n                \n                \n                \n                \n  ___           \n /   \          \n/-----\         \n","                \n                \n                \n                \n                \n                \n                \n                \n                \n")
    lives=11
    words=open("words.txt").read().lower().split("\n")
    word= words[random.randint(0,len(words)-1)]
    guess=[]
    WIN=False
    while True:
        GGuess=False
        match=False
        c=0
        print(hangman[lives])
        #
        if WIN==True:
            print("The word: \x1b[1m",word,"\x1b[0m\n")
            print("You have\x1b[1m",lives,"\x1b[0mlives left\n")
            print("\x1b[32m\x1b[1mYou have WON\x1b[0m")
            pause(True)
            break            
        if lives==0:
            print("The word: \x1b[1m",word,"\x1b[0m\n")
            print("You have\x1b[1m",lives,"\x1b[0mlives left\n")
            print("\x1b[31m\x1b[1mYou are dead\x1b[0m")
            pause(True)
            break
        else:
            print("The word: ",end="")
            for char in word:
                try:
                    for guessed in guess:
                        if guessed==char:
                            print(char,end="")
                            break
                    if char==" ":
                        print(" ",end="")
                    elif guessed!=char:
                        print("_",end="") 
                except:
                    if char==" ":
                        print(" ",end="")
                    else :
                        print("_",end="")
            print("\n")
            #
            print("You have",lives,"lives left\n")
            g=input("guess: ").lower()

            if len(g)>1:
                if g==word:
                    WIN=True
                else:
                    lives-=1
            elif len(g)<2:
                for gu in guess:
                    if match==True:
                        break
                    elif g==gu:
                        match=True
                if match == False:
                    guess.append(g)

                for char in word:
                    if GGuess==True:
                        break
                    elif char==guess[len(guess)-1] or g==char:
                        GGuess=True
                if GGuess!=True:
                    lives-=1

                for char in word:
                    for gues in guess:
                        if WIN==True:
                            break
                        elif char==gues:
                            c+=1
                for char in word:
                    if char == " ":
                        c+=1
                if c==len(word):
                    WIN=True
            refresh()


#def gameoption():
#    while True:
#            refresh()
#            print("[1]singleplayer")
#            print("[2]multiplayer")
#            print("[3]exit")
#
#            gaction=input("Chose: ")
#            refresh()
#
#            if gaction=="1":
#                gameSingle()
#            elif gaction=="2":
#                print("WIP")
#                pause(True)
#            elif gaction=="3":
#                break
#            else:
#                print("\x1b[31minvalid input\x1b[0m")
#                time.sleep(.25)


def credits():
    print("made by \x1b[32m\x1b[1mSomeKristi\x1b[0m on github")

def about():
    print("creation from a chalange made by a friend :D")

def scoreboard():
    print("nothing here ... yet")


#menu
while True:
    refresh()
    print("[1]play")
    print("[2]credits")
    print("[3]about")
    #print("[4]scoreboard")
    print("[4]exit")
    
    action=input("Chose: ")
    refresh()

    if action=="1":
        gameSingle()
        #gameoption()

    elif action=="2":
        credits()
        pause(True)

    elif action=="3":
        about()
        pause(True)

    #elif action=="4":
    #    scoreboard()
    #    pause(True)

    elif action=="4":
        print("\x1b[1mBye\x1b[0m")
        time.sleep(1)
        break

    else:
        print("\x1b[31minvalid input\x1b[0m")
        time.sleep(.25)