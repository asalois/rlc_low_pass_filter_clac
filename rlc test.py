#  a simple program to calculate values of Q and omega not for a series rlc low pass filter
# by Alex Salois Feb 2018


import math
import numpy as np


def find_w (l, c):  # a function to calc w from inputs of the inductor and capacitor values
    w = 1 / math.sqrt(l * c)
    return w


def find_q (r, l, c):  # a function to calc Q from Resistor, Inductor and capacitor values
    q = 1 / r * (math.sqrt(l/c))
    return q


f, v = np.loadtxt('input/Lab 6.csv', delimiter=',', unpack=True, skiprows=1)

for i, ele in enumerate(f):
    if 24999 < f[i] < 25001:
        print("25000=", v[i])
    if 9999 < f[i] < 10001:
        print("10000=", v[i])


# a list to hold values of the inductor values
list_l = [.001, .01, .082]
cc = .000000027
for j in range(1, 10000):  # for loop to try different c values
    w = find_w(list_l[1], cc)
    if w > math.pi * 2 * 14000 -1:
            if w < math.pi * 2 * 16000 + 1000:
                print(w)
                print(list_l[1], cc)

for m in range(1, 100000):  # for loop to find different q values
    q = find_q(m, list_l[1], cc)
    if q > .8:
        if q < .9:
            if m == 710:
                print(m, q)

qh = find_q(710*1.05, list_l[1]*1.1, cc*1.10)
ql = find_q(710*.95, list_l[1]*.9, cc*.9)
print("Tolerance:", "High=", qh, "Low=", ql)
w = find_w(list_l[1], cc)
print("Inductor=", list_l[1], "Capacitor=", cc, "Ressitor=", 710)
print(w, w / (2*math.pi))
