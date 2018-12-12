def foo(n):
    for i in range(n):
        yield (-1)**(i+1)


L = [x for x in foo(7)]

print('Task 5:\nL =',L, end='\n\n')

print('Task 7:\nlist')  
M = [x for x in foo(10)]
for e in M:
    print(e)
