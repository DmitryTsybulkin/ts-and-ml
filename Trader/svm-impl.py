import numpy as np
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.svm import SVC

newsgroups = datasets.fetch_20newsgroups(subset='all', categories=['alt.atheism', 'sci.space'])

transformer = TfidfVectorizer()

transformed = transformer.fit_transform(newsgroups.data)

feature_mapping = transformer.get_feature_names()
for i in feature_mapping: print(i)

grid = {'C': np.power(10.0, np.arange(-5, 6))}
cv = KFold(n_splits=5, shuffle=True, random_state=241)
clf = SVC(kernel='linear', random_state=241)
gs = GridSearchCV(estimator=clf, param_grid=grid, scoring='accuracy', cv=cv, return_train_score=True)
gs.fit(transformed, newsgroups.target)
clf._get_coef()

# for i in gs.cv_results_:
    # print(i.mean_validation_score)
    # print(i.parameters)

print(np.mean(gs.cv_results_.get('parameters')))