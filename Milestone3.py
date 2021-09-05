import random

def character():
    global npcName
    global response

responses = ["Hello outsider, care to help bring us back some supplies and maybe defeat any last remaining enemies lingering?"]
npcNameChoice = ["Thalen"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

prinnt(npcName, ":]Greetings traveler, My name is", npcName, ", approach wisely...")
random.shuffle(responses)
answer = input(print("Press y to approach"))
if answer =="y":
    print(npcName, ":] ", responses[0])
else:
    print(npcName, ":] Safe Travels.")
answer = input(print("Press y to accept"))
if answer =="y":
    print(npcName, ":] Here take this, you'll need it.")
else:
    print(npcName, ":] So be it...")

responses = ["Hello Soldier, welcome to Phoenix's Landing, we are the Crusaders...you are on planet Arnoux and you can get back home through that portal right there."]
npcNameChoice = ["Senjin"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print(npcName, ":]", responses[0])

print(npcName, ":]My name is", npcName, ", by the way, would you care to help inflitrate the enemy's camp, I'll have a pretty reward for you.")
random.shuffle(responses)
answer = input(print("Press y to accept"))
if answer =="y":
    print(npcName, ":] Excellent, lets get a move on")
else:
    print(npcName, ":] Be safe soldier.")


responses = ["Look what we have here, seems like you've come back for more!"]
npcNameChoice = ["Rok: The Thrower"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print(npcName, ":]", responses[0])

print(npcName, ":] Dodge this!")
random.shuffle(responses)
answer = input(print("Press d to dodge"))
if answer =="d":
    print(":] Nice dodge! Now follow up with a counter attack!")
    print(":] Attack was successful!")
else:
    print(":] Mission Failed, please try again.")


responses = ["You hear a faint buzzing above you...you look up and a swarn of human like beings. You follow them to a hill overlooking their camp"]
npcNameChoice = ["Vallera"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print(":]", responses[0])
print(npcName, ":] You! There! Come here...My name is Vallera I have been trying to sneak in this camp for a while now, can you help me?")

answer = input(print("Press y to accept"))
if answer =="y":
    print(":] You and Vallera sneak past the enemies in the camp into the mine and steal their supplies.")
    print(npcName, ":] *whispers*: This will surely help us make some better weapons.")
else:
    print(npcName, ":] You are missing out!")


responses = ["That was some impressive work, we could use someone like you in our group, we call ourselves the Night Stalkers. Come back if you are interested"]
npcNameChoice = ["Vallera"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print("You must choose between joining the Night Stalkers or the Crusaders")

answer = input(print("Press 1 to join the Night Stalkers or press 2 to join the Crusaders."))
if answer == "1":
    print(npcName, ":]Good to see you back, looks like you made a decision. Lets get to the test.")
if answer =="y":
    print(npcName, ":] You will have to defeat these 5 enemies to join us.")
    print(npcName, "Congratulations! You did it.")
    print("You have receive a new ability; Dance of Shadows.")
else:
    print(npcName, ":] Come back when you are ready.")
if answer == "2":
    print("You leave the camp, and approach Thalen.")
    print("Thalen:] Welcome back soldier. So you want to join the Crusaders? Any one that has our common enemy is welcome")
    print("You have received a new ability: Wrath of the Holy Avenger.")
answer = input(print("Press y to continue"))


responses = ["We must enter the Shadowfang Temple to defeat the keeper. He holds the Orb of Dark Matter, with that we can reactivate the portal."]
npcNameChoice = ["Thalen"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print(npcName, ":] You must use your new abilities to help assist us defeat the Keeper of the Temple.")
random.shuffle(responses)
answer = input(print("Press y to start encounter"))
if answer =="y":
    print(npcName, ":] Forward!")
else:
    print(npcName, ":] What are we waiting for?")

print("You must dodge the incoming attacks to defeat the boss")
print("the Keeper of the Temple extends his arms to fill and prepares to spin...")

answer = input(print("Press j to jump over his spin attack."))
if answer =="j":
    print("Nice job, now counter attack!")
else:
    print("you missed, try again.")
answer = input(print("Press w to attack."))
if answer == "w":
    print("good hit, the boss has dropped to the ground.")


print("You approach the lifeless body and you loot him revealing the Orb of Dark Matter")
npcNamddeChoice = ["Thalen"]

random.shuffle(npcNameChoice)
npcName = npcNameChoice[0]

print(npcName, ":] We did it...there it is, the Orb of Dark Matter...Come, let us get to the Portal.")
print("You approach the portal with the Orb of Dark Matter in hand...")
answer = input(print("Press y to reactivate the portal"))
if answer =="y":
    print("The portal has activated, and you walk through it returning you back home!")
