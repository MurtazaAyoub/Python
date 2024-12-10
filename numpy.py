#saving a single array

import numpy as np
arr = np.array([1, 2, 3, 4])
np.save('array.npy', arr)
loaded = np.load('array.npy')
print(loaded)


#saving multile arrays
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
np.savez('arrays.npz', a=arr1, b=arr2)
data = np.load('arrays.npz')
print(data['a'])
print(data['b'])