import numpy as np
from numpy import array, exp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N = 17     # число экспериментов
# sigma = 3   # стандартное отклонение наблюдаемых значений
# k = 0.5     # теоретическое значение параметра k
# b = 2       # теоретическое значение параметра b

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
# f = np.array([k*z+b for z in range(N)])
y = np.array([3.29, 6.34, 8.30, 11.85, 12.79, 17.69, 22.66, 23.38, 27.77, 29.85, 32.42, 37.83, 40.22, 43.34, 45.38, 46.30, 51.13])
x = np.array(x, dtype=float) #transform your data in a numpy array of floats
y = np.array(y, dtype=float) #so the curve_fit can wo
# вычисляем коэффициенты

mx = x.sum()/N
my = y.sum()/N
a2 = np.dot(x.T, x)/N
a11 = np.dot(x.T, y)/N

def func(mx=mx, my=my, a11=a11, a2=a2):
    kk = (a11 - mx * my) / (a2 - mx ** 2)
    bb = my - kk * mx
    print(kk, bb)
    return kk, bb

def func2(x, a, b):
    return b*(a**x)

def func1(x, a, b):
    # return b*(a**x)
    # return a * exp(x * b)
    return a * np.log(b * x)

ff = np.array([func()[0]*z+func()[1] for z in range(N)])

popt, pcov = curve_fit(func1, x, y)
popt1, pcov1 = curve_fit(func2, x, y)

plt.scatter(x, y, s=2, c='red')
# plt.plot(f)
plt.plot(x, func1(x, *popt), label="1") #same as line above \/
plt.plot(x, func2(x, *popt1), label="2") #same as line above \/
# plt.plot(x, func1(x, *[1.159462, 5.6917]), label="log") #same as line above \/
plt.legend(loc='upper left')
plt.plot(ff, c='red')
plt.grid(True)
plt.show()
