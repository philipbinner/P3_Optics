# Task 2: Laser Cavity Stability
# For reference, see Alan Forrester, Margareta Lönnqvist, Miles J. Padgett, and Johannes Courtial, "Why are the eigenmodes of stable laser resonators structurally stable?," Opt. Lett. 27, 1869-1871 (2002).

import numpy as np
from matplotlib import pyplot as plt

#Use the thin lens equation to model the new object distance in the resonator
def new_obj_dist(obj_dist, f, l):
    return -(1/((1/f)-(1/obj_dist)))+2*l

#See the refernce above. Omega is also a good way of checking laser stability.
def omega_dist(O, L):
    return np.pi +2*np.arctan((O-L)/(np.sqrt(1-L**2)))

n = 10000
l = 3 #cavity length
f = 10 #focal length of concave mirror
u = l/4 #initial object distance
v = np.zeros(n+1) #new object distance
w = np.zeros(np.size(v)) #omega distance

#Loop to find object distance and omega distance
v[0] = new_obj_dist(u, f, l) #find first object distance for for loop
L = (l/f)-1
for i in np.arange(1,n+1): #loop to find latter object distances
    v[i] = new_obj_dist(v[i-1], f, l)
    O = (v[i-1]/f)-1
    w[i] = omega_dist(O, L)


#Plot the new object distance distribution.
plt.figure(1)
plt.hist(v, bins=np.linspace(-100,100,1000))
plt.xlim([-100, 100])
plt.xlabel('Object Distance (cm)')
plt.ylabel('Counts')
plt.title('Object Distance Distribution in Resonator')

#Plot the omega distribution. For a stable resonator, the counts should be 
#constant from 0 to 2pi meaning an object is imaged to all planes for the 
#resonator.
plt.figure(2)
plt.hist(w, bins=np.linspace(0,2*np.pi,1000))
plt.xlim(0, 2*np.pi)
plt.xlabel("omega")
plt.ylabel("Counts")
plt.title("Omega Distribution in Resonator")
plt.show()
