from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from sklearn import tree

data = pd.read_csv('titanic.csv')

data.describe()
data.info()

ind = pd.isnull(data['Age'])
data = data[~ind]

Sex = list()
for i in data.Sex:
    Sex.append(i)

data = data.drop('Sex', axis=1)
int_sex = list()
for i in Sex:
    if i == 'male':
        int_sex.append(0)
    if i == 'female':
        int_sex.append(1)

data['Sex'] = int_sex

X = pd.DataFrame(data, columns=['Pclass', 'Fare', 'Age', 'Sex'])
y = np.array(data['Survived'])

clf = tree.DecisionTreeClassifier(random_state=241)

clf.fit(X, y)

important_features = clf.feature_importances_
print(X.describe())
print(important_features)