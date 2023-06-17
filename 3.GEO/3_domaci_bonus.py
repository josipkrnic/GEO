import numpy as np
import matplotlib.pyplot as plt
#U ovom kodu istražujemo limit jednadžbe stanja
#pogledat ćemo kako se gustoća mijenja za veće raspone temperature pri S = konst i za veće raspone saliniteta pri T = konst
#gustoća bi se trebala smanjivati pri povećanju temperature, a povećavati povećavanjem saliniteta, pa idemo vidjtei do kojih vrijednosti je to ispunjeno
def funkcija(f,x):
    return f(x)
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
#koeficijenti K
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
T0 = -20 #početna promatrana temperatura
S0 = 0 #početni promatrani salinitet
h = 1 #dubina je fiksirana, h = 1 m
RO1 = [] #tražimo iznose ro1 za različite T
RO2 = [] #tražimo iznose ro1 za različite S
K1 = [] #tražimo K za različite T
K2 = [] #tražimo K za različite S
TEM = [] #lista temperatura, redom od T0 do 120 °C
SAL = [] #lista saliniteta, od S0 do apsurdno visokog S, nešto ala 10000 g/kg
RO_1 = [] #konačna lista gustoća u ovisnosti o T
RO_2 = [] #konačna lista gustoća u ovisnosti o S
#u forovima punimo liste gore navedenim podacima
for i in range(0,110):
    TEM.append(T0+i*1.3)
    SAL.append(S0+100*i)
for i in TEM:
    RO1.append(ro1(i,35))
for i in SAL:
    RO2.append(ro1(20,i))
for i in TEM:
    K1.append(K(i,35,1))
for i in SAL:
    K2.append(K(20,i,1))
for i in range(0,110):
    RO_1.append(RO1[i]/(1-(h/10)/K1[i]))
    RO_2.append(RO2[i]/(1-(h/10)/K1[i]))
plt.plot(TEM,RO_1)
plt.title("Ovisnost gustoće o temperaturi")
plt.xlabel("T [°C]")
plt.ylabel("gustoća [kg/m^3]")
plt.show()
plt.plot(SAL,RO_2)
plt.title("Ovisnost gustoće o salinitetu, T = 20 °C")
plt.xlabel("S [g/kg]")
plt.ylabel("gustoća [kg/m^3]")
plt.show()
#može se vidjeti da na oko 90 °C iznos gustoće više ne pada povećanjem temperature, ima minimum u toj točki i gustoća počinje naglo rasti
#dakako, na T > 100 °C voda prelazi u plinovito stanje gustoće mnogo manje od tekuće vode
#jednadžba stanja, dakle, prestaje funkcionirati na temperaturama bliskim temperaturi vrelišta vode
#ispod točke ledišta vidimo da se gustoća nastavlja kontinuirano mijenjati, nema prekida, što je nefizikalno s obzirom da postoji pad gustoće leda u odnosu na vodu
#za čistu vodu taj je skok oko 100 kg/m^3, a daljnjim hlađenjem gustoća leda raste, što opet nije uočeno na ovom grafu
#dapače, gustoća nastavlja monotono padati, pa jednadžba ne funkcionira za zaleđenu vodu
#što se tiče saliniteta, gustoća vode cijelo vrijeme raste povećanjem saliniteta
#čak i kad smo uzeli ogroman raspon za S, jednadžba stanja je i dalje isključivo rastuća funkcija
#po tome bi rekli da jednadžba stanja ima dovoljno visoku toleranciju na velike raspone saliniteta, da možemo tvrditi kako vrijedi za bilo koju vrijednost S
#međutim, takve koncentracije soli su praktično nemoguće

