import numpy as np
from matplotlib import pyplot as plt
import math
import pylab
import rungekutt
import eiler

def diff(x,t,m):
    return (math.sqrt((m*g)/k))*math.tanh(math.sqrt((k*g)/m)*t)
def fun(m,k,g,t):
       return (m/k)*(math.log(math.cosh(math.sqrt((k*g)/m)*t)))

x=0
m=100
k=0.6
g = 9.8
T_MIN=0
T_MAX=10
COUNT=1000

tlist = np.linspace(T_MIN,T_MAX,COUNT)
xlist = [fun (m,k,g,t) for t in tlist]

xeiler = eiler.diffur_steps_params(diff, m, T_MIN, x, T_MAX, COUNT)
xrunge = rungekutt.diffur_steps_params(diff, m, T_MIN, x, T_MAX,COUNT)

plt.plot(tlist, xeiler, 'g-', linewidth=3, label='Метод Эйлера')
plt.plot(tlist, xrunge, 'b-', linewidth=2, label='Метод Рунге-Кутты')
plt.plot(tlist, xlist,'r--',linewidth=2, label="Конечная функция")
plt.legend()
plt.xlabel('Время')
plt.ylabel('Растояние')
plt.show()