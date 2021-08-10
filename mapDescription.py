import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.cluster import KMeans
from sklearn import datasets 

df=datasets.load_iris()
x=df.data
y=df.target

print(x)
print(y)

kmean=KMeans(n_clusters=5)
y_kmean=kmean.fit_predict(x)
print(y_kmean)

print(kmean.cluster_centers_)

Error=[]
for i in range(1,11):
	kmeans=KMeans(n_clusters=i).fit(x)
	kmeans.fit(x)
	Error.append(kmeans.inertia_)
import matplotlib.pyplot as plt
plt.plot(range(1,11),Error)
plt.title('Elbow method')
plt.xlabel('no of clusters')
plt.ylabel('Error')
plt.show()

kmeans3=KMean(n_clusters=3)
y_kmeans3=kmeans3.fit_predict(x)
print(y_kmeans3)

print(kmeans3.cluster_centers_)


