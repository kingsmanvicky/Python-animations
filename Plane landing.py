import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import numpy as np


# Creating  the time array
t0 = 0 #[Secs]
t_end = 10 #[Secs]
dt = 0.02 #[Secs]
t = np.arange(t0,t_end+dt,dt)

# Creating x-array
x_i = 1000 #[m]
a = 200
x = x_i + a*t


# Creating y array
y_i = 1500
b = -100
y = y_i + b*t



############################ ANIMATION ############################

frame_amount = len(t)


def update_plot(num):
    #Plane movement
    plane_1.set_data([x[num]-40,x[num]+20],[y[num]-0,y[num]+0])
    plane_2.set_data([x[num]-15,x[num]+10],[y[num]-0,y[num]+0])
    plane_3.set_data([x[num]-45,x[num]-30],[y[num]+80,y[num]])
    plane_4.set_data([x[num]-65,x[num]-40],[y[num],y[num]])  

    #Plane Trajectory
    plane_trajectory.set_data(x[0:num],y[0:num])

    #positional vectors
    pos_x.set_data(t[0:num],x[0:num])
    pos_y.set_data(t[0:num],y[0:num])

    #Arrows for Vector representation
    arrow_change = ax0.arrow(0,0,x[num],y[num],length_includes_head = True, head_length= 80, head_width=40, color='g', linewidth=2)
    arrow_rest = ax0.arrow(0,0,x_i,y_i,length_includes_head = True, head_length= 80, head_width=40, color='g', linewidth=2)
    arrow_disp = ax0.arrow(x_i,y_i,x[num]-x_i,y[num]-y_i,length_includes_head = True, head_length= 80, head_width=40, color='purple', linewidth=2)
    arrow_x = ax0.arrow(x_i,y_i,x[num]-x_i,0,length_includes_head = True, head_length= 80, head_width=40, color='r', linewidth=2)
    arrow_y = ax0.arrow(x[num],y_i,0,y[num]-y_i,length_includes_head = True, head_length= 80, head_width=40, color='b', linewidth=2)
    arrow_x_pos = ax1.arrow(t[num],x_i,0,x[num]-x_i,length_includes_head = True, head_length= 100, head_width=0.2, color='r', linewidth=2)
    arrow_y_pos = ax2.arrow(t[num],y_i,0,y[num]-y_i,length_includes_head = True, head_length= 100, head_width=0.2, color='b', linewidth=2)

    return plane_1,plane_2,plane_3,plane_4,plane_trajectory,pos_y,pos_x,arrow_change,arrow_rest,arrow_disp,arrow_x,arrow_y,arrow_x_pos,arrow_y_pos


#Setting up the figure properties
fig = plt.figure(figsize=(16, 9), dpi = 80, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(2,2)


#Airplane motion
ax0 = fig.add_subplot(gs[0,:],facecolor= (1,1,1))


#Drawing the airplane
plane_1, = ax0.plot([],[],'k',linewidth = 10)
plane_2, = ax0.plot([],[],'k',linewidth = 5)
plane_3, = ax0.plot([],[],'k',linewidth = 4)
plane_4, = ax0.plot([],[],'k',linewidth = 3)


plane_trajectory, = ax0.plot([],[],"--k",linewidth= 2)


plt.xlim(0,max(x))
plt.ylim(0,max(y)+100)
plt.xlabel("position_x [m]",fontsize = 15)
plt.ylabel("position_y [m]",fontsize = 15)
plt.grid(True)


#Position X vs time
ax1 = fig.add_subplot(gs[1,0],facecolor=(1,1,1))
pos_x, = ax1.plot([],[],"-b",linewidth=3,label="X = "+str(x_i)+ " + ("+str(a)+")t")
plt.xlim(0,t_end)
plt.ylim(0,max(x))
plt.xlabel("time [s]", fontsize=15)
plt.ylabel("position_x [m]", fontsize=15)
plt.grid(True)
plt.legend(loc='lower right', fontsize='x-large')


#Creating Y vs time
ax2 = fig.add_subplot(gs[1,1],facecolor=(1,1,1))
pos_y, = ax2.plot([],[],"-b",linewidth=3,label="Y = "+str(y_i)+ " + ("+str(b)+")t")
plt.xlim(0,t_end+dt)
plt.ylim(0,max(y)+100)
plt.xlabel("time [s]", fontsize=15)
plt.ylabel("position_y [m]", fontsize=15)
plt.grid(True)
plt.legend(loc='lower right', fontsize='x-large')


plane_ani = animation.FuncAnimation(fig,update_plot,frames = frame_amount,interval = 20, repeat = True, blit = True)
plt.show()








