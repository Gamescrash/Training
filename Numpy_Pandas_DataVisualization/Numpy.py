import numpy as np

# a = np.array([5,6,9])
# print(a.ndim)

# print(a.itemsize)
# print(a.size)
a = np.arange(12).reshape(3,4)
print(a)
print("\n")

# for row in a:
#     for cell in row:
#         print(cell)
# print("\n")

for cell in a.flat:
    print(cell)
print("\n")

for x in np.nditer(a, order='F'): #Fortran order - another paramether: flags=['external_loop']
    print(x)
print("\n")

