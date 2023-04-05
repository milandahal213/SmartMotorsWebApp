try:
    from ulab import numpy as np
except ImportError:
    import numpy as np

a = np.array([1, 2, 3, 4], dtype=np.int8)
b = a.copy()
print(b)
a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int16)
b = a.copy()
print(b)
a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float)
b = a.copy()
print(b)
print(a.dtype)
print(a.flatten())
print(np.array([1,2,3], dtype=np.uint8).itemsize)
print(np.array([1,2,3], dtype=np.uint16).itemsize)
print(np.array([1,2,3], dtype=np.int8).itemsize)
print(np.array([1,2,3], dtype=np.int16).itemsize)
print(np.array([1,2,3], dtype=np.float).itemsize)
print(np.array([1,2,3], dtype=np.float).shape)
print(np.array([[1],[2],[3]], dtype=np.float).shape)
print(np.array([[1],[2],[3]], dtype=np.float).reshape((1,3)))
print(np.array([[1],[2],[3]]).size)
print(np.array([1,2,3], dtype=np.float).size)
print(np.array([1,2,3], dtype=np.uint8).tobytes())
print(np.array([1,2,3], dtype=np.int8).tobytes())
print(np.array([1,2,3], dtype=np.float).transpose().shape)
print(np.array([[1],[2],[3]], dtype=np.float).transpose().shape)
a = np.array([1, 2, 3, 4, 5, 6], dtype=np.uint8)
b = a.byteswap(inplace=False)
print(a)
print(b)
c = a.byteswap(inplace=True)
print(a)
print(c)
a = np.array([1, 2, 3, 4, 5, 6], dtype=np.uint16)
b = a.byteswap(inplace=False)
print(a)
print(b)
c = a.byteswap(inplace=True)
print(a)
print(c)
