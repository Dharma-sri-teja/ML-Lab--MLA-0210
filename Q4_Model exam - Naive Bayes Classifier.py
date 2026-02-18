from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'PolicyType': ['Premium','Premium','Basic','Basic'],
    'ClaimAmount': ['Low','High','High','Low'],
    'History': ['Good','Good','Poor','Poor'],
    'Approval': ['Yes','Yes','No','No']
}

df = pd.DataFrame(data)

le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = CategoricalNB()
model.fit(X, y)

# Predict new case
# Example: Premium, Low, Good
new_case = [[1, 1, 1]]  # Adjust according to encoding
prediction = model.predict(new_case)

print("Prediction:", prediction)
