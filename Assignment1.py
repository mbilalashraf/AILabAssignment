#1. Considering the image below, develop the adjacency matrix representation of the graph.
# Find the in-degree and out-degree of V6

from IPython.display import Image
Image(filename='img.png')
adj =[[0,1,0,0,0,0,0,0,0],
      [0,0,0,1,0,0,0,0,0],
      [1,0,0,0,0,0,0,0,0],
      [0,0,0,0,1,0,1,0,0],
      [0,1,1,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,0],
      [0,0,0,0,1,1,0,0,1],
      [0,0,0,0,0,0,1,0,0]]
i=0
o=0
y=5
print("Indegree:",end=" ")
for z in range(0,9):
    p= adj[z][y]
    if(p==1):
        i = i+1
        print(z+1,end=" ")
print("\nIndegree of v6 is: ",i)
print("Outdegree:",end=" ")
for z in range(0,9):
    p= adj[y][z]
    if(p==1):
        o = o+1
        print(z+1,end=" ")
print("\nOutdegree of v6 is: ",o)

#2. Using numpy, create a matrix of 100 elements with values from 101 to 200
import numpy as np
x = np.arange(101,201)
print(x)

#3. Now, convert the above matrix to 10 X 10 array
x = x.reshape(10,10)
print(x)

#4. Assign the upper 5 X 5 sub-matrix, value equals to -1
for y in range(0,5):
    for z in range(0,5):
        x[y][z]=-1
print(x)

