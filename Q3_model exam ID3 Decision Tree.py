import pandas as pd
import math

data = {
    'PolicyType': ['Premium','Premium','Basic','Basic'],
    'ClaimAmount': ['Low','High','High','Low'],
    'History': ['Good','Good','Poor','Poor'],
    'Approval': ['Yes','Yes','No','No']
}

df = pd.DataFrame(data)

def entropy(target):
    counts = target.value_counts()
    total = len(target)
    return -sum((count/total)*math.log2(count/total) for count in counts)

def information_gain(df, attr, target='Approval'):
    total_entropy = entropy(df[target])
    values = df[attr].unique()
    weighted_entropy = 0
    for val in values:
        subset = df[df[attr] == val]
        weighted_entropy += (len(subset)/len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

for col in df.columns[:-1]:
    print(f"Information Gain for {col}:",
          information_gain(df, col))

