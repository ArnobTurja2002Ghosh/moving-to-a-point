"""
Teleports the robot to a set of start positions and plots the robot as it moves towards the
goal from each start position.
"""

from math import cos, sin, pi
from matplotlib import pyplot as plt
import numpy as np

###############################################################################
# STUDENTS: These can be left at their default values, but your code should 
# generate the right result if they are changed.
###############################################################################
START_CIRCLE_RADIUS = 5
START_CIRCLE_N = 8
TRIAL_LENGTH = 100
MANTA_Z = 0.2

def initStartPositions():
    """ Return a list of start positions for the robot.  Each start position is a tuple
    containing the (x, y, z) position of the robot."""

    ###########################################################################
    # STUDENTS: You should comment out the following line which dictates four
    # start positions at the corner of a square and replace with START_CIRCLE_N start positions
    # evenly spaced on a circle of radius START_CIRCLE_RADIUS.
    startPositions = []
    for i in range(START_CIRCLE_N):
        angle = 2 * pi * i / START_CIRCLE_N
        x = START_CIRCLE_RADIUS * cos(angle)
        y = START_CIRCLE_RADIUS * sin(angle)
        startPositions.append((x, y, MANTA_Z))
    #startPositions = [(4, 4, MANTA_Z), (-4, 4, MANTA_Z), (-4, -4, MANTA_Z), (4, -4, MANTA_Z)]
    ###########################################################################



    return startPositions

def sysCall_init():
    """ This is called at the beginning of the simulation and is used to initialize global variables. """
    global timeStep, finishedPlot, robotHandle, ax, startPositions
    
    sim = require('sim')
    
    startPositions = initStartPositions()

    # Global variables
    timeStep = 0
    finishedPlot = False

    # Get handle for the robot
    robotHandle = sim.getObject('/Manta')
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
        
def sysCall_actuation():
    """ This is called upon every time step.  This function has the following responsibilities:
        - Teleport the robot to each start position at the start of every trial.
        - Collect a history of the robot's current position and plot this history at the end of every trial.
    A trial occurs every TRIAL_LENGTH time steps until all start positions have been tested. """
    global timeStep, xHistory, yHistory, finishedPlot
    
    if finishedPlot:
        return
    
    elif timeStep % TRIAL_LENGTH == 0:
        
        if timeStep > 0:
            ax.plot(xHistory, yHistory)
            plt.show(block=False)
            plt.pause(0.01)
        
        if len(startPositions) > 0:
            # Choose the next stored start position
            startPos = startPositions.pop()
            sim.setObjectPosition(robotHandle, sim.handle_world, startPos)
            sim.setObjectOrientation(robotHandle, sim.handle_world, [0, 0, 0])
            xHistory = []
            yHistory = []
        else:
            finishedPlot = True
            plt.show()
        
    timeStep += 1

    # Store the current position
    pos = sim.getObjectPosition(robotHandle, sim.handle_world)
    xHistory.append(pos[0])
    yHistory.append(pos[1])

def sysCall_sensing():
    # Nothing needed here
    pass

def sysCall_cleanup():
    # Nothing needed here
    pass