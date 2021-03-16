import random

charms = input("Charms? Type 1 for yes or 0 for no: ")
ch = False
if charms == "1":
    ch = True

hexCount = 0
print("Calculating...")
for i in range (1000000): 
    if ch == False: #No Charm
        if random.randint(0,49) == 0: #Elite chance
            if random.randint(0,1499) == 0: #Named chance
                hexCount += 1
            else: #Elite hex chance
                if random.randint(0,1499) == 0:
                    hexCount += 1
        else: #Normal Seeker
            if random.randint(0,1499999) == 0:
                hexCount += 1
    else: # Seeker charm chance
        if random.randint(0,9) == 0: #Elite chance
            if random.randint(0,1499) == 0: #Named chance
                hexCount += 1
            else: #Elite hex chance
                if random.randint(0,1499) == 0:
                    hexCount += 1
        else: #Normal Seeker
            if random.randint(0,1499999) == 0:
                hexCount += 1

output = "In 1,000,000 seeker kills, "
if ch == True:
    output += "with "
else:
    output += "without "
output += "seeker charms, you got " + str(hexCount) + " bows"
if hexCount != 0:
    output += ", getting one on average every " + str((1000000/hexCount)) + "kills."
else:
    output += "."

print(output)