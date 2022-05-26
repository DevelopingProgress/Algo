from scipy.spatial import distance
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class NearestNeighborClassifier:
    def fit(self, features, labels):
        self.features_train = features
        self.labels_train = labels

    def predict(self, features_test):
        predictions = []

        for row in features_test:
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self, row):
        best_dist = distance.euclidean(row, self.features_train[0])
        best_index = 0

        for i in range(0, len(self.features_train)):
            dist = distance.euclidean(row, self.features_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i

        return self.labels_train[best_index]


iris = datasets.load_iris()
features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size=0.5)
model = NearestNeighborClassifier()
model.fit(features_train, labels_train)
predictions = model.predict(features_test)
result = accuracy_score(labels_test, predictions)
print(result)
