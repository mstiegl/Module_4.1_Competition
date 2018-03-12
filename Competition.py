import matplotlib.pyplot as plt


BTS_population= 15
BTS_birth_fraction = 1
BTS_births = BTS_birth_fraction * BTS_population
BTS_death_proportionality_constant = 0.20
WTS_population= 20
BTS_deaths = (BTS_death_proportionality_constant*WTS_population)*BTS_population
WTS_birth_fraction = 1
WTS_births = WTS_population * WTS_birth_fraction
WTS_death_proportionality_constant = 0.27
WTS_deaths=WTS_death_proportionality_constant * BTS_population*WTS_population
t=0
dt=0.001
simLength=5
numiterations=int(simLength/dt)+1
time=[t]
BTSLst=[BTS_population]
WTSLst=[WTS_population]
for i in range(1,numiterations):
    t=i*dt
    BTS_population=BTS_population+BTS_births*dt-BTS_deaths*dt
    WTS_population=WTS_population+WTS_births*dt-WTS_deaths*dt
    time.append(t)
    BTSLst.append(BTS_population)
    WTSLst.append(WTS_population)
    BTS_births = BTS_birth_fraction * BTS_population
    BTS_deaths = (BTS_death_proportionality_constant * WTS_population) * BTS_population

    WTS_births = WTS_population * WTS_birth_fraction
    WTS_deaths = (WTS_death_proportionality_constant * BTS_population) * WTS_population

print('Time(month)\tWTS\tBTS\n\n')
for i in range(1,6):

        print('%5.3f\t%5.2f\t%5.2f\n' % (time[i*1000], WTSLst[i*1000], BTSLst[i*1000]))
plt.plot(time,BTSLst, color='red')
plt.text(4,10,'BTS', color='red')
plt.plot(time,WTSLst,color='blue')
plt.text(1,7,'WTS',color='blue')
plt.xlabel('Time (months)')
plt.ylabel('Population')
plt.title('Competition between Whitetip Sharks (WTS) and Blacktip Sharks (BTS)')
plt.show()
outfile = open("sharkcompetition.dat", 'w')
for i in range(numiterations):
    outfile.write("%6.3f\t%12.2f\t%12.2f\n" % (time[i], WTSLst[i], BTSLst[i]))
outfile.close()
