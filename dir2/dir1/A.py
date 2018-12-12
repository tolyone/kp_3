import numpy as np

x = 6

def foo(x):
    return x*x

z = np.array([ [2, 7, 3], [3, 9, 4], [1, 5, 3] ])
z = z.astype(np.int_)
print('Task 8:\n', z, 'z.dtype =', z.dtype, end='\n\n')
