import numpy as np
import matplotlib.pyplot as plt
#ANTICIKLONA
#i za C i A su uzeti mali prostorni rasponi (5 km u svakom smjeru) jer bi derivacije trebale biti što točnije, međutim iznosi vektora vjetra bi svakako bili jednaki jer je jednoliki gradijent
#u suštini je bilo svejedno, međutim uzet ćemo ipak manji prostor da bi se više približili realnoj situaciji
Z01 = 540 #gpm
dZ1 = 0.001 #gpm/0.1km
ro = 1.27 #gustoca zraka
fi = 45 #zemljopisna sirina
g = 9.81 #gravitacijsko ubrzanje
f = 2*2*np.pi/(24*3600)*np.sin(np.pi/180*fi) #Coriolisov parametar
dx = 0.1 #mali korak u x smjeru, u km
dy = 0.1 #mali korak u y smjeru, ukm
x = np.linspace(-2.5,2.5,51) #granice područja u x [km]
y = np.linspace(-2.5,2.5,51) #granice područja u y [km]
X,Y = np.meshgrid(x,y)
Z1 = Z01 + np.sqrt(X**2 + Y**2)*dZ1 #prostorna promjena geopotencijalne visine
u = (g/(ro*f))*np.sqrt((dZ1/dx)**2+(dZ1/dy)**2)*(Y/np.sqrt(0.001+X**2+Y**2)) #formule izvedene za komponente brzine u priloženoj slici
v = -(g/(ro*f))*np.sqrt((dZ1/dx)**2+(dZ1/dy)**2)*(X/np.sqrt(0.001+X**2+Y**2))
#dalje je sve crtanje
h = plt.contourf(x,y,Z1)
plt.axis("Scaled")
plt.colorbar()
plt.quiver(X,Y,u,v)
plt.title("Anticiklona; p = 500 hPa, Z0 = 540 gpm")
plt.show()
#CIKLONA
#sve potpuno analogno 
Z02 = 580 #gpm
dZ2 = 0.0004 #gpm/0.1km
x1 = np.linspace(-2.5,2.5,51)
y1 = np.linspace(-2.5,2.5,51)
X1,Y1 = np.meshgrid(x1,y1)
Z2 = Z02 - np.sqrt(X1**2 + Y1**2)*dZ2
uC = -(g/(ro*f))*np.sqrt((dZ2/dx)**2+(dZ2/dy)**2)*(Y1/np.sqrt(0.001+X1**2+Y1**2))
vC = (g/(ro*f))*np.sqrt((dZ2/dx)**2+(dZ2/dy)**2)*(X1/np.sqrt(0.001+X1**2+Y1**2))
h = plt.contourf(x1,y1,Z2)
plt.axis("Scaled")
plt.colorbar()
plt.quiver(X1,Y1,uC,vC)
plt.title("Ciklona; p = 500 hPa, Z0 = 580 gpm")
plt.show()
#BONUS: model koji koristimo je vrlo simplističan i podrazumijeva savršenu radijalnu i azimutalnu simetriju, što je vrlo različito od stvarnih uvjeta. Ova se simetrija možda
#može približno postići na manjim prostornim skalama, a na malo većim vjerojatno i dalje imamo jednosmjerne gradijente tlaka, no oni će biti različitih iznosa
#za iste radijalne udaljenosti u različitim smjerovima (koji bi odgovarali različitim kutevima otklona od npr. x osi kako ju postavimo u danom problemu
