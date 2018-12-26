#http://otak-keren.blogspot.com/2017/06/knearestneighbors-pada-python.html


from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris=load_iris()

x=iris.data     #merupakan ciri ciri atau nilai fitur
y=iris.target   #merupakan pelabelan data

#penentuan nilai K
k_range= range(1,31)    #penentuan range =>30
k_skor=[]               #list untuk menampung nilai n nantinya

for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    skor = cross_val_score(knn, x, y, cv=10, scoring='accuracy')     #cv adalah lipatan data; scoring berdasarkan akurasi
    k_skor.append(skor.mean())                                      #memasukkan nilai mean kedalam list

plt.plot(k_range, k_skor) 
plt.xlabel('K argument')
plt.ylabel('K Skor')

plt.show()