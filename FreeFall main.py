import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec


#Time array
t0 = 0 #[secs]
t_end = 12 #[secs]
dt = 0.02 #[secs]
t = np.arange(t0,t_end+dt,dt) #[secs]


#gravitational acceleration
g_Earth = -9.8 #[m/s^2]
g_Mars = -3.7 #[m/s^2]
g_Moon = -1.6 #[m/s^2]

#positional array i.e., y
n = 2
y_i = 100 #[m]
y_Earth = y_i + 0.5*g_Earth*t**n #[m]
y_Mars = y_i + 0.5*g_Mars*t**n #[m]
y_Moon = y_i + 0.5*g_Moon*t**n #[m]

#Velocity Y arrays
y_Earth_velocity = n*0.5*g_Earth*t**(n-1) #[m/s]
y_Mars_velocity = n*0.5*g_Mars*t**(n-1) #[m/s]
y_Moon_velocity = n*0.5*g_Moon*t**(n-1) #[m/s]


#Acceleration Y arrays
y_Earth_acceleration = (n-1)*g_Earth*t**(n-2) #[m/s^2]
y_Mars_acceleration = (n-1)*g_Mars*t**(n-2) #[m/s^2]
y_Moon_acceleration = (n-1)*g_Moon*t**(n-2) #[m/s^2]


#Creating Circles
radius = 5 #[m]
def create_circle(r):
    degrees = np.arange(0,361,1)
    radians = degrees*(np.pi/180)
    sphere_x  = r*np.cos(radians)
    sphere_y = r*np.sin(radians)

    return sphere_x,sphere_y
   

sphere_x_Earth, sphere_y_Earth = create_circle(radius)
sphere_x_Mars,sphere_y_Mars = create_circle(radius)
sphere_x_Moon,sphere_y_Moon = create_circle(radius)


######################## Animation ########################
frame_amount = len(t)
width_ratio = 1.2
y_f = -10 #[m]
dy = 10 #[m]


def update_plot(num):
    if  y_Earth[num] >= radius:
        sphere_Earth.set_data(sphere_x_Earth,sphere_y_Earth+y_Earth[num])
        alt_E.set_data(t[0:num],y_Earth[0:num])
        vel_E.set_data(t[0:num],y_Earth_velocity[0:num])
        acc_E.set_data(t[0:num],y_Earth_acceleration[0:num])
        
    if  y_Mars[num] >= radius:
        sphere_Mars.set_data(sphere_x_Mars,sphere_y_Mars+y_Mars[num])
        alt_Mars.set_data(t[0:num],y_Mars[0:num])
        vel_Mars.set_data(t[0:num],y_Mars_velocity[0:num])
        acc_Mars.set_data(t[0:num],y_Mars_acceleration[0:num])
       
    if  y_Moon[num] >= radius:
        sphere_Moon.set_data(sphere_x_Moon,sphere_y_Moon+y_Moon[num])
        alt_Moon.set_data(t[0:num],y_Moon[0:num])
        vel_Moon.set_data(t[0:num],y_Moon_velocity[0:num])
        acc_Moon.set_data(t[0:num],y_Moon_acceleration[0:num])
    
    
    return sphere_Earth,sphere_Moon,sphere_Mars,alt_E,alt_Mars,alt_Moon,vel_E,vel_Mars,vel_Moon,acc_E,acc_Mars,acc_Moon  


#Figure Properties
fig = plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)


#Creating Object for Earth
ax1 = fig.add_subplot(gs[:,0],facecolor=(0.9,0.9,0.9))
sphere_Earth, = ax1.plot([],[],'k',linewidth=3)
land_Earth, = ax1.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],'',linewidth=43)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+(2*dy),dy))
plt.title("Earth")
plt.ylabel("Altitude [m]")

#Creating Object for Mars
ax2 = fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
sphere_Mars, = ax2.plot([],[],"k",linewidth=3)
land_Mars, = ax2.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],'orangered',linewidth=43)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+(2*dy),dy))
plt.title("Mars")


#Creating Object for Moon
ax3 = fig.add_subplot(gs[:,2],facecolor=(0.9,0.9,0.9))
sphere_Moon, = ax3.plot([],[],"k",linewidth=3)
land_Moon, = ax3.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],'gray',linewidth=43)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+(2*dy),dy))
plt.title("Moon")


#Creating Position function
ax4 = fig.add_subplot(gs[0,3],facecolor=(0.9,0.9,0.9))
alt_E, = ax4.plot([],[],'',linewidth=3,label="Alt_Earth = "+ str(y_i) + '+ ('+ str(round(g_Earth/2.1))+')t^'+str(n)+' [m]')
alt_Mars, = ax4.plot([],[],'orangered',linewidth=3,label="Alt_Mars = "+ str(y_i) + '+ ('+ str(round(g_Mars/2.1))+')t^'+str(n)+' [m]')
alt_Moon, = ax4.plot([],[],'gray',linewidth=3,label="Alt_Moon = "+ str(y_i) + '+ ('+ str(round(g_Moon/2.1))+')t^'+str(n)+' [m]')
plt.xlim(0,t_end)
plt.ylim(0,y_i)
plt.legend(loc=(0.6,0.7), fontsize='x-small')


#Creating Velocity Function
ax5 = fig.add_subplot(gs[1,3],facecolor=(0.9,0.9,0.9))
vel_E, = ax5.plot([],[],'',linewidth=3,label="Vel_Earth = "+ str(g_Earth)+ 't [m/s]')
vel_Mars, = ax5.plot([],[],'orangered',linewidth=3,label="Vel_Mars = "+ str(g_Mars)+ 't [m/s]')
vel_Moon, = ax5.plot([],[],'gray',linewidth=3,label="Vel_Moon = "+ str(g_Moon)+ 't [m/s]')
plt.xlim(0,t_end)
plt.ylim(y_Earth_velocity[-1],0)
plt.legend(loc="lower left", fontsize="x-small")


#Creating Acceleration Function
ax6 = fig.add_subplot(gs[2,3],facecolor=(0.9,0.9,0.9))
acc_E, = ax6.plot([],[],'',linewidth=3,label="acc_Earth = "+ str(g_Earth) + " [m/s^2]")
acc_Mars, = ax6.plot([],[],'orangered',linewidth=3,label="acc_Mars = "+ str(g_Mars) + " [m/s^2]")
acc_Moon, = ax6.plot([],[],'gray',linewidth=3,label="acc_Moon = "+ str(g_Moon) + " [m/s^2]")
plt.xlim(0,t_end)
plt.ylim(g_Earth-1,0)
plt.legend(loc=(0.02,0.25), fontsize="x-small")


plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()




