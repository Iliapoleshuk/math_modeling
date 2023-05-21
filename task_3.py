import numpy as np
y = int(input())
x = int(input())
v = int(input())
g = 10
t= np.arange(0,5.01,0.01)
for i in range(0,len(t),1):
    s = x + v*t
    l = y + v*t - (g*t**2)/2
    a = [t,s,l]
k = np.array(a)
print(k)
