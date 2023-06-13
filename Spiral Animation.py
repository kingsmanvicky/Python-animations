import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np


#Creating the time array
t0 = 0 #[secs]
t_end = 10 #[secs]
dt = 0.02 #[secs]
t = np.arange(t0,t_end+dt,dt)


#Creating arrays for x and y dimensions
r = 3
f = 1
x = r*np.cos(2*np.pi*f*t)
y = r*np.sin(2*np.pi*f*t)


#Creating array for z dimension
z = t


###################### ANIMATION ######################
frame_amount  = len(t)


def update_plot(num):
    #Trajectory
    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_trajectory.set_3d_properties(z[0:num])

    #Positional Vectors
    pos_x.set_data(t[0:num],x[0:num])
    pos_y.set_data(t[0:num],y[0:num])
    pos_z.set_data(t[0:num],z[0:num])

    return plane_trajectory,pos_x,pos_y,pos_z


fig = plt.figure(figsize=(16, 9), dpi = 80, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(3,4)


#3D motion
ax0 = fig.add_subplot(gs[:,0:3], projection = '3d', facecolor = (1,1,1))
plane_trajectory, = ax0.plot([],[],[], 'r', linewidth = 4, label="Motion trajectory")
ax0.set_xlim(min(x),max(x))
ax0.set_ylim(min(y),max(y))
ax0.set_zlim(min(z),max(z))
ax0.set_xlabel('position_x [m]', fontsize = 12)
ax0.set_ylabel('position_y [m]', fontsize = 12)
ax0.set_zlabel('position_z [m]', fontsize = 12)
plt.grid(True)
plt.legend(loc='upper left', fontsize='large')


#Plot for x dimension
ax1 = fig.add_subplot(gs[0,3],facecolor = (1,1,1))
pos_x, = ax1.plot([],[],'b',linewidth=2,label=f'x = {r}cos(2π{f}t)')
plt.xlim(t0,t_end)
plt.ylim(min(x),max(x))
plt.yticks([-5,0,5])
plt.xticks([0,2,4,6,8,10])
plt.ylabel("position_x [m]",fontsize=12)
plt.legend(loc="lower right", fontsize='small')
plt.grid(True)


#Plot for y dimension
ax2 = fig.add_subplot(gs[1,3],facecolor = (1,1,1))
pos_y, = ax2.plot([],[],'b',linewidth=2,label=f'y = {r}sin(2π{f}t)')
plt.xlim(t0,t_end)
plt.ylim(min(y),max(y))
plt.yticks([-5,0,5])
plt.xticks([0,2,4,6,8,10])
plt.ylabel("position_y [m]",fontsize=12)
plt.legend(loc="lower right", fontsize='small')
plt.grid(True)


#Plot for z dimension
ax3 = fig.add_subplot(gs[2,3],facecolor = (1,1,1))
pos_z, = ax3.plot([],[],'b',linewidth=2,label="z = t")
plt.xlim(t0,t_end)
plt.ylim(min(x),max(y))
plt.yticks([0,2,4,6,8,10])
plt.xticks([0,2,4,6,8,10])
plt.ylabel("position_z [m]",fontsize=12)
plt.xlabel("time [secs]",fontsize=12)
plt.legend(loc="lower right", fontsize='small')
plt.grid(True)


plane_ani = animation.FuncAnimation(fig,update_plot,frames = frame_amount,interval = 20, repeat = True, blit = True)
plt.show()