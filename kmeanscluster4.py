from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
Data={'x':[1.713,0.180,0.353,0.940,1.486,1.266,1.540,0.5459,0.773],'y':[1.586,1.786,1.240,1.566,1.759,10.106,0.419,1.799,0.816]}

df=DataFrame(Data,columns=['x','y'])
kmeans=KMeans(n_clusters=3).fit(df)
centriods=kmeans.cluster_centers_
print(centriods)

plt.scatter(df['x'],df['y'],s=50)
plt.scatter(centriods[:,0],centriods[:,1],c='red',s=50)
plt.show()
