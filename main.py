import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hex
import multiprocessing

print("Program started")
charmList = []
percentage = 0
rang = 1000
with multiprocessing.Pool() as p:
    charmList += list(p.map(hex.hexRollsTrue, range(1000)))

with multiprocessing.Pool() as p:
    charmList += list(p.map(hex.hexRollsFalse, range(1000)))

print("True: " + str(charmList))

cl = pd.DataFrame(
    charmList, columns=["Hexhunter Bows", "Using charms", "Average Bows"], dtype=float
)
print(cl)

plot = sns.displot(data=cl, x="Average Bows", hue="Using charms", kde=True)
plot.set(ylabel="Count")
plt.show()
