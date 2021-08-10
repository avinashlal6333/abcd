from math import sqrt
def eaclidean_distance(row1,row2):
	distance=0
	for i in range(len(row1)-1):
		distance += (row1[i]-row2[i])**2
	return sqrt(distance)

def get_neighbor(train,test_row,num_neighbors):
	distances=list()
	for train_row in train:
		dist=eaclidean_distance(test_row,train_row)
		distances.append((dist,train_row))
	distances.sort()
	neighbors=list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][1])
	return neighbors

dataset=[[1,2,0], [3,4,0] ,[3,3,0],[7,2,1],[5,2,7],[7,3,1]]
neighbors=get_neighbor(dataset,[5,4,2],2)
for neighbor in neighbors:
	print(neighbor)

