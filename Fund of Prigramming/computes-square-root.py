from math import isclose, sqrt

#get input from user (i)

i = float(input("please enter number: "))

#Begin with a provisional root (r) of 1
r = 1 

#Repeatedly adjust r to compute square root^2

while not isclose (r * r, i):
    print(f"thr provisional root is {r}")
    r = (r + i/r) / 2


print(f"the square root of {i} is {r} (or {sqrt(i)}).")

