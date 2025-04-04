""" Implements the move-to-point controller described in Sec. 4.1.1.1. of
Corke's textbook. """

from math import atan2, cos, sin, sqrt

def get_smallest_signed_angular_difference(a, b):
    """ Return angle between the two given angles with the smallest absolute
    value.  This value will have a sign indicating the direction of the smallest angle between the two
    given angles. """
    # From: https://stackoverflow.com/questions/1878907/the-smallest-difference-between-2-angles
    return atan2(sin(a-b), cos(a-b))

def task1Controller(poseSelf, positionGoal):
    """ Given the pose of the robot and the position of the goal, compute the move-to-point
    controller's forward speed and steering angle, returning both as a tuple.
        poseSelf: pose of the robot (a tuple containing x, y and theta)
        positionGoal: tuple giving the (x, y) position of the goal in world coordinates.
    """
    theta_star = atan2(positionGoal[1] - poseSelf[1], positionGoal[0] - poseSelf[0])
    
    ###########################################################################
    # STUDENTS: Comment out the following line and insert appropriate code to implement the
    # move-to-point controller.  The return value should be a 2-tuple containing the forward speed and
    # steering angle.  For example, the line below indicates that the forward speed is 10 and the steering
    # angle is 1.
    if(sqrt((poseSelf[0]-positionGoal[0])**2 + (poseSelf[1]-positionGoal[1])**2) == 0):
        print("Goal reached")
    return 11*sqrt((poseSelf[0]-positionGoal[0])**2 + (poseSelf[1]-positionGoal[1])**2), get_smallest_signed_angular_difference(theta_star, poseSelf[2])
    ###########################################################################
        
        
def sysCall_init():
    sim = require('sim')
    
    # Get handles for the robot, steering wheel, motor and goal
    self.robotHandle = sim.getObject('.')
    self.steerHandle = sim.getObject('./steer_joint')
    self.motorHandle = sim.getObject('./motor_joint')
    self.goalHandle = sim.getObject('/GoalPosition')

def sysCall_actuation():
     # Get the robot's pose.  Note that there is a getObjectPose function but that returns the
     # full 6-dimensional pose vector.  
    pos = sim.getObjectPosition(self.robotHandle, sim.handle_world)
    eulerAngles = sim.getObjectOrientation(self.robotHandle, sim.handle_world)
    pose = (pos[0], pos[1], eulerAngles[2])

    # Get the goal's absolute position.
    goalPos = sim.getObjectPosition(self.goalHandle, sim.handle_world)

    # Call the controller with the robot's pose and the goal's (x, y) position.
    forwardSpeed, steeringAngle = task1Controller(pose, goalPos[0:2])

    # Actuate the robot.
    sim.setJointTargetVelocity(self.motorHandle, forwardSpeed)
    sim.setJointTargetPosition(self.steerHandle, steeringAngle)

def sysCall_sensing():
    # Nothing to do here
    pass

def sysCall_cleanup():
    # Nothing to do here
    pass
