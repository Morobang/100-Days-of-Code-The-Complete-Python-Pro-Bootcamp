# Day 65 — NumPy — SOLUTIONS
import numpy as np

def create_arrays():
    return {'zeros':np.zeros((3,4)),'ones':np.ones((2,3)),'eye':np.eye(4),
            'linspace':np.linspace(0,1,10),'arange':np.arange(0,20,2)}

def array_stats(arr):
    return {'mean':np.mean(arr,axis=0),'std':np.std(arr,axis=0),
            'min':np.min(arr,axis=0),'max':np.max(arr,axis=0),'sum':np.sum(arr,axis=0)}

def normalise(matrix):
    mean=np.mean(matrix,axis=0); std=np.std(matrix,axis=0)
    return (matrix-mean)/std

def replace_negatives(arr,fill=0):
    arr=arr.copy(); arr[arr<0]=fill; return arr

def matrix_ops(A,B):
    result={'dot':np.dot(A,B),'elementwise':A*B,'transpose':A.T}
    if A.shape[0]==A.shape[1]:
        try: result['inverse']=np.linalg.inv(A)
        except: result['inverse']=None
    return result

def batch_bmi(weights,heights):
    return np.round(weights/heights**2,1)
