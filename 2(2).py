import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import eiler
import rungekutt

def diff(x,t,P):
    dxdt = k * (P-x)
    return dxdt

def func(P,t,k):
	x = P*(1 - math.e**(-k*t))
	return x

x =0 
P = 100
k = 0.9
T_MIN = 0
T_MAX = 5
COUNT = 150

tlist = np.linspace(T_MIN,T_MAX,COUNT)
xlist = [func (P,t,k) for t in tlist]

y = odeint(diff, x, tlist, args=(P,))
xeiler = eiler.diffur_steps_params(diff, P, T_MIN, x, T_MAX, COUNT)
xrunge = rungekutt.diffur_steps_params(diff, P, T_MIN, x, T_MAX, COUNT)

plt.plot(tlist, y, 'b-', linewidth=2, label='Численный метод')
plt.plot(tlist, xeiler, 'g-', linewidth=2, label='Метод Эйлера')
plt.plot(tlist, xrunge, 'y-', linewidth=2, label='Метод Рунге-Кутты')
plt.plot(tlist, xlist, 'r--', label='Конечная функция')
plt.legend()
plt.xlabel('Время')
plt.ylabel('m(t)')
plt.grid()
plt.show()