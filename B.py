import A
import dir2.dir1 as dear
import numpy as np

print('Task 2:\n', A.foo(A.x), end='\n\n')

A.x = 19
print('Task 3:\nx =', A.x, '\n', A.foo(A.x), end='\n\n')

dear.A.x = 30
print('Task 6:\nx =', dear.A.x)

z = np.float32([x for x in dear.C.foo(7)])
print('z =',z,'\ntype(z) =',type(z),'\nz.dtype =',z.dtype)

dear.A.z = dear.A.z.astype(np.complex64)
print('Task 8:\nz =', dear.A.z)

dear.A.z = dear.A.z.astype(np.float_)
print(dear.A.z)
print('Task 9:\nz.dtype =', dear.A.z.dtype, '\nDet(z) =', np.linalg.det(dear.A.z))

inv = np.linalg.inv(dear.A.z)
print('Task 10:\nz^(-1) =', inv)
print('z * z^(-1) =\n', np.dot(dear.A.z, inv))
f = open('my_file.txt', 'w')
print(inv, file=f)
f.close()
