import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import hex

print("Program started")
charmList = []
noCharmList = []
percentage = 0

for i in range(1000):
    if (i % 10) == 0:
        print(str(percentage) + "% of the way through.")
        percentage += 1
    charmList.append(hex.hexRollsTrue())
    noCharmList.append(hex.hexRollsFalse())

# hexCount = hex.hexRolls(ch)
print("True: " + str(charmList))
print("False: " + str(noCharmList))

'''charms = input("Charms? Type 1 for yes or 0 for no: ")
ch = False
if charms == "1":
    ch = True
    
output = "In 1,000,000 seeker kills, "
if ch == True:
    output += "with "
else:
    output += "without "
output += "seeker charms, you got " + str(hexCount) + " bows"
if hexCount != 0:
    output += ", getting one on average every " + str((1000000/hexCount)) + " kills."
else:
    output += "."'''

# print(output)
# print("\nYou got bows from the following creatures: \nNormal Soulgazers: " + str(normCount) + "\nElite Soulgazers: " + str(eliteCount) + "\nVeil-ripper Ozharakha: " + str(nameCount))
