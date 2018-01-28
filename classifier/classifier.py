import csv
import pickle

from sklearn.neural_network import MLPRegressor

with open('raw.csv', 'r') as infile:
    data = list(csv.reader(infile))[1:]

age_min = min(int(r[0]) for r in data)
age_max = max(int(r[0]) for r in data)
age_range = age_max - age_min

gender = {'male': 0, 'other': 0.5, 'female': 1}

movies = list(set(r[2] for r in data))

X = [
        [
            int(r[0]) / age_range,
            gender[r[1].lower()]
        ]
        for r in data
    ]
Y = [
        [movies.index(r[2]) / len(movies)]
        for r in data
    ]


clf = MLPRegressor()

clf.fit(X, Y)

# print([r[2] for r in data])
print(Y)
# print([
#     movies[int(round(idx * len(movies)))]
#     for idx in clf.predict(X)
# ])
print(clf.predict(X))

with open('model.pk', 'wb') as outfile:
    pickle.dump(clf, outfile)
