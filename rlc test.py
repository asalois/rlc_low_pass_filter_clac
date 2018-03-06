#  a simple program to calculate values of Q and omega not for a series rlc low pass filter
# by Alex Salois Feb 2018


import math
import numpy as np

# def fill(array, Q):
#     for idx, line in enumerate(array):
#         array[idx] = transfer(idx, 1, Q)
#     return  array
#
#
# def transfer(w1, w0, Q):
#     h = w0**2/(w0**2-w1**2+j*w0/Q*w1)
#     return h
#
#
# size = 10000000
# w = np.linspace(1, 10000000, size)
# play = np.empty(size)
# y = np.empty(size)
# y = fill(play, 1)
# z = np.empty(size)
# z = fill(play, 2)
# a = np.empty(size)
# a = fill(play, .8)
# b = np.empty(size)
# b = fill(play, 5)
#
# plt.figure(1)
# plt.plot(w, y, label='Q = 1')
# plt.plot(w, z, label='Q = 2')
# plt.plot(w, a, label='Q = .8')
# plt.plot(w, b, label='Q = 5')
#
# plt.show()


def find_w(l, c):  # a function to calc w from inputs of the inductor and capacitor values
    w = 1 / math.sqrt(l * c)
    return w


def find_q(r, l, c):  # a function to calc Q from Resistor, Inductor and capacitor values
    q = 1 / r * (math.sqrt(l/c))
    return q


f, v = np.loadtxt('input/Lab 6.csv', delimiter=',', unpack=True, skiprows=1)

# a loop to show values in range specified
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
                x = 0


ql = find_q(710*1.05, list_l[1]*1.1, cc*1.10)
qh = find_q(710*.95, list_l[1]*.9, cc*.9)
wh = find_w(list_l[1]*.9, cc*.9)
wl = find_w(list_l[1]*1.1, cc*1.10)
print("Q=", find_q(710, list_l[1], cc))
print("Tolerance of Q:", "High=", qh, "Low=", ql)
print("Tolerance of Wo:", "High=", wh, "Low=", wl)
w = find_w(list_l[1], cc)
print("Inductor=", list_l[1], "Capacitor=", cc, "Resistor=", 710)
print("w=", w, "fo=", w / (2*math.pi))
