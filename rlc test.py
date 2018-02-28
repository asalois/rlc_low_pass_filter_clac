import math

def find_w (l, c):
    w = 1 / math.sqrt(l * c)
    return w

def find_q (r, l, c):
    q = 1 / r * (math.sqrt(l/c))
    return q

list_l = [.001, .01, .082]
k = 0
cc = .000000027
for j in range(1, 10000):
    w = find_w(list_l[1], cc)
    if w > math.pi * 2 * 14000 -1:
            if w < math.pi * 2 * 16000 + 1000:
                print(w)
                print(list_l[1], cc)

for m in range(1, 100000):
    q = find_q(m, list_l[1], cc)
    if q > .8:
        if q < .9:
            if m == 710:
                print(m, q)

w = find_w(list_l[1], cc)
print( list_l[1], cc , 710)
print(w, w / (2*math.pi))
