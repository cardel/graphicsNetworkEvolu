#!/usr/bin/python
# -*- coding: utf-8 -*- 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
plt.rc('xtick',labelsize=8)
plt.rc('ytick',labelsize=8)


#Caso SWHD
#Iteracion
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

#Fitness
z = np.array([99646.032808169,99235.502164121,98875.399009859,98425.205582876,98130.616472437,97785.388758847,97417.462089274,97185.274775199,96969.941089948,96753.131315654,96433.141631098,96201.507682763,95935.045834382,95802.643728529,95579.592337399,95407.463737012,95197.24856396,94999.924382788,94861.068252584,94675.485664479,94589.97939282,94430.625464838,94306.765079482,94128.447481065,93911.453980429,93793.433819756,93672.954783801,93488.146693081,93459.799714687,93375.169998232])

#Tiempo
y = np.array([3.658422319,6.976918109,10.254235633,13.449950322,16.634001366,19.757345955,22.834210006,25.95183123,29.054594994,32.077502147,35.123346289,38.170334617,41.180718954,44.197970851,47.169401352,50.140859604,53.097373303,56.023112456,58.919787383,61.797380265,64.641855677,67.493434381,70.362946868,73.177232424,75.975950567,78.742295162,81.477358905,84.190503597,86.910240936,89.622349421
])
x, y = np.meshgrid(x, y)

fig = plt.figure()

ax = fig.add_subplot(2, 2, 1, projection='3d')


surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="SWHD")

plt.xlabel(u"Iteración")
plt.ylabel(u"Tiempo")                       
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_title(u'Estrategias swbest', fontsize=8)

#Caso 

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])


z = np.array([100918.033524684,100388.626964509,100153.79229063,99930.38945284,99582.349635819,99426.361887363,99140.968924206,99015.795492742,98945.719345807,98720.412863641,98546.809562623,98360.916148789,98234.535120412,98090.486676437,97911.235038923,97811.328957576,97534.210594072,97363.170341245,97264.838009173,97206.424978577,97063.488151268,96973.794696637,96864.304869617,96707.167846955,96630.627472401,96500.642505817,96432.43595928,96384.19698432,96343.621016465,96173.754753118
])

y = np.array([2.281238468,4.253087489,6.117812904,7.927325988,9.74482952,11.561011259,13.330645283,15.10891726,16.855074867,18.591956687,20.312925998,22.060356236,23.788479265,25.526012015,27.2389141,28.939389849,30.633545478,32.33978742,34.045022821,35.74575731,37.421279565,39.114448325,40.790491835,42.461328745,44.116144188,45.770512144,47.416744145,49.04854025,50.678647765,52.309863162])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 2, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración")
plt.ylabel(u"Tiempo")
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia swhd', fontsize=8)

# Add a color bar which maps values to colors.
fig.colorbar(surf2, shrink=0.5, aspect=5)


#otra swnormal

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

z= np.array([100045.944600848,99695.831537613,99512.190803115,99201.996806392,98779.64429622,98595.141006234,98315.473648711,98213.461306091,97833.507161989,97612.723376706,97415.666179756,97329.606358593,97076.432272277,96927.415949351,96691.347703393,96508.919074008,96367.826250439,96207.596172892,96143.765636242,96061.360301031,95998.355471348,95943.475316326,95806.06952913,95727.168328156,95522.143156643,95422.485309696,95357.351564262,95267.319022983,95113.965182167,95042.923203518])

y = np.array([2.174092166,4.047870223,5.844731061,7.592200073,9.327517899,11.062993717,12.743191727,14.411852956,16.097949489,17.785171159,19.458837763,21.117509548,22.782094407,24.401054708,26.029655409,27.689281042,29.33205936,30.977367091,32.60224851,34.224814995,35.82318906,37.410660028,38.999307831,40.581835365,42.168468936,43.788039374,45.400040205,46.967855239,48.553460614,50.109408545])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 3, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración")
plt.ylabel(u"Tiempo")
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia sw normal', fontsize=8)


# Add a color bar which maps values to colors.
fig.colorbar(surf2, shrink=0.5, aspect=5)

#otra evolutivo

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

z = np.array([101428.520536777,100987.479238551,100506.654887197,100233.853770325,99836.559892355,99392.480097403,99081.198298662,98986.859289138,98794.528668633,98521.314698689,98333.222316939,98174.176274507,97981.412013223,97843.88900947,97680.280308063,97632.296557454,97401.782375038,97319.768445681,97057.771637553,96911.448733607,96931.947382403,96896.323061962,96734.78337851,96649.775256499,96554.870784714,96438.000464863,96281.886979743,96234.804180623,96240.968336441,96224.031623923])

y = np.array([2.809194374,4.764719375,6.741292254,8.694867452,10.658479508,12.621612287,14.596862181,16.587040695,18.58237052,20.559694179,22.546626918,24.521742304,26.50718739,28.487675714,30.467522025,32.446237191,34.444327593,36.415741539,38.398682849,40.371106275,42.354654876,44.335875456,46.319547073,48.308977159,50.294097074,52.279476007,54.249211629,56.225939123,58.205360889,60.179563427
])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 4, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración")
plt.ylabel(u"Tiempo")
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia evolutiva', fontsize=8)

# Add a color bar which maps values to colors.
fig.colorbar(surf2, shrink=0.5, aspect=5)

plt.savefig("color.png")
