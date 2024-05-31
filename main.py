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

print("True: " + str(charmList))

cl = pd.DataFrame(charmList, columns=['Hexhunter Bows', 'Using charms', 'Average Bows'], dtype=float)
print(cl)

plot = sns.displot(data=cl, x='Average Bows', hue="Using charms", kde=True)
plot.set(ylabel="Count")
plt.show()
