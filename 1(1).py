import numpy as np
import matplotlib.pyplot as plt
import math
import eiler
import rungekutt

def model(x,t):
    k  = math.log1p(2 ** (1/1590) - 1)
    dxdt = - k * x
    return dxdt

def func(m0,t):
    return m0*(2**(-t/1590))

m0 = 100
T_MIN = 0
T_MAX = 15000
COUNT = 1000

tlist = np.linspace(T_MIN,T_MAX,COUNT)
xlist = [func (m0,t) for t in tlist]

xeiler = eiler.diffur(model, T_MIN, m0, T_MAX, COUNT)
yrunge = rungekutt.diffur(model, T_MIN, m0, T_MAX, COUNT)

plt.plot(tlist, xeiler, 'g-', linewidth=2, label='Метод Эйлера')
plt.plot(tlist, yrunge, 'y-', linewidth=2, label='Метод Рунге-Кутты')
plt.plot(tlist, xlist, 'r--', label='Конечная функция')
plt.legend()
plt.xlabel('Время')
plt.ylabel('m(t)')
plt.show()
