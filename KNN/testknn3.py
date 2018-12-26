#http://otak-keren.blogspot.com/2017/06/knearestneighbors-pada-python.html

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

x = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors = 20)

knn.fit(x,y)

knn.predict([[20,34,21,7]])