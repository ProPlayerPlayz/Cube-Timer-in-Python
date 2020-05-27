# Cube Timer Mark 3
# Program by S.Sakthi Swaroopan

"""
Change Log:
-Fixed In accurate Time Issue
-Added Saving and Loading Data
-Added Profiles
-Better Interface

Note:
-All Profiles are made to be offline and can be faked easily (planned to be fixed in future updates)
-The Save Data are to be stored in the same folder as the program file so creating dedicated folder recommended
-Any Irregularities in the save file will lead to the rejection of the file
"""

# Importing Modules
import random
import time

# Main Functions


def scrambler():                                        # Produces a Scramble for the Cube
    main = ["F", "R", "L", "U", "D", "B",
            "F'", "R'", "L'", "U'", "D'", "B'",
            "F2", "R2", "L2", "U2", "D2", "B2"]
    chk = "ZZ"
    c = 14
    scramble = ""
    while c > 0:
        current = main[random.randint(0, 17)]
        if current[0] != chk[0]:
            scramble += current + " "
            chk = current
            c -= 1
    return scramble


def timer_raw():										# Timer Function
    input("Press [Enter] to Start Timer")
    start = time.time()
    input("Press [Enter] to Stop Timer")
    end = time.time()
    tim = round(end - start, 4)
    print("Your Time is", tim)
    return tim

def save(T):											# Saves Times
    name = input("Enter Name >>")
    dir1 = name + ".txt"
    try:
        f = open(dir1, "r")
        f = open(dir1, "a")
        for i in T:
            f.write(str(i)+" ")
        print("Save File Updated Successfully")
    except:
        f = open(dir1, "a")
        for i in T:
            f.write(i)
        print("Save File Created Successfully")

def load_save():										# Loads Save Files
    name = input("Enter Name >>")
    dir1 = name + ".txt"
    try:
        f = open(dir1, "r")
        raw = f.read().split(" ")
        T = []
        for i in raw:
            T.append(float(i))
        return T
    except:
        print("An Error Occured While trying to load the save file!")
        print("This Can Happen due to 2 reasons:")
        print("     - Save File Doesn't Exist")
        print("     - Save File is corrupted or in the incorrect format")
        time.sleep(2)



# __main__
print("==============================")
print("  Cube Timer [Mark 3 - v.02]  ")
print("==============================")
while True:
    print()
    print("For Entering the Timer [Enter 1]")
    code = int(input("For Closing Program [Enter 2] >>>"))
    curr = open("junk.txt","w")
    if code == 1:
        print("Entering Timer...")
        chk1 = False
        code2 = input("Do you have an existing save file? [Y/N] >>>")
        if code2.lower() in ["yes","y","yeah","yup","yea"]:
            T = load_save()
            chk1 = True
        elif code2.lower() in ["no","n","nope","nah","no way"]:
            T = []
            chk1 = True
        else:
            print("Option not found!")
        while True:
            try:
                print(scrambler())
                t = timer_raw()
                T.append(t)
                if len(T)>=5:
                    chk2=0
                    for i in T:
                        chk2+=i
                    print("Average ==>",round(chk2,3))
            except KeyboardInterrupt:
                break
        if chk1:
            code3 = input("Do you want to save your session? [Y/N] >>>")
            if code3.lower() in ["yes", "y", "yeah", "yup", "yea"]:
                save(T)
            elif code3.lower() in ["no", "n", "nope", "nah", "no way"]:
                pass
            else:
                print("Option not found!")
    elif code == 2:
        print("Closing Program...")
        break
    elif code == 4098203:
        print("Program Created by S.Sakthi Swaroopan!")
    else:
        print("Invalid Option! Please Use only the available Option Numbers")

print("==============================")
print("          Thank You           ")
print("==============================")