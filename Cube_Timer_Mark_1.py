#CUBE TIMER
#Made by Sakthi Swaroopan
import time
import random
print("Welcome To the Cube Timer 1.0 made by ProPlayerPlayz")
time.sleep(1.5)
print("This Program will Generate Random Scrambles for your 3x3 Cube")
time.sleep(1.5)
print("It has one Feature added to it in this version.... ")
time.sleep(1.5)
print("The Difficulties!!!")
time.sleep(1.5)


#Starting code and The Lists...
print("If you Want to see the Highscores Press 0")
print("If you want the StopWatch Timer Press 1")
code=int(input("If you want a Random Scramble Press 2"))
easy=["F","R","U","B","D"]
med=["F","R","U","B","D","F'","R'","U'","B'","D'","F2","R2","U2","B2","D2"]
hard=["F","R","U","B","D","M","F'","R'","U'","B'","D'","M'","F2","R2","U2","B2","D2","M2"]
pro=["F","R","U","B","D","M","F'","R'","U'","B'","D'","M'","F2","R2","U2","B2","D2","M2","f","r","u","b","d","f'","r'","u'","b'","d'","f2","r2","u2","b2","d2"]
h_name=["","","","",""]
h_score=[99999999,99999999,99999999,99999999,99999999]
   

#The Main Infinity Loop
while True:
    #The Scrambler
    while code==2:
        print("Select Difficulty:")
        print("Easy - Press 1")
        print("Medium - Press 2")
        print("Hard - Press 3")
        dif=int(input("Pro - Press 4"))
        if dif==1: #Easy Level
            x,y="",""
            for i in range(10):
                x=random.randint(0,4)
                while x == y:
                    x=random.randint(0,4)
                y=x
                print(easy[x],end=" ")
            print()
            print("If you Want to see the Highscores Press 0")
            print("If you want the StopWatch Timer Press 1")
            code = int(input("If you want a Random Scramble Press 2"))
        elif dif==2: #Medium Level
            x,y="",""
            for i in range(15):
                x=random.randint(0,14)
                while x == y:
                    x=random.randint(0,14)
                y=x
                print(med[x],end=" ")
            print()
            print("If you Want to see the Highscores Press 0")
            print("If you want the StopWatch Timer Press 1")
            code = int(input("If you want a Random Scramble Press 2"))
        elif dif==3: #Hard Level
            x,y="",""
            for i in range(20):
                x=random.randint(0,17)
                while x == y:
                    x=random.randint(0,17)
                y=x
                print(hard[x],end=" ")
            print()
            print("If you Want to see the Highscores Press 0")
            print("If you want the StopWatch Timer Press 1")
            code = int(input("If you want a Random Scramble Press 2"))
        elif dif==4: #Pro Level
            x,y="",""
            for i in range(25):
                x=random.randint(0,32)
                while x == y:
                    x=random.randint(0,32)
                y=x
                print(pro[x],end=" ")
            print()
            print("If you Want to see the Highscores Press 0")
            print("If you want the StopWatch Timer Press 1")
            code = int(input("If you want a Random Scramble Press 2"))
        else: #Failsafe
            print("Invalid Difficulty")
            print("If you Want to see the Highscores Press 0")
            print("If you want the StopWatch Timer Press 1")
            code = int(input("If you want a Random Scramble Press 2"))
    #The StopWatch Timer
    while code==1:
        try:
            input("Press Enter to start and CTRL+C to end")
            print("Timer has Started")
            start=time.time()
            while True:
                time.sleep(1)
                print("Time Elapsed ",round(time.time()-start,0),"seconds")
        except KeyboardInterrupt:
            print("Timer has stopped")
            t=round(time.time()-start,2)
            print("Your Time is ",t,"seconds")
            for i in range(0,5):
                if t<=h_score[i]:
                    for k in range(3,-1):
                        h_score[k+1]=h_score[k]
                    h_score[i]=t
                    print("Congrats! You have secured the ",i+1," Place in the Highscore list")
                    name=input("Enter Your Name")
                    for k in range(3,-1):
                        h_name[k+1]=h_name[k]
                    h_name[i]=name
                    break
                else:
                    pass
            
        print("If you Want to see the Highscores Press 0")
        print("If you want the StopWatch Timer Press 1")
        code=int(input("If you want a Random Scramble Press 2"))

    #Highscore Displayer
    while code==0:
        for i in range(0,5):
            print(i+1,")",h_name[i],"Time =>",h_score[i])
        print("If you Want to see the Highscores Press 0")
        print("If you want the StopWatch Timer Press 1")
        code=int(input("If you want a Random Scramble Press 2"))
    #Failsafe
    while code!=1 and code!=2 and code!=0:
        print("Invalid Option Please Choose from the Options Given")
        print("If you Want to see the Highscores Press 0")
        print("If you want the StopWatch Timer Press 1")
        code=int(input("If you want a Random Scramble Press 2"))
