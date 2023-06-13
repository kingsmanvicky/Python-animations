import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import numpy as np


#Creating the time array
t0 = 0 #[secs]
t_end = 1 #[secs]
dt = 0.005 #[secs]
t = np.arange(t0,t_end+dt,dt)


#Creating x and y arrays for join 1
r1 = 4
f1 = 1 #[Hz]
alpha1 = 2*np.pi*f1*t
x1 = (r1)*np.cos(alpha1)
y1 = (r1)*np.sin(alpha1)


#Creating x and y arrays for joint 2
r2 = 3
f2 = 2 #[Hz]
alpha2 = 2*np.pi*f2*t #This is in wrt to first joint
dx1 = (r2)*np.cos(alpha2)
dy1 = (r2)*np.sin(alpha2)


#Creating x and y arrays for joint 3
r3 = 2
f3 = 3 #[Hz]
alpha3 = 2*np.pi*f3*t #This is in wrt to first joint
dx2 = (r2)*np.cos(alpha3)
dy2 = (r2)*np.sin(alpha3)


#With respect to reference axis
x2 = x1 + dx1 
y2 = y1 + dy1 
x3 = x2 + dx2
y3 = y2 + dy2   


########################### ANIMATION ###########################
frame_amount = len(t)


def update_plot(num):
    #Robot
    joint_1.set_data([0,x1[num]],[0,y1[num]])
    joint_2.set_data([x1[num],x2[num]],[y1[num],y2[num]])
    joint_3.set_data([x2[num],x3[num]],[y2[num],y3[num]])
    trajectory.set_data(x3[0:num],y3[0:num])


    #Joint1
    alpha1_funct.set_data(t[0:num],alpha1[0:num])


    #Joint2
    alpha2_funct.set_data(t[0:num],alpha2[0:num])


    #Joint3
    alpha3_funct.set_data(t[0:num],alpha3[0:num])


    return joint_1,joint_2,joint_3,trajectory,alpha1_funct,alpha2_funct,alpha3_funct


#Defining Figure properties
fig = plt.figure(figsize=(16,9), dpi = 80, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(3,3)
plt.subplots_adjust(left=0.03, top=0.97, right=0.99, bottom=0.065, hspace=0.2, wspace=0.15)


#Subplot1
ax1 = fig.add_subplot(gs[:,0:2], facecolor=(1,1,1))
base_line, =ax1.plot([0,0],[0,0.4],'k',linewidth=20)
joint_1, = ax1.plot([],[],'k',linewidth=4)
joint_2, =ax1.plot([],[],"b",linewidth=4)
joint_3, =ax1.plot([],[],"g",linewidth=4)
trajectory, =ax1.plot([],[],'r',linewidth=2)
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')
ax1.xaxis.set_label_coords(0.5,-0.01)
ax1.yaxis.set_label_coords(-0.002,0.5)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xticks(np.arange(-10,10+1,1))
plt.yticks(np.arange(-10,10+1,1))
plt.xlabel('meters [m]',fontsize=12)
plt.ylabel('meters [m]',fontsize=12)
plt.grid(True)


#Subplot 2
ax2 = fig.add_subplot(gs[0,2], facecolor=(1,1,1))
alpha1_funct, = ax2.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,6*np.pi) 
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])
plt.ylabel("angle [rads]", fontsize=12)
plt.grid(True)



#Subplot 3
ax3 = fig.add_subplot(gs[1,2], facecolor=(1,1,1))
alpha2_funct, = ax3.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,6*np.pi) 
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])
plt.ylabel("angle [rads]", fontsize=12)
plt.grid(True)


#Subplot 4
ax4 = fig.add_subplot(gs[2,2], facecolor=(1,1,1))
alpha3_funct, = ax4.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])
plt.xlabel("time [secs]",fontsize=12)
plt.ylabel("angle [rads]", fontsize=12)
plt.grid(True)


plane_ani = animation.FuncAnimation(fig,update_plot,frames = frame_amount,repeat = True, blit =True,interval = 10)
plt.show()


