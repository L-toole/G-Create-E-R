from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p


colorOrder = []

def init():
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    create_disconnect()
    if not create_connect_once():
        print("Create not connected...")
        exit(0)
    print("Create connected...")
    create_full()
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    elif c.IS_GREEN_BOT:
        print("I AM GREEN!")
    else:
        print("I AM YELLOW")
        DEBUG() # Do not remove!!!
    selfTestDateGrab()
    p.cameraInit()
    print("Press right button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    shut_down_in(119.0)
    print("Running the robot.")
    c.START_TIME = seconds()

def selfTestDateGrab():
    print ("Running Self Test")
    enable_servo(c.servoBotGuyArm)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    msleep(1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    # open/close claw
    enable_servo(c.servoBotGuyClaw)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    # lower ramp
    enable_servo(c.servoCrateArm)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    enable_servo(c.servoCrateClaw)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmUp, 10)

    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    ao()

def pickUpDateBinsExperiment():
    #drive from start box to date bin
    #drive_timed(-160, -160, 1400)
    #rotate_degrees(86, 100)
    #drive_timed(250, 250, 1800)

    drive_timed(-250, -250, 1100)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown-150, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    drive_timed(-40, -40, 3600)
    # msleep(1000)
    moveServo(c.servoBotGuyClaw, c.clawLoose, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    drive_timed(100, 100, 1800)


####################################################################3
def getOutOfstartBox ():
    rotate_degrees(-28, 100)
    if c.IS_BLUE_BOT:
        drive_timed(-100, -100, 3000)
        rotate_degrees(90, 100)
        timedLineFollowRightFront(250, 4.85)
    elif c.IS_GREEN_BOT:
        drive_timed(-100, -100, 3200)
        rotate_degrees(80, 100)
        msleep(1000)
        #timedLineFollowRightFront(250, 4.65)
        lineFollowRightFrontTilBlack()
        drive_timed(-50, -50, 1000)

def seeBlocks():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToSecondBlock():
    timedLineFollowRightFront(200, 3.2)
    driveTilBlackLCliff()

# def goToSecondBlock():
#     lineFollowLeftFrontTilBlack()
#     drive_timed(50, 50, 1000)

def getCrates():
    if c.IS_BLUE_BOT:
        rotate_degrees(-90,200)
        drive_timed(75,75, 2000)
        msleep(1000)
        driveTilBlackLCliffAndSquareUp(-75,-75)
        moveServo(c.servoHayArm, c.hayArmDown, 15)
        moveServo(c.servoHayClaw, c.hayClawOpen, 15)
        msleep(250)
        drive_timed(-100, -100, 400)
        resetArm(30, 2000)
        drive_timed(-65, -75, 1450)
        moveServo(c.servoHayClaw, c.hayClawClosed, 15)
        msleep(500)
        driveTilBlackLCliffAndSquareUp(250,250)
        moveServo(c.servoHayArm, c.hayArmCarry, 15)
        rotate_degrees(180, 100)
        msleep(1000)
        moveServo(c.servoBotGuyClaw, c.clawBotguy, 15)
    elif c.IS_GREEN_BOT:
        rotate_degrees(-90,200)
        drive_timed(75,75, 2000)
        msleep(450)
        driveTilBlackLCliffAndSquareUp(-75,-75)
        moveServo(c.servoCrateArm, c.crateArmDown, 15)
        moveServo(c.servoCrateClaw, c.crateClawOpen, 15)
        msleep(200)
        drive_timed(-100, -100, 700)
        drive_timed(-75, -55, 1600)
        # drive_timed(-75, -75, 100)
        msleep(100)
        moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
        moveServo(c.servoCrateArm, c.crateArmMid, 15)
        msleep(350)
        driveTilBlackLCliffAndSquareUp(100, 100)
        moveServo(c.servoCrateArm, c.crateArmMid, 15)
        rotate_degrees(180, 100)
        msleep(500)
        moveServo(c.servoBotGuyClaw, c.clawBotguy, 15)

def getBotGuy():
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    driveTilBlackLCliffAndSquareUp(125,125)
    moveServo(c.servoBotGuyClaw, c.clawbotguyArea, 10)
    msleep(250)
    drive_timed(100, 100, 500)
    msleep(100)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    driveTilBlackLCliffAndSquareUp(-100, -100)
    drive_timed(-100, -100, 1500)
    msleep(500)

def gotoSecondBlock():
    print "gotoSecondBlock"
    rotate_degrees(-80, 100)

def seeBlocks2():
    print ("SeeBlocks2")
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
        dropBlocksFirst()
        DEBUG()
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToBlock3():
    timedLineFollowRightFrontBlocks(200, 3)


def seeBlocks3():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
    p.determineOrder(colorOrder)


def dropBlocksFirst():
    rotate_degrees(67 , 150)
    drive_timed(-75, -75, 1500)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    drive_timed(-50, -50, 700)
    drive_timed(50, 50, 900)
    drive_timed(-50, -50, 750)
