import numpy as np

def fpSub(f,x0,tol,Nmax):
    count = 0
    arr = np.zeros(Nmax)
    while(count < Nmax):
        x1 = f(x0)
        arr[count] = x1
        count = count + 1
        if (abs(x1-x0) <tol):
            xstar = x1
            arr1 = np.zeros(count)
            for i in range(count):
                arr1[i] = arr[i] 
            return arr1
        x0 = x1
    return arr

def aitkens(arr):
    p = np.zeros(len(arr)-2)
    for n in range(len(arr)-2):
        p[n] = (arr[n+1]**2 - arr[n]*arr[n+2])/(2*arr[n+1]-arr[n]-arr[n+2])
        n = n+1
    return p

f1 = lambda x: 1+0.5*np.sin(x)

Nmax = 100
tol = 1e-6
x0 = 0.0

print(fpSub(f1,x0,tol,Nmax))
print(aitkens(fpSub(f1,x0,tol,Nmax)))