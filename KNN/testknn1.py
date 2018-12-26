import matplotlib.pyplot as plt

x=[7,7,3,1]
y=[7,4,4,4]

plt.scatter(x,y)

#data baru
plt.scatter(3,7)   #scatter untuk memasukkan data baru

plt.xlabel("Daya")
plt.ylabel("Kekuatan")

plt.show()