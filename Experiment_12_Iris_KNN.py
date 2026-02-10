import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Data
print("Loading Iris Data...")
try:
    df = pd.read_csv('iris.csv')
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
except FileNotFoundError:
    print("iris.csv not found!")
    exit()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN Classifier (K=3)
print("\nTraining KNN Classifier (K=3)...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Evaluate
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Example Prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
print(f"\nPrediction for sample {sample}: {knn.predict(sample)}")
