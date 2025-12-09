import numpy as np
print( np.__version__)

a=np.array([1, 2, 3])
print("Array a:", a)

c=np.zeros(5)
print(c)

d=np.ones(4)
print(d)


f=np.arange(0, 10, 2)
print(f)

g=np.linspace(0, 1, 5)
print(g)

h=np.random.random((3,3))
print(h)

i=np.eye(3)
print(i)

j=np.array([[1, 2], [3, 4]])
print("Matrix j:\n", j)

k=np.array([[5, 6], [7, 8]])
print("Matrix k:\n", k)

sum_result = j + k
print("Sum of j and k:\n", sum_result)

prod_result = np.dot(j, k)
print("Product of j and k:\n", prod_result)

i=a + d
print("\n",i)