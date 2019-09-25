GlowScript 2.7 VPython

#gravitational constant
G=6.67e-11
#AU to meter conversion
AU=1.496e11
#create the sun (NOT TO SCALE) - note, the Sun doesn't move
sun=sphere(pos=vector(-.3*AU,0,0), radius=0.04*AU, color=color.yellow)
sun.m=1.989e30

#the planet  Change it's vector position for fun
planet=sphere(pos=vector(1.5*AU,0,0),radius=0.02*AU, color=color.cyan, 
make_trail=True, trail_radius=0.005*AU)
planet.m=1e20 #mass doens't actually matter for the planet
r=planet.pos-sun.pos
#just for reference, if you want a circular orbit set the velocity to this value in the y-direction
vcircle=sqrt(G*sun.m/mag(r))


#initial velocity.  CHANGE THIS
planet.v=vector(0,1e4,0)
#planet.v=vector(0,vcircle,0)



t=0
dt=3600*10 #time interval - you might need to change this if you make stuff weird

#loop for calculations
while t<1e9:
  rate(100) #rate is how fast to run sim
  r=planet.pos-sun.pos
  F=-G*planet.m*sun.m*norm(r)/mag(r)**2
  planet.v=planet.v+F*dt/planet.m
  planet.pos=planet.pos+planet.v*dt
  t=t+dt