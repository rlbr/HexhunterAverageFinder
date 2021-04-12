import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hex

print("Program started")
charmList = []
percentage = 0
rang = 1000

for i in range(rang):
    if (i % 10) == 0:
        print(str(percentage) + "% of the way through true.")
        percentage += 1
    charmList.append(hex.hexRollsTrue())
percentage = 0
for i in range(rang):
    if (i % 10) == 0:
        print(str(percentage) + "% of the way through false.")
        percentage += 1
    charmList.append(hex.hexRollsFalse())

# hexCount = hex.hexRolls(ch)
print("True: " + str(charmList))

cl = pd.DataFrame(charmList, columns=['Hexhunter Bows', 'Using charms', 'Average Bows'], dtype=float)
print(cl)

#plot = sns.displot(data=cl, x='Hexhunter Bows', hue="Using charms", kde=True)
plot = sns.displot(data=cl, x='Average Bows', hue="Using charms", kde=True)
plot.set(ylabel="Count")
#plot = sns.boxplot(y="Average Bows", data=cl, x="Using charms")
#plot.set(xlabel="Using charms?")
# sns.displot(ncl['Hexhunter Bows'], kind="kde")
# sns.boxplot(x='Average Bows', y='Hexhunter Bows', data=cl, )
# sns.boxplot(x='Average Bows', y='Hexhunter Bows', data=ncl, )
plt.show()

'''ncl = pd.DataFrame(noCharmList, columns=['Hexhunter Bows', 'Average Bows', 'Normal Soulgazer', 'Elite Soulgazer',
                                         'Veil-ripper Ozharakha'], dtype=float)
print(ncl)'''
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
