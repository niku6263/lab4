import numpy as np
import array

def fpSub(f,x0,tol,Nmax):
    count = 0
    arr = np.zeros(Nmax)
    while(count < Nmax):
        x1 = f(x0)
        arr[count] = x1
        count = count + 1
        if (abs(x1-x0) <tol):
            xstar = x1
            return arr
        x0 = x1
    return arr

f1 = lambda x: 1+0.5*np.sin(x)
f2 = lambda x: 3+2*np.sin(x)

Nmax = 100
tol = 1e-6
x0 = 0.0

print(fpSub(f1,x0,tol,Nmax))
print(fpSub(f2,x0,tol,Nmax))