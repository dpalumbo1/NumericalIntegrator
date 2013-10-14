from __future__ import division
from visual import *


scene.width = 600
scene.height = 400
scene.autoscale = 0
scene.range = (100,100, 100)
scene.center = (0,50,0)

bodies = []
G = -6.67e-11
k = 8.96e9
dt = .5

def run():
     while (True):
         rate(100)
         iterate()
def setdt(timeStep):
     dt = timeStep
def addBody (body):
     bodies.append(body)
def calculateForces(body1, body2):
     Fg = (G * body1.mass * body2.mass)
     Fe = (k * body1.charge * body2.charge)
     #if (mag(body1.position()- body2.position())<1):
         #return 0
     return (Fg + Fe)*(body1.position()-
body2.position())/((mag(body1.position()- body2.position()))**3)


def iterate():
     for body in bodies:
         body.force = vector(0, 0, 0)
         for body1 in bodies:
             if (body1 != body):
                 body.force += calculateForces(body, body1)
         print body.force
     for body in bodies:
         body.accelerate(dt)


class Body():
     def __init__ (self, mass, charge, position, velocity):
         self.mass = mass
         self.charge = charge
         self.velocity = velocity
         self.model = sphere(pos = position, radius = 2.5, color =
color.red)
         self.force=vector(0,0,0)
     def accelerate (self, dt):
         self.velocity += self.force / self.mass * dt
         self.model.pos += self.velocity * dt
     def position(self):
         return self.model.pos

def main():
     addBody(Body(1000000000,0,vector(10,0,0),vector(0,.02,0)))
     addBody(Body(10000000000,0,vector(-10,0,0),vector(0,0,0)))
     print bodies
     run()

main()
