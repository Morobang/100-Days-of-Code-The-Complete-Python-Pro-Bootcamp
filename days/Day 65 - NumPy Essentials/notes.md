# Day 65 — NumPy Essentials

## Key syntax
```python
import numpy as np

np.array([1,2,3])
np.zeros((3,4)); np.ones((2,3)); np.eye(4)
np.linspace(0,1,10); np.arange(0,20,2)
np.random.randn(3,3); np.random.randint(0,10,(3,3))

arr.shape; arr.dtype; arr.ndim; arr.size
arr.reshape((3,4)); arr.flatten()
arr.T  # transpose

# Indexing
arr[1,2]; arr[0,:]; arr[:,1]; arr[arr>5]  # boolean

# Math
np.mean(arr,axis=0); np.std(arr,axis=1)
np.sum, np.min, np.max, np.argmax
arr1 + arr2; arr * 3  # broadcasting
np.dot(A, B); np.linalg.inv(A); np.linalg.det(A)
```

## Broadcasting rules
Arrays are broadcast together when dimensions are compatible:
`(3,1) op (1,4) → (3,4)`

## Interview tips
- NumPy is 10-100x faster than Python loops for numeric operations
- Always specify `axis` for reductions (0=along rows, 1=along columns)
- `@` operator for matrix multiplication (Python 3.5+)
