#importing the required libraries

import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np  

#Initial Values
t0 = 0 #[hrs]
t_end = 2 #[hrs]
dt = 0.005 #[hrs]
altitude = 2 #[hrs]


#Create array for item
t = np.arange(t0,t_end+dt,dt)


#Create a X array
x = (800)*(t)


#Create a Y array
y = np.ones(len(t))* altitude

#Speed Array
speed_x = np.ones(len(t))*800


############### ANIMATION ############### 
frame_amount = len(t)
dot = np.zeros(frame_amount)
n = 20
for i in range(0,frame_amount):
    if i ==n:
        dot[i] = x[n]
        n+=20
    else:
        dot[i] = x[n-20]

def update_plot(num):
    #Subplot 1
    plane_trajectory.set_data(dot[0:num],y[0:num])
    plane_1.set_data([x[num]-40,x[num]+20],[y[num]-0,y[num]+0])
    wing_1.set_data([x[num]-20,x[num]+0],[y[num]+0.3,y[num]+0])
    wing_2.set_data([x[num]-20,x[num]+0],[y[num]-0.3,y[num]+0])
    wing_3.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]+0])
    wing_4.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]+0])
    vertical_line_0.set_data([x[num],x[num]],[0,y[num]])   
    text_ax1.set_text(f"Distance covered: {int(x[num])} kms \nTime Taken: {round(t[num],1)} hrs")
    

    #Subplot 2
    x_dist.set_data(t[0:num],x[0:num])
    horizontal_line_1.set_data([t[0],t[num]],[x[num],x[num]])
    vertical_line_1.set_data([t[num],t[num]],[x[0],x[num]])   


    #Subplot 3
    speed.set_data(t[0:num],speed_x[0:num])
    vertical_line_2.set_data([t[num],t[num]], [0,speed_x[num]])
    if num != 0:
        division_x_distance.set_text(str(int(x[num])))
        division_x_time.set_text(str(round(t[num],2)))
        division_result.set_text("= " + str(int(x[num]/t[num])) + " [km/hr]")


    return plane_trajectory,plane_1,wing_1,wing_2,wing_3,wing_4,text_ax1,horizontal_line_1,vertical_line_1,x_dist,vertical_line_0,speed,vertical_line_2,division_x_distance,division_x_time,division_result
    


fig = plt.figure( figsize=(16,9), dpi = 80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


#Subplot 1
ax1 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))
plane_trajectory, = ax1.plot( [], [], 'r:o', linewidth = 2)
plane_1, = ax1.plot([], [], 'k', linewidth = 10)
wing_1, = ax1.plot([], [], 'k', linewidth = 5)
wing_2, = ax1.plot([], [], 'k', linewidth = 5)
wing_3, = ax1.plot([], [], 'k', linewidth = 3)
wing_4, = ax1.plot([], [], 'k', linewidth = 3)

#Skyscrapers
S_1, = ax1.plot([350,350],[0,0.8],'k',linewidth=7)
S_2, = ax1.plot([150,150],[0,0.7],'k',linewidth=7)
S_3, = ax1.plot([700,700],[0,0.9],'k',linewidth=15)
S_4, = ax1.plot([900,900],[0,0.6],'k',linewidth=10)
S_5, = ax1.plot([1300,1300],[0,1.0],'k',linewidth=20)


#Text Objects
distance = 0
box = dict(boxstyle= "square",fc=(0.9,0.9,0.9), ec ="k",lw = 1)
text_ax1 = ax1.text(50,2.5, "", size = 7, color ='k', bbox = box)

#Properties
plt.title("AIRPLANE ANIMATION",fontsize=10)
plt.xlim(x[0],x[-1])
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size = 8)
plt.xlabel("X-Distance (Kms)",fontsize=8)
plt.ylim(0,altitude+1)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]),size = 8)
vertical_line_0, = ax1.plot([], [],"g:o", linewidth = 2, label= "vertical line")
plt.ylabel("Y-Altitude (Kms)",fontsize=8 )
plt.grid(True)


#Subplot 2
ax2 = fig.add_subplot(gs[1,0],facecolor = (0.9,0.9,0.9))
x_dist, = ax2.plot([], [], '-b', linewidth = 3, label= "X= 800*t")
horizontal_line_1, = ax2.plot([], [],'r:o', linewidth = 2, label= "horizontal line")
vertical_line_1, = ax2.plot([], [],"g:o", linewidth = 2, label= "vertical line")
plt.ylim(x[0],x[-1])
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4))
plt.ylabel("X-distance [kms]",fontsize=8)
plt.xlim(0,y[0])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.xlabel("Time [hrs]",fontsize=8)
plt.title("Distance as a function of time",fontsize=10)
plt.legend(loc="upper left", fontsize = 'x-large')
plt.grid(True)



#Subplot 3
ax3 = fig.add_subplot(gs[1,1],facecolor = (0.9,0.9,0.9))
speed, = ax3.plot([], [], "-b",linewidth = 3, label = "dx/dt = 800 km/hr")
plt.ylim(0,speed_x[-1]*2)
plt.yticks(np.arange(0,speed_x[-1]*2+1,speed_x[-1]*0.5),size =10)
plt.ylabel("Speed [km/hr]",fontsize=8)
plt.xlim(t[0],t[-1])
plt.xticks(np.arange(0,t[-1]+dt,t[-1]/4),size = 10)
plt.legend(loc="upper right", fontsize = 'x-large')
plt.xlabel("Time [hrs]",fontsize=8)
plt.grid(True)
plt.title("Speed as a function of time",fontsize=10)
vertical_line_2, = ax3.plot([], [], "g:o", linewidth = 3)
division_line = ax3.plot([0.1,0.20], [995,995], "k", linewidth=1)
division_x_distance = ax3.text(0.1, 1015,"", fontsize = 10,color = 'r')
division_x_time = ax3.text(0.1, 895,"",fontsize = 10, color = 'r')
division_result = ax3.text(0.25, 955,"", fontsize=10, color = "g")


plane_ani = animation.FuncAnimation(fig,update_plot,frames = frame_amount, interval=20, repeat=True, blit = True)
plt.show()
