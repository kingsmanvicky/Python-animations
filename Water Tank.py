#Importing the required packages
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec  
import numpy as np


#Time array
t0 = 0 #[sec]
dt = 0.04 #[sec]
t_end = 60 #[sec]
t = np.arange(t0,t_end+dt,dt)


#Functions for the Tanks
#Zero Arrays for Tank 1,2,3
volume_Tank1 = np.zeros(len(t))
volume_Tank2 = np.zeros(len(t))
volume_Tank3 = np.zeros(len(t))


#Creating values for Tanks 
#Tank1
for i in range(len(t)):
    if t[i] <=22.5:
        volume_Tank1[i] = 50+(2*t[i])
    elif t[i] <= 32.5:
        volume_Tank1[i] = 95
        temp11 = i
    elif t[i] <= (32.5 + (45**0.5)):
        volume_Tank1[i] = 95 - ((t[i]-t[temp11])**2)
        temp12 = i
    elif t[i] <= (42.5 + (45**0.5)):
        volume_Tank1[i] = 50 + (np.sin(2*np.pi*(t[i]-t[temp12])))
    else:
        volume_Tank1[i] = 50


#Tank 2
for i in range(len(t)):
    if t[i] <= 27.5:
        volume_Tank2[i] = 40 + 2*t[i]
        temp21 = i
    elif t[i] <= 32.5:
        volume_Tank2[i] = 95 
        temp22 = i
    elif t[i] <= (32.5 + (45**0.5)):
        volume_Tank2[i] = 95 - ((t[i]-t[temp22])**2)
        Temp23 = i
    elif t[i] <= (37.5 + (45**0.5)):
        volume_Tank2[i] = 50 + 3*np.sin(2*np.pi*(t[i] - t[Temp23]))
        Temp24 = i
    elif t[i] <= (42.5 + (45**0.5)):
        volume_Tank2[i] = 50 + np.sin(2*np.pi*2*(t[i] - t[Temp24]))
    else:
        volume_Tank2[i] = 50


#Tank 3:
for i in range(len(t)):
    if t[i] <= 32.5:
        volume_Tank3[i] = 30 + (2*t[i])
        temp31 = i
    elif t[i] <= (32.5 + (45**0.5)):
        volume_Tank3[i] = 95 - ((t[i] - t[temp31])**2)
        temp32 = i
    elif t[i] <= (42.5 + (45**0.5)):
        volume_Tank3[i] = 50 - np.sin(2*np.pi*(t[i] - t[temp32]))
    else:
        volume_Tank3[i] = 50


##################### ANIMATION #####################
frame_amount = len(t)


#Creating Water Tank 
radius = 5 #[m]
volume_i = 0 #[m^3]
volume_f = 100 #[m^3]
dVol = 10


def update_plot(num):
    #Tank 1:
    tank_1.set_data([-radius,radius],[volume_Tank1[num],volume_Tank1[num]])
    tank_12.set_data([0,0],[-145,volume_Tank1[num]-105])
    tnk_1.set_data(t[0:num],volume_Tank1[0:num])
    tnk_1z.set_data(t[0:num],volume_Tank1[0:num])


    #Tank 2:
    tank_2.set_data([-radius,radius],[volume_Tank2[num],volume_Tank2[num]])
    tank_22.set_data([0,0],[-145,volume_Tank2[num]-105])
    tnk_2.set_data(t[0:num],volume_Tank2[0:num])
    tnk_2z.set_data(t[0:num],volume_Tank2[0:num])


    #Tank 3:
    tank_3.set_data([-radius,radius],[volume_Tank3[num],volume_Tank3[num]])
    tank_32.set_data([0,0],[-145,volume_Tank3[num]-105])
    tnk_3.set_data(t[0:num],volume_Tank3[0:num])
    tnk_3z.set_data(t[0:num],volume_Tank3[0:num])


    return tank_12,tank_1,tank_22,tank_2,tank_32,tank_3,tnk_1,tnk_2,tnk_3,tnk_1z,tnk_2z,tnk_3z


fig = plt.figure(figsize=(16,9), dpi = 80, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(2,3)


#Tank-1:
ax1 = fig.add_subplot(gs[0,0], facecolor = (1,1,1))
tank_1, = ax1.plot([],[],'r',linewidth = 4)
tank_12, = ax1.plot([],[],'royalblue', linewidth = 500)
plt.xlim(-radius, radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel("Tank Volume [m^3]")
plt.title("Tank 1")


#Tank -2:
ax2 = fig.add_subplot(gs[0,1], facecolor = (1,1,1))
tank_2, = ax2.plot([],[],'r',linewidth = 4)
tank_22, = ax2.plot([],[],'royalblue', linewidth = 500)
plt.xlim(-radius, radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.title("Tank 2")


#Tank-3:
ax3 = fig.add_subplot(gs[0,2], facecolor = (1,1,1))
tank_3, = ax3.plot([],[],'r',linewidth = 4)
tank_32, = ax3.plot([],[],'royalblue', linewidth = 500)
plt.xlim(-radius, radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.title("Tank 3")


#Creating Volume Subplot:
ax4 = fig.add_subplot(gs[1,0:2],facecolor = (1,1,1))
tnk_1, = ax4.plot([],[],'blue',linewidth=3,label="Tank-1")
tnk_2, = ax4.plot([],[],'green',linewidth=3,label="Tank-2")
tnk_3, = ax4.plot([],[],'red',linewidth=3,label="Tank-3")
plt.xlim(t0,t_end)
plt.ylim(volume_i,volume_f)
plt.xticks([0,22.5,27.5,32.5,32.5+(45**0.5),37.5+(45**0.5),42.5+(45**0.5),60])
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.xlabel("Time [sec]")
plt.ylabel("Tank Volume [m^3]")
plt.legend(loc="upper right")
plt.grid(True)


#Creating Zoomed Subplot:
ax5 = fig.add_subplot(gs[1,2],facecolor=(1,1,1))
tnk_1z, = ax5.plot([],[],"blue",linewidth=3)
tnk_2z, = ax5.plot([],[],"green",linewidth=3)
tnk_3z, = ax5.plot([],[],"red",linewidth=3)
plt.xticks([0,22.5,27.5,32.5,32.5+(45**0.5),37.5+(45**0.5),42.5+(45**0.5),60])
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.axis([38,50,47,53])
plt.grid(True)
plt.xlabel("Time [sec]")


ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()






