import numpy
import math
import lec_3_task_1 
h = 10 ** (-1)
t = math.sin(math.pi/6) / math.cos(math.pi/6)
b = math.sin(math.pi/3) / math.cos(math.pi/3)
c = math.cos(math.pi/3)
from lec_3_task_1 import g
v = (g*h*(t**2)/2*(c**2)*(1-t*b))**(1/2)
print(v)


from lec_3_task_1 import k
from lec_3_task_1 import  e
from lec_3_task_1 import  h
T = 200
E = 300

a = 2 / math.sqrt(math.pi)
b = h / math.sqrt((k*T)**3)
c = e ** (-E / k*T)
d = E ** (T/2)
N = a * b * c * d
print(N)
