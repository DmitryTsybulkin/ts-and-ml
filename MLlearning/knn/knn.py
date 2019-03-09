import pandas as pd
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import numpy as np
import sklearn.metrics as ms

data = pd.read_csv('wine.csv')

split_generator = KFold(n_splits=5, shuffle=True, random_state=42)

X = data.drop(labels='class', axis=1)
y = data['class']

X_train, X_test, y_train, y_test = train_test_split(X, y)

cv = dict()
neighbors = range(1, 51)

for i in neighbors:
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    first_mse = ms.mean_squared_error(y_true=y_test, y_pred=pred)
    cv[i] = np.mean(cross_val_score(estimator=model, X=X_train, y=y_train, cv=split_generator, scoring='accuracy'))

#  0.7282051282051282
X = scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y)

cross_v = dict()

for i in neighbors:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    predict = knn.predict(X_test)
    second_mse = ms.mean_squared_error(y_true=y_test, y_pred=predict)
    cross_v[i] = np.mean(cross_val_score(estimator=knn, X=X_train, y=y_train, cv=split_generator, scoring='accuracy'))

# 0.9626780626780628