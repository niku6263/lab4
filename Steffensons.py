import numpy as np

def steffensons(f,x0,tol,Nmax):
    count = 0
    arr = np.zeros(Nmax+1)
    while(count < Nmax):
        a = arr[count]
        b = f(arr[count])
        c = f(b)
        arr[count+1] = a - (((b-a)**2)/ c - 2*b + a)
        count = count + 1
        if (abs(arr[count]-arr[count-1]) <tol):
            arr1 = np.zeros(count)
            for i in range(count):
                arr1[i] = arr[i] 
            return arr1
    return arr

f1 = lambda x: 1+0.5*np.sin(x)

Nmax = 100
tol = 1e-10
x0 = 1.5

print(steffensons(f1,x0,tol,Nmax))