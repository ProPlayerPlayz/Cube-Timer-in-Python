# Cube Timer 2

import random
import time

def scrambler(x):
    moves = ["L", "L2", "L'",
            "R", "R2", "R'",
            "F", "F2", "F'",
            "B", "B2", "B'",
            "U", "U2", "U'",
            "D", "D2", "D'"]

    cnt = 0
    output = []
    prev = 'ZZ'

    if x==0:
        while cnt < 7:
            pos = random.randrange(18)
            if moves[pos][0] != prev[0]:
                output.append(moves[pos])
                prev = moves[pos]
                cnt += 1
    elif x==1:
        while cnt < 10:
            pos = random.randrange(18)
            if moves[pos][0] != prev[0]:
                output.append(moves[pos])
                prev = moves[pos]
                cnt += 1
    elif x==2:
        while cnt < 15:
            pos = random.randrange(18)
            if moves[pos][0] != prev[0]:
                output.append(moves[pos])
                prev = moves[pos]
                cnt += 1

    return output

def timer():
    input("Press [Enter] to Start")
    start=time.time()
    print("Timer has Started !")
    input("Press [Enter] to Stop")
    end=time.time()
    t=round(end-start,3)
    print("Your Time is",round(end-start,3),"Seconds!")
    return t
    
code=int(input("""Easy [Press 1]
Medium [Press 2]
Hard [Press 3]
(Difficulty cant be changed after this)>>"""))

times=[]

while True:
    y=scrambler(code)
    for i in y:
        print(i,end=" ")
    print()
    t=timer()
    times.append(t)
    if len(times)>=5 and len(times)<=12:
        avg5=times[-1]+times[-2]+times[-3]+times[-4]+times[-5]
        print("Average Time in Last 5 Solves",round(avg5,3),"[Ao5]")
    elif len(times)>=5 and len(times)>=12:
        avg5=times[-1]+times[-2]+times[-3]+times[-4]+times[-5]
        avg12=times[-1]+times[-2]+times[-3]+times[-4]+times[-5]+times[-6]+times[-7]+times[-8]+times[-9]+times[-10]+times[-11]+times[-12]
        print("Average Time in Last 5 Solves",round(avg5,3),"[Ao5]")
        print("Average Time in Last 12 Solves",round(avg12,3),"[Ao12]")
    else:
        print("Not Enough Times to Calculate Ao5 and Ao12 !")
    
    print()
    
    

        
