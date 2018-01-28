import csv
import pickle

from sklearn.dummy import DummyRegressor
import numpy as np

age_range = 80
gender = {'male': 0, 'other': 0.5, 'female': 1}

X = np.array([[20 / age_range, gender['male']], [56 / age_range, gender['other']]])
Y = np.array([[.2]        , [.7]])


clf = DummyRegressor()
clf.fit(X, Y)

# print([r[2] for r in data])
print(Y)
# print([
#     movies[int(round(idx * len(movies)))]
#     for idx in clf.predict(X)
# ])
print(clf.predict([[0.2, 1]]))

with open('model.pk', 'wb') as outfile:
    pickle.dump(clf, outfile)
