#Carlos Eduardo de la Rosa Noriega
#Solución numérica del proyecto final

import scipy as sp
import matplotlib.pylab as plt
import math as math


#Solución numérica
#T''+2T'-8T=0, T(0)=10, T(10)=0
#shooting method
#T'=z, z'=8T-2z
T0=10.0
T10=0.0
z=0.0 #proposición de valor para z
h=0.01 #step size

T=T0
p0=z

Tpoints=[]
xpoints=[]
zpoints=[]

def f(x, T, z):
    return z

def g(x,T,z):
    return (8*T - 2*z)

i=0.0
while(i<=10.01):
    xpoints.append(i)
    i+=h

for x in xpoints:
    Tpoints.append(T)
    zpoints.append(z)

    k1=h*f(x, T, z)
    l1=h*g(x, T, z)

    k2=h*f(x + 0.5*h, T + 0.5*k1, z +0.5*l1)
    l2=h*g(x + 0.5*h, T + 0.5*k1, z +0.5*l1)

    k3=h*f(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)
    l3=h*g(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)

    k4=h*f(x+h, T + k3, z + k3)
    l4=h*g(x+h, T + k3, z + k3)

    T +=  (1/6) * (k1+ 2*k2 + 2*k3 + k4)
    z +=  (1/6) * (l1+ 2*l2 + 2*l3 + l4)
    #print(x)

q0=T
z=-25.0
p1=z
T=T0

Tpoints.clear()
zpoints.clear()

for x in xpoints:
    Tpoints.append(T)
    zpoints.append(z)

    k1=h*f(x, T, z)
    l1=h*g(x, T, z)

    k2=h*f(x + 0.5*h, T + 0.5*k1, z +0.5*l1)
    l2=h*g(x + 0.5*h, T + 0.5*k1, z +0.5*l1)

    k3=h*f(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)
    l3=h*g(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)

    k4=h*f(x+h, T + k3, z + k3)
    l4=h*g(x+h, T + k3, z + k3)

    T +=  (1/6) * (k1+ 2*k2 + 2*k3 + k4)
    z +=  (1/6) * (l1+ 2*l2 + 2*l3 + l4)

q1=T

p=( p0 +  (p1-p0)/(q1-q0) * -q0   )
print("Valor aproximado para 'z': ")
print(p)
Tpoints.clear()
zpoints.clear()

z=p
T=T0
for x in xpoints:
    Tpoints.append(T)
    zpoints.append(z)

    k1=h*f(x, T, z)
    l1=h*g(x, T, z)

    k2=h*f(x + 0.5*h, T + 0.5*k1, z +0.5*l1)
    l2=h*g(x + 0.5*h, T + 0.5*k1, z +0.5*l1)

    k3=h*f(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)
    l3=h*g(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)

    k4=h*f(x+h, T + k3, z + k3)
    l4=h*g(x+h, T + k3, z + k3)

    T +=  (1/6) * (k1+ 2*k2 + 2*k3 + k4)
    z +=  (1/6) * (l1+ 2*l2 + 2*l3 + l4)

print("Temperatura con ese valor inicial en x=10: ")
print(round(T))
##################################################
#Solución numérica RK4
z=p
T=T0
Tpoints.clear()
zpoints.clear()
for x in xpoints:
    Tpoints.append(T)
    zpoints.append(z)

    k1=h*f(x, T, z)
    l1=h*g(x, T, z)

    k2=h*f(x + 0.5*h, T + 0.5*k1, z +0.5*l1)
    l2=h*g(x + 0.5*h, T + 0.5*k1, z +0.5*l1)

    k3=h*f(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)
    l3=h*g(x+ 0.5*h, T + 0.5 * k2, z+ 0.5*l2)

    k4=h*f(x+h, T + k3, z + k3)
    l4=h*g(x+h, T + k3, z + k3)

    T +=  (1/6) * (k1+ 2*k2 + 2*k3 + k4)
    z +=  (1/6) * (l1+ 2*l2 + 2*l3 + l4)



######################################################3
#Solución analítica
x=[]
y=[]

c2= -10*math.exp(-40) / ( math.exp(20) - math.exp(-40) )
c1=10 - c2

for i in range(0,110):
    x.append(i/10);
    y.append(( c1 * math.exp(-4 * x[i])) - (c2 * math.exp(2 * x[i] )) )

###########################################################3

plt.xlabel('x (m)')
plt.ylabel('T (°C)')
plt.title("Temperatura (°C) vs posición del cilíndro (m)")
plt.plot(x,y, color='green', linewidth=4, linestyle='dashed', label="Solución analítica")
plt.plot(xpoints, Tpoints, color='blue', label="Solución numérica")
plt.legend()
plt.show()
