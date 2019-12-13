import pandas as pd
import numpy as np


df = pd.read_excel("./lottery_data.xlsx")
next_list = df[df['1'] == 1].index.tolist()
next_list = [i + 1 for i in next_list]
next_number_list = []
for k in next_list:
    for j in df['1']:
        next_number_list.append(df['1'][k])

print(next_number_list[:10])
# print(next_list)
# print(df['1'][1])

