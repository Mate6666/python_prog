# Kör területe: r^2*PI
# print(math.pi)
import math
d = int(input("Kérem az átmérőjét:"))
r = d/2
#T = r**2*math.pi
pi = math.pi 
T = math.pow(r,2)*math.pi
x = round(T,2) 
print(f"A kör területe: {x}")
K = 2*r*math.pi
y = round(K,2)
print(f"A kör kerülete: {y}")

d = 10 
T2 = (math.pow(d,2)*pi)/4
z = round(T2,2)
print(f"A kör kerülete: {z}")

