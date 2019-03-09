import numpy as np
from sklearn import datasets as ds
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

data = ds.load_boston()
X = data.data
y = data.target
preprocessing.scale(X)

block_splitter = KFold(n_splits=5, shuffle=True, random_state=42)

optimal_p = np.linspace(start=1, stop=10, num=200)
cv_quality = list()

for i in optimal_p:
    knn = KNeighborsRegressor(n_neighbors=5, weights='distance', metric='minkowski', p=i)
    knn.fit(X, y)
    cv_quality.append(
        np.mean(cross_val_score(estimator=knn, X=X, y=y, cv=block_splitter, scoring='neg_mean_squared_error')))

print(cv_quality.index(max(cv_quality)))