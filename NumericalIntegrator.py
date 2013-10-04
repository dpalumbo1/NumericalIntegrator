from visual import *
from numpy import *

bodies = []
G = 6.67e-11
k = 8.96e9
dt = .5


def setdt(timeStep):
    dt = timeStep
def addBody (body):
    bodies.append(body)
def calculateForces(body1, body2):
    Fg = (G * body1.mass * body2.mass)/((mag(body1.position- body2.position))^2)
    Fe = (k * body1.charge * body2.charge)/((mag(body1.position- body2.position))^2)
    return [Fg, Fe]
def iterate():
    for body in bodies:
        forceSum = [0, 0, 0]
        for body1 in bodies:
            if (body1 != body):
                forceSum += calculateForces(body, body1)
        body.accelerate(body, forceSum, dt)
