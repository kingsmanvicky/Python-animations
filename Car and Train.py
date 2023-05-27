#Importing the required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec  


#Initial Values
#Time array
t0 = 0 #[sec]
t_end = 16 #[sec]
dt = 0.02 #[sec]
t = np.arange(t0, t_end+dt, dt)


#Arrays for motion
#Required Functions for green and purple car


#Blue train:
f1 = 0.125 #[Hz]
A1 = 7 #[m]
train_blue = A1*np.sin(2*np.pi*f1*t)


#Red train:
f2 = 0.125 #[Hz]
A2 = -7 #[m]
train_red = A2*np.cos(2*np.pi*f2*t)


#Cars:
y_i = 13
car_green = y_i - 2*(t-2)**2
car_purple = y_i - 2*(t-6)


################ ANIMATION ################
frame_amount = len(t)


def update_plot(num):
    #Subplot 1
    x_blue.set_data(t[0:num],train_blue[0:num])
    x_red.set_data(t[0:num],train_red[0:num])

    #Subplot 2&3
    block_blue.set_data([train_blue[num]-0.45,train_blue[num]+0.45],[3.5,3.5])
    block_red.set_data([train_red[num]-0.45,train_red[num]+0.45],[1.5,1.5])


    if t[num]>=2:
        block_green.set_data([3.5,3.5],[car_green[num]-0.5,car_green[num]+0.5])
        y_green1.set_data(t[int(2/dt):num],car_green[int(2/dt):num])
    else:
        block_green.set_data([3.5,3.5],[y_i-0.5,y_i+0.5])
        y_green2.set_data(t[0:num],y_i)
   
    
    if t[num]>=6:
        block_purple.set_data([-3.5,-3.5],[car_purple[num]-0.5,car_purple[num]+0.5]) 
        y_purple1.set_data(t[int(6/dt):num],car_purple[int(6/dt):num])   
    else:
        block_purple.set_data([-3.5,-3.5],[y_i-0.5,y_i+0.5])
        y_purple2.set_data(t[0:num],y_i)


    return x_blue,x_red,block_blue,block_red,block_green,y_green1,y_purple1,y_purple2,block_purple,y_green2


fig = plt.figure(figsize=(16, 9), dpi = 80, facecolor = (0.9,0.9,0.9))
gs = gridspec.GridSpec(2,2)


#Subplot 1
ax1 = fig.add_subplot(gs[0,0], facecolor=(0.9,0.9,0.9))
x_blue, = ax1.plot([], [], 'b', linewidth = 3, label = "X_blue = " + str(A1) + "*sin(2π" + str(f1) + "*t)")
x_red, = ax1.plot([], [], 'r', linewidth = 3, label = "X_red = " + str(A2) + "*cos(2π" + str(f2) + "*t)")
plt.xlim(t0,t_end)
plt.ylim(-max(A1,A2)-1,max(A1,A2)+1)
plt.xlabel("Time [sec]")
plt.ylabel("X [m]")
plt.grid(True)
ax1.spines['bottom'].set_position("center")
ax1.xaxis.set_label_coords(0.5,-0.05)
plt.legend(bbox_to_anchor=(1,1.2),fontsize = 'medium')


#Subplot 2
ax2 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
y_green1, = ax2.plot([], [], "g",linewidth =3)
y_green2, = ax2.plot([], [], "g",linewidth =3)
y_purple1, = ax2.plot([], [], "m",linewidth =5)
y_purple2, = ax2.plot([], [], "m",linewidth =5)
plt.xlim(t0,t_end)
plt.ylim(-2,y_i+1)
plt.xlabel("Time [sec]")
plt.ylabel("Y [m]")
plt.grid(True)
ax2.spines['bottom'].set_position('zero')
ax2.xaxis.set_label_coords(0.5,-0.05)


#Subplot 3
ax3 = fig.add_subplot(gs[:,1], facecolor=(0.9,0.9,0.9))
ax3.spines['left'].set_position("zero")
ax3.spines['bottom'].set_position("zero")
plt.grid(True)
block_blue, = ax3.plot([], [], "b",linewidth=28)
block_red,  = ax3.plot([], [], "-r",linewidth=28)
block_green, = ax3.plot([], [], "-g",linewidth=24)
block_purple, = ax3.plot([], [], "purple",linewidth=24)


#Creating Danger zone(Collision Zone) 1
danger_zone_1, = ax3.plot([3,4], [1,1], "-k",linewidth=3)
danger_zone_2, = ax3.plot([3,4], [2,2], "-k",linewidth=3)
danger_zone_3, = ax3.plot([3,3], [1,2], "-k",linewidth=3)
danger_zone_4, = ax3.plot([4,4], [1,2], "-k",linewidth=3)


#Creating Danger zone(Collision Zone) 2
danger_zone_1, = ax3.plot([3,4], [3,3], "-k",linewidth=3)
danger_zone_2, = ax3.plot([3,4], [4,4], "-k",linewidth=3)
danger_zone_3, = ax3.plot([3,3], [3,4], "-k",linewidth=3)
danger_zone_4, = ax3.plot([4,4], [3,4], "-k",linewidth=3)


#Creating Danger zone(Collision Zone) 3
danger_zone_1, = ax3.plot([-3,-4], [1,1], "-k",linewidth=3)
danger_zone_2, = ax3.plot([-3,-4], [2,2], "-k",linewidth=3)
danger_zone_3, = ax3.plot([-3,-3], [1,2], "-k",linewidth=3)
danger_zone_4, = ax3.plot([-4,-4], [1,2], "-k",linewidth=3)


#Creating Danger zone(Collision Zone) 4
danger_zone_1, = ax3.plot([-3,-4], [3,3], "-k",linewidth=3)
danger_zone_2, = ax3.plot([-3,-4], [4,4], "-k",linewidth=3)
danger_zone_3, = ax3.plot([-3,-3], [3,4], "-k",linewidth=3)
danger_zone_4, = ax3.plot([-4,-4], [3,4], "-k",linewidth=3)


bbox_green = dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g',lw=1)
bbox_purple = dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='purple',lw=1)
ax3.text(1.65,y_i+1.5,'green_car= '+str(int(y_i))+'-2(t-2)^2',size=10,color='g',bbox=bbox_green)
ax3.text(-6.25,y_i+1.5,'purple_car= '+str(int(y_i))+' -2(t-6)',size=10,color='purple',bbox=bbox_purple)


plt.xlim(-max(A1,A2)-1,max(A1,A2)+1)
plt.ylim(-2,y_i+1)
plt.xticks(np.concatenate([np.arange(-7-1,0,1),np.arange(1,7+2,1)]),size=10)
plt.yticks(np.concatenate([np.arange(-2,0,1),np.arange(1,y_i+1,1)]),size=10)


ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()