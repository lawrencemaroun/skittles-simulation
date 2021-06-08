import numpy as np
import random
import pandas as pd

bulk_batch = []
colours = ['r','g','b','y','o']

for c in colours:
    for i in range(100000):
        bulk_batch.append(c)

random.shuffle(bulk_batch)

bags = {'r':[],'g':[],'b':[],'y':[],'o':[]}
last_bag = False

while len(bulk_batch) > 0:
    size = random.randint(53,64)
    
    new_bag = {'r':0,'g':0,'b':0,'y':0,'o':0}
    
    for i in range(size):
        try:
            colour = bulk_batch.pop()
            new_bag[colour] = new_bag[colour] + 1
        except:
            last_bag = True
            break
    
    if last_bag:
        break

    for key in new_bag:
        bags[key].append(new_bag[key])

bags_df = pd.DataFrame(bags)

bags_df.to_csv("output.csv")


