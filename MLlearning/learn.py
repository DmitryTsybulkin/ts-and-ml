import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

data = pd.read_csv('titanic.csv', index_col='PassengerId')

male_count = sum(data['Sex'] == 'male')
female_count = sum(data['Sex'] == 'female')

survived_percent = sum(data['Survived'] == 1) * 100 / len(data['Survived'])

first_class_percent = sum(data['Pclass'] == 1) * 100 / len(data['Pclass'])

mean_age = data['Age'].mean()
median_age = data['Age'].median()

SibSp_corr_Parch = data['SibSp'].corr(data['Parch'])

only_female = data[(data['Sex'] == 'female')]
only_female = only_female.reset_index()

names = list()


def getName(name):
    string = str()
    ls = name.split(' ')
    for i in ls:
        if i == 'Miss.' or i == 'Mrs.':
            string = ls[ls.index(i) + 1]
    return string


for name in only_female['Name']:
    names.append(getName(name))

print(names)

final_names = list()

for i in names:
    final_names.append(i.strip('()'))

names.clear()
names = pd.Series(final_names)



#  TODO: just delete '()' in list and analyze it
