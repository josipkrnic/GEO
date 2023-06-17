import numpy as np
import matplotlib.pyplot as plt
#UNESCO jednadžba stanja: ro = ro1/(1-P/K)
def funkcija(f,x):
    return f(x)
#RAČUNAMO RO1 iz jednadžbe stanja, uzimam formule iz prethodnih vježbi, ro1 kao varijable uzima temperaturu T u °C i salinitet u g/kg
def ro1(T,S):
    a0=999.842594
    a1=6.793953*10**(-2)
    a2=-9.09529*10**(-3)
    a3=1.001685*10**(-4)
    a4=-1.120083*10**(-6)
    a5=6.536332*10**(-9)
    b0=8.2449*10**(-1)
    b1=-4.0899*10**(-3)
    b2=7.6438*10**(-5)
    b3=-8.2467*10**(-7)
    b4=5.3875*10**(-9)
    c0=-5.7246*10**(-3)
    c1=1.0227*10**(-4)
    c2=-1.6546*10**(-6)
    d0=4.8314*10**(-4)
    R1 = a0+a1*T+a2*T**2+a3*T**3+a4*T**4+a5*T**5
    R2 = b0+b1*T+b2*T**2+b3*T**3+b4*T**4
    R3 = c0+c1*T+c2*T**2
    return R1 + R2*S + R3*S**(3/2) + d0*S**2
#računamo modul kompresibilnosti K koji za parametre uzima T,S i dubinu h u metrima, preko koje izražavamo ovisnost o tlaku, p = h/10, u bar
def K(T,S,h):
    e0=19652.21
    e1=148.42
    e2=-2.327105
    e3=1.360447*10**(-2)
    e4=-5.155288*10**(-5)
    f0=54.6746
    f1=-0.603459
    f2=1.09987*10**(-2)
    f3=-6.167*10**(-5)
    g0=7.944*10**(-2)
    g1=1.6483*10**(-2)
    g2=-5.3009*10**(-4)
    K1 = e0+e1*T+e2*T**2+e3*T**3+e4*T**4
    K2 = f0+f1*T+f2*T**2+f3*T**3
    K3 = g0+g1*T+g2*T**2
    K0 = K1 + K2*S + K3*S**(3/2)
    h0=3.2399;
    h1=1.43713*10**(-3)
    h2=1.16092*10**(-4)
    h3=-5.77905*10**(-7)
    i0=2.2838*10**(-3)
    i1=-1.0981*10**(-5)
    i2=-1.6078*10**(-6)
    j0=1.91075*10**(-4)
    k0=8.50935*10**(-5)
    k1=-6.12293*10**(-6)
    k2=5.2787*10**(-8)
    m0=-9.9348*10**(-7)
    m1=2.0816*10**(-8)
    m2=9.1697*10**(-10)
    A1 = h0+h1*T+h2*T**2+h3*T**3
    A2 = A1 + (i0+i1*T+i2*T**2)*S+j0*S**(3/2)
    B1 = k0+k1*T+k2*T**2
    B2 = B1 + (m0+m1*T+m2*T**2)*S
    P = h/10
    return K0 + A2*P + B2*P**2
#OVISNOST O TEMPERATURI ZA FIKSNI S = 35 i P = 0.1 bar (h = 1 m):
T0 = -1.8 #otprilike točka zamrzavanja morske vode, u °C
h = 1 #metara, dubina
RO1_L = []  #ove liste uzimaju vrijednosti gustoće za različite temperature
RO2_L = []
RO3_L = []
RO4_L = []
RO5_L = []
RO6_L = []
RO7_L = [] #ova lista će uzeti podatke za S = 0
T_L = [] #ova lista će ispuniti vrijednosti temperature od T0 do cca. 30°C u koracima od 0.01°C
K1_L = [] #ova lista uzima vrijednosti K za sve temperature iz liste T_L
K2_L = []
K3_L = []
K4_L = []
K5_L = []
K6_L = []
K7_L = [] #ova lista će uzeti podatke za S = 0
RO1 = [] #ove liste pune konačne vrijednosti gustoće za sve temperature redom iz T_L
RO2 = []
RO3 = []
RO4 = []
RO5 = []
RO6 = []
RO7 = [] #ova lista će uzeti podatke za S = 0
#punim listu T_L temperaturama od T0 do cca 30°C u koracima od 0.01°C
for i in range(0,3200):
    T_L.append(T0+i*0.01)
#za svaki član u T_L redom računamo ro1 za različite salinitete u rasponu od 32 do 37 g/kg
for i in T_L:
    RO1_L.append(ro1(i,35))
    RO2_L.append(ro1(i,32))
    RO3_L.append(ro1(i,33))
    RO4_L.append(ro1(i,34))
    RO5_L.append(ro1(i,36))
    RO6_L.append(ro1(i,37))
    RO7_L.append(ro1(i,0))
#za svaki član u T_L redom računamo K za različite salinitete u rasponu od 32 do 37 g/kg
for i in T_L:
    K1_L.append(K(i,35,1))
    K2_L.append(K(i,32,1))
    K3_L.append(K(i,33,1))
    K4_L.append(K(i,34,1))
    K5_L.append(K(i,36,1))
    K6_L.append(K(i,37,1))
    K7_L.append(K(i,0,1))
#pomoću izračunatih ro1 i K,te pomoću tlaka kojeg smo fiksirali dubinom h = 1, računamo gustoće za različite temperature pri fiksiranim salinitetima
for i in range(0,3200):
    RO1.append(RO1_L[i]/(1-(h/10)/K1_L[i]))
    RO2.append(RO2_L[i]/(1-(h/10)/K2_L[i]))
    RO3.append(RO3_L[i]/(1-(h/10)/K3_L[i]))
    RO4.append(RO4_L[i]/(1-(h/10)/K4_L[i]))
    RO5.append(RO5_L[i]/(1-(h/10)/K5_L[i]))
    RO6.append(RO6_L[i]/(1-(h/10)/K6_L[i]))
    RO7.append(RO7_L[i]/(1-(h/10)/K7_L[i]))
plt.plot(T_L,RO1)
plt.plot(T_L,RO2)
plt.plot(T_L,RO3)
plt.plot(T_L,RO4)
plt.plot(T_L,RO5)
plt.plot(T_L,RO6)
plt.plot(T_L,RO7)
#crtamo grafove ovisnosti gustoće o temperaturi na dubini h = 1 m, za nekoliko različitih fiksnih iznosa saliniteta
plt.title("Ovisnost gustoće morske vode o temperaturi pri različitim salinitetima na dubini h = 1 m")
plt.legend(["S = 35","S = 32","S = 33","S = 34","S = 36","S = 37","S = 0"])
plt.xlabel("T [°C]")
plt.ylabel("gustoća [kg/m^3]")
plt.show()
#

