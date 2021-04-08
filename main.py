import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hex

print("Program started")
charmList = []
noCharmList = []
percentage = 0

for i in range(10):
    if (i % 10) == 0:
        print(str(percentage) + "% of the way through.")
        percentage += 1
    charmList.append(hex.hexRollsTrue())
    noCharmList.append(hex.hexRollsFalse())

# hexCount = hex.hexRolls(ch)
print("True: " + str(charmList))
print("False: " + str(noCharmList))

cl = pd.DataFrame(charmList, columns=['Hexhunter Bows', 'Average Bows', 'Normal Soulgazer', 'Elite Soulgazer',
                                      'Veil-ripper Ozharakha'], dtype=float)
print(cl)

ncl = pd.DataFrame(noCharmList, columns=['Hexhunter Bows', 'Average Bows', 'Normal Soulgazer', 'Elite Soulgazer',
                                         'Veil-ripper Ozharakha'], dtype=float)
print(ncl)

sns.boxplot(x='Average Bows',y='Hexhunter Bows',data=cl,)
sns.boxplot(x='Average Bows',y='Hexhunter Bows',data=ncl,)
plt.show()

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
# print("\nYou got bows from the following creatures: \nNormal Soulgazers: " + str(normCount) + "\nElite
# Soulgazers: " + str(eliteCount) + "\nVeil-ripper Ozharakha: " + str(nameCount))
