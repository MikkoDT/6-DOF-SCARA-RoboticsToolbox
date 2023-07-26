
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lenths in mm
a1 = float(input("a1 = ")) # For testing, 60 mm
a2 = float(input("a2 = ")) # For testing, 70 mm
a3 = float(input("a3 = ")) # For testing, 30 mm
a4 = float(input("a4 = ")) # For testing, 70 mm
a5 = float(input("a5 = ")) # For testing, 15 mm
a6 = float(input("a6 = ")) # For testing, 5 mm
a7 = float(input("a7 = ")) # For testing, 10 mm

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)
a5 = mm_to_meter(a5)
a6 = mm_to_meter(a6)
a7 = mm_to_meter(a7)

# link limits converted to meters
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1) #60mm

# Create Links
SCARA_V3 = DHRobot([
    PrismaticDH(0,0,(0/180)*np.pi,a1,qlim=[0,lm1]),
    RevoluteDH(0,a2,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(a3,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,a4,0,0,qlim=[0,0]),
    RevoluteDH(-a5,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(a6+a7,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),

], name='SCARA_V3')

print(SCARA_V3)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q0 = np.array([0,0,0,0,0,0,0])
# Test 5mm, 60deg, 45deg, -30deg, 90deg, 30deg 
q1 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Test 10mm, 90deg, 90deg, 90deg, 90deg, 90deg 
q2 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Test 0mm, -60deg, -45deg, 30deg, 0deg, 60deg 
q3 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Test 15mm, 10deg, -45deg, 20deg, 60deg, 45deg 
q4 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Test 0mm, -60deg, -45deg, 0deg, -90deg, 40deg 
q5 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Test 0mm, 0deg, 0deg, 0deg, 0deg, 0deg 
q6 = np.array([mm_to_meter(float(input("d1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = "))),
                0,
                deg_to_rad(float(input("T4 = "))),
                deg_to_rad(float(input("T5 = "))),
                deg_to_rad(float(input("T6 = ")))])

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,15)
traj2 = rtb.jtraj(q1,q2,15)
traj3 = rtb.jtraj(q2,q3,15)
traj4 = rtb.jtraj(q3,q4,15)
traj5 = rtb.jtraj(q4,q5,15)
traj6 = rtb.jtraj(q5,q6,15)

#plot scale
x1 = -1.0
x2 = 1.0
y1 = -1.0
y2 = 1.0
z1 = -1.0
z2 = 1.0

# Plot commands
SCARA_V3.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2])
SCARA_V3.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2])
SCARA_V3.plot(traj3.q,limits=[x1,x2,y1,y2,z1,z2])
SCARA_V3.plot(traj4.q,limits=[x1,x2,y1,y2,z1,z2])
SCARA_V3.plot(traj5.q,limits=[x1,x2,y1,y2,z1,z2])
SCARA_V3.plot(traj6.q,limits=[x1,x2,y1,y2,z1,z2],block=True)


#SCARA_V3.teach(jointlabels=1)







