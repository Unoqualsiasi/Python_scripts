#Example of IsolationForest on Iris dataset

#!/usr/bin/env python3.6

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)
data = load_iris()

X=data.data
y=data.target
X_outliers = rng.uniform(low=-4, high=4, size=(X.shape[0], X.shape[1]))

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=0)

clf = IsolationForest()
clf.fit(X_train)

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)

print(y_pred_test)
print(y_pred_outliers)
