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
    print("You can't read!\nGetOut!")
    exit()
points = points - strength

print("Wow big stronk! strength set to " + str(strength))
print("You have " + str(points) + " skill points remaining.")

stamia = int(input("How fast are you hero?\n0-100\n>"))

if stamia > 100 or stamia < 0 or stamia > points:
    print("You can't read!\nGetOut!")
    exit()
points = points - stamia

print("Wow sup faz! stamia set to " + str(stamia))
print("You have " + str(points) + " skill points remaining.")

magic = int(input("How mage are you?\n0-100\n>"))

if magic > 100 or magic < 0 or magic > points:
    print("You can't read!\nGetOut!")
    exit()
points = points - magic

print("Wow magy! magic set to " + str(magic))
print("You have " + str(points) + " skill points remaining.")

wisdom = int(input("How smart are you hero?\n0-100\n>"))

if wisdom > 100 or wisdom < 0 or wisdom > points:
    print("You can't read!\nGetOut!")
    exit()
points = points - wisdom

print("Wow so smrt! wisdom set to " + str(wisdom))
print("You have " + str(points) + " skill points remaining.")

charisma = int(input("How good are you with people hero?\n0-100\n>"))

if charisma > 100 or charisma < 0 or charisma > points:
    print("You can't read!\nGetOut!")
    exit()
points = points - charisma

print("Wow so good! charisma set to " + str(charisma))
print("Such good skills you choose, now off you go hero to your adventure.")

print("You hero are a lonely man with your wife out in the sticks of your kingdom Snakefort.\nOne day you had to go in to your backyard forest for more wood at night.\nWhile you are out the king has ordered his footlings to capture your wife to become his.\nYou hear her screaming while getting wood\nYou run back to see what's happening but it's too late\nThey are already ridding back to the kingdom on their horeses.")

#First encounter
print("You encounter a menecing wall. What will you do hero?")
print("1. Punch wall")
print("2. Reason with wall")
print("3. Magic the wall")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 20:
        print("The wall shatters to pieces in a blaze of bright lights.\nAnd now you get to go to the fields.")

    else:
        print("Your fist and whole arm shatters to pieces\n>u week boi.\nYou go back home.")
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
    print("You can't do that! You LOSE!")
    exit()