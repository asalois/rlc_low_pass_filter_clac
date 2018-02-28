#  a simple program to calculate values of Q and omega not for a series rlc low pass filter

import math


def find_w (l, c):  # a function to calc w from inputs of the inductor and capacitor values
    w = 1 / math.sqrt(l * c)
    return w


def find_q (r, l, c):  # a function to calc Q from Resistor, Inductor and capacitor values
    q = 1 / r * (math.sqrt(l/c))
    return q


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


w = find_w(list_l[1], cc)
print("Inductor", "Capacitor", "Resistor")
print( list_l[1], cc, 710)
print(w, w / (2*math.pi))
