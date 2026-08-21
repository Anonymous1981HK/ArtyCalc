import shells
import math


class Shell:
    def __init__(self,name,mass,diameter,cd,area):
        self.name=name
        self.mass=mass
        self.diameter=diameter
        self.cd=cd
        self.area=area


print("Available shells: ")
available_shells = list(shells.shell.keys())
for i, name in enumerate(available_shells, 1):
    print(f"{i}. {name}")
choice=int(input("Select shell by number: "))-1
selected_name=available_shells[choice]
shell_data=shells.shell[selected_name]


allstats = {
    "name": selected_name,
    "mass": shell_data["mass"],
    "diameter": shell_data["diameter"],
    "cd": shell_data["cd"],
    "area": shell_data["area"]
}
shell=Shell(**allstats)


g=9.81
rho=1.225
dt=0.01


barrelangle=float(input("Enter angle of barrel(radians): "))
muzzlev=float(input("Enter muzzle velocity(search on internet): "))


#INIT EQU
vy=muzzlev*math.sin(barrelangle)
vx=muzzlev*math.cos(barrelangle)
x=0
y=0
prevx=0
prevy=0

while y >= 0:
    prevx=x
    prevy=y

    if y<=11000:
        rho=1.225 * ((1 - 0.0000225577 * y) ** 4.25588)
    else:
        rho = 0.36391 * math.exp(-0.000157688 * (y - 11000))



    #AERODYNAMIC DRAG MODEL AND CURRENT TOTAL SPEED
    currenttotalspeed=math.sqrt(((vx*vx)+(vy*vy)))
    drag=0.5*rho*(currenttotalspeed**2)*shell.cd*shell.area

    #DIRECTIONAL DEACCELERATION
    ax=-(drag/shell.mass)*(vx/currenttotalspeed)
    ay=-(g)-((drag/shell.mass)*(vy/currenttotalspeed))
    
    if currenttotalspeed==0:
        break


    #COMPONENT VELOCITIES
    vx=vx+(ax*dt)
    vy=vy+(ay*dt)
    x=x+(vx*dt)
    y=y+(vy*dt)


#LINEAR INTERPOLATION
if y<0 and prevy != y:
    fraction=(0-prevy)/(y-prevy)
    precisex=prevx+fraction*(x-prevx)
else:
    precisex=x



#PRINT
print(f"The shell landed at {precisex:.2f} meters.")
