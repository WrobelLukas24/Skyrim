import random

#strength
#stamia
#magic
#wisdom
#charisma

points = 250

print("Welcome, adventurer!\nTime to choose your skills!\nYou have 250 skill points to use.")
strength  = int(input("How strong are you?\n0-100\n>"))

if strength > 100 or strength < 0 or strength > points:
    print("You can't read\nGetOut")
    exit()
points = points - strength

print("Wow big stronk! strength set to " + str(strength))
print("You have " + str(points) + " skill points remaining.")

stamia = int(input("How fast are you hero?\n0-100\n>"))

if stamia > 100 or stamia < 0 or stamia > points:
    print("You can't read\nGetOut")
    exit()
points = points - stamia

print("Wow sup faz! stamia set to " + str(stamia))
print("You have " + str(points) + " skill points remaining.")

magic = int(input("How mage are you?\n0-100\n>"))

if magic > 100 or magic < 0 or magic > points:
    print("You can't read\nGetOut")
    exit()
points = points - magic

print("Wow magy! magic set to " + str(magic))
print("You have " + str(points) + " skill points remaining.")

wisdom = int(input("How smart are you hero?\n0-100\n>"))

if wisdom > 100 or wisdom < 0 or wisdom > points:
    print("You can't read\nGetOut")
    exit()
points = points - wisdom

print("Wow so smrt! wisdom set to " + str(wisdom))
print("You have " + str(points) + " skill points remaining.")

charisma = int(input("How good are you with people hero?\n0-100\n>"))

if charisma > 100 or charisma < 0 or charisma > points:
    print("You can't read\nGetOut")
    exit()
points = points - charisma

print("Wow so good! charisma set to " + str(charisma))
print("Such good skills you choose, now off you go hero to your adventure.")

print("You hero are a lonely man with your wife out in the sticks of your kingdom Snakefort.\nOne day you had to go in to your backyard forest for more wood at night.\nWhile you are out the king has ordered his footlings to capture your wife to become his.\nYou hear her screaming while getting wood\nYou run back to see what's happening but it's too late\nThey are already ridding back to the kingdom on their horeses.")
print("They stole your horse to get back and the only way to go to Snakefort is over a ridge only horses can jump\nSo you need to pass through the dark cave\nIt's the only way\nNow go through them and save your wife")

#First encounter
print("You encounter a menecing wall. What will you do hero?")
print("1. Destroy the wall")
print("2. Reason with the wall")
print("3. Mage wall")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 20:
        print("The wall shatters to pieces in a blaze of bright lights.\nAnd now go onto the fields hero.")

    else:
        print("Your whole arm shatters to pieces\n>u week boi.\nYou go back home and die alone.")
        exit()

elif choice == "2":
    roll = random.randrange(0, charisma)
    if roll > 50:
        print("The wall shatters to pieces from your inspiering words.\nGood job hero.\nNow off you go to the fields")

    else:
        print("The wall fell on top of you and you splattered like a tomato.\nYour dead.")
        exit()

elif choice == "3":
    roll = random.randrange(0, magic)
    if roll > 80:
        print("You destroyed the wall in a blaze of your own fire.\n Good job hero\nNow go onto the fields")

    else:
        print("You didn't know enough about magic.\nYou burnt yourself alive\nYour dead")
        exit()

else:
    print("You are a idot")
    exit()

#Second encounter
print("While walking through the feilds you run into a gigantic man\nBuilt like a tank\nWhat are you going to do")
print("1. Kill the giant")
print("2. Ask for directions")
print("3. Turn him into a popsicle")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 75:
        print("You easily kill the giant\nGood job hero\nNow you can go to Snakefort's border wall")

    else:
        print("The giant overtakes you and breaks all of your bones\nYour ded")
        exit()

elif choice == "2":
    roll = random.randrange(0, charisma)
    if roll > 60:
        print("The giant kindly tells you how to get to Snakefort's border wall and leaves")

    else:
        print("You tell the giant to leave me alone\nHe punches your head off and goes back to his house\nYou dead for sure")
        exit()

elif choice == "3":
    roll = random.randrange(0, magic)
    if roll > 50:
        print("A burst of cold air comes from your hands\nTurning the giant into a popsicle and you walk right by him to Snakefort's border wall")

    else:
        print("You try to freeze the giant\nBut you don't know how to use magic that well\nYou turned yourself into the popsicle\nYour dead")
        exit()

else:
    print("You are a big dumb dumb")
    exit()

#Third encounter
print("You have finally gotten to the border wall of Snakefort an hour later\nThe rage is already building up in you\nThe wall is too tall to jump over\nYou look around and their is a entrance booth with a guard that's asleep\nHow will you enter the kingdom")
print("1. Kill the guard")
print("2. Talk with the guard")
print("3. Blow the guards mind")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 45:
        print("You sneak up on the guard and get him in a sleeper hold\nHe starts to struggle and you snap his neck\nYou drag him into his booth and take his clothes")

    else:
        print("You sneak up on the guard and get him in a headlock\nHe struggles and grabs his knife and stabs you ten times\nYou bleed to death")
        exit()

elif choice == "2":
    roll = random.randrange(0, charisma)
    if roll > 70:
        print("You go up to the guard and wake him up\nHe is startled and goes for his sword\nYou calm him down and say your here to visit your brother\nHe looks at you funny but lets you in anyways\nWhen you walk into the street and look back\nHe is already back asleep")
        
    else:
        print("You go up to the guard and wake him up\nHe is startled and goes for his sword\nYou calm him down and say your here to visit your brother\nHe knows who you are and starts to open the gate to let you in\nWhen you start to walk in he stabs you in the back\nYou bleed to death")
        exit()

elif choice == "3":
    roll = random.randrange(0, wisdom)
    if roll > 80:
        print("You wake up the guard and start to talk to him about the history of Europe\nHe is so amazed that you know so much that his mind blows up in your face\nSlattering brain chuncks in your face\nYou wipe them off and grab the guards key and clothes then you open the gate and walk in to Snakefort")

    else:
        print("You wake up the guard and he is so surprised to see you that he stabs you with his knife\nYou bleed out in front of him and die")
        exit()

else:
    print("You are smol brain")
    exit()

print("You finally are in Snakefort and want to crush the Kings skull with your heel\nBut you need to find him first")










