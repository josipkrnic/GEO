import matplotlib.pyplot as plt
#1. DAN 4. lipnja, 2023., jučer u odnosu na predani domaći, postaja Split-Marjan
T1 = [21.5,20.7,20.3,19.6,19.7,19.4,19.9,21.2,22,23.9,25.4,26,26.3,26.7,26.6,26.5,26.5,26,25,24.2,23.6,22.2,22,22.1,22]
#2. DAN 1. veljače, 2023, Split, meteo-info
T2 = [8,7.6,7.2,7,7.1,6.6,7.1,6.5,7.1,8.4,9.7,10.5,11.2,11.5,11.4,11,10.5,10.3,10.2,9.9,9.7,9.4,9,8.3,8.1]
#3. DAN 4. kolovoza, 2022., Split, meteo-info
T3 = [27,26,26.4,26,25,25.2,24.6,25.4,27,28.2,29.9,30.8,31.5,32.3,32.1,31.3,31.3,32,32.2,32.4,31.4,30.4,30,29.1,28.6]
#4. DAN 10.studenog, 2021., Split, meteo-info
T4 = [15,15.1,16,15,15.2,15.2,15.2,15,15.2,15.5,16.4,17.5,17.6,18.2,18.2,17.9,17.7,17.3,17,17.2,17.5,17.6,17.6,17,16.8]
h = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
plt.subplot(2,2,1)
plt.plot(h,T1)
plt.xlabel("t [h]")
plt.ylabel("T [°C]")
plt.title("Temperatura kroz dan 4. lipnja, 2023., Split-Marjan")
plt.subplot(2,2,2)
plt.plot(h,T2)
plt.xlabel("t [h]")
plt.ylabel("T [°C]")
plt.title("Temperatura kroz dan 1. veljače, 2023., Split")
plt.subplot(2,2,3)
plt.plot(h,T3)
plt.xlabel("t [h]")
plt.ylabel("T [°C]")
plt.title("Temperatura kroz dan 4. kolovoza, 2022., Split")
plt.subplot(2,2,4)
plt.plot(h,T4)
plt.xlabel("t [h]")
plt.ylabel("T [°C]")
plt.title("Temperatura kroz dan 10. studenog, 2021., Split")
plt.show()
