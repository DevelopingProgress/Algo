from sklearn.neighbors import NearestCentroid
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = load_iris()

X = pd.DataFrame(dataset.data)
y = pd.DataFrame(dataset.target)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=0)
model = NearestCentroid()
model.fit(X_train, y_train.values.ravel())

print(f"Training Set Score : {model.score(X_train, y_train) * 100} %")
print(f"Test Set Score : {model.score(X_test, y_test) * 100} %")
print(f"Model Classification Report : \n{classification_report(y_test, model.predict(X_test))}")