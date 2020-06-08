import numpy as np

mat1 = np.array([data.split() for data in open("./data2.dat","r") ], dtype=float)
mat2 = np.array([data.split() for data in open("./data3.dat","r") ], dtype=float)

print( mat1 + mat2 )
print( mat1 - mat2 )
print( mat1 * mat2 )
print( np.dot(mat1,mat2.T) )