import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'IAm':lst})
#print(data)

one_hot = pd.DataFrame({'robot': (data['IAm'] == 'robot').astype(int), 'human': (data['IAm'] == 'human').astype(int)})

print(one_hot.head())
