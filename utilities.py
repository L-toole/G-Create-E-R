
import constants as c
import createPlusPlus as cpp
from wallaby import *

def wait_for_button(force=False):
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Button..."
        while not right_button():
            pass
        msleep(1)
        print "Pressed"
        msleep(1000)

def wait_for_selection(force=False):    #asks for prompt twice... FIX THIS
    #asks for response; used to determine running seeding or head-to-head code
    seeding1= False
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Left Button for Seeding...\nPress Right Button for Head-to-Head"
        while not right_button():
            if left_button():
                seeding1 = True
                print "Pressed Left"
                msleep(1000)
                return seeding1
            pass
        msleep(1)
        print "Pressed Right"
        msleep(1000)
        return seeding1

def wait_4_light(ignore=False):
    if ignore:
        wait_for_button()
        return
    while not calibrate(c.STARTLIGHT):
        pass
    _wait_4(c.STARTLIGHT)


def calibrate(port):
    print("Press LEFT button with light on")
    while not left_button():
        pass
    while left_button():
        pass
    lightOn = analog(port)
    print("On value =", lightOn)
    if lightOn > 200:
        print("Bad calibration")
        return False
    msleep(1000)
    print("Press RIGHT button with light off")
    while not right_button():
        pass
    while right_button():
        pass
    lightOff = analog(port)
    print("Off value =", lightOff)
    if lightOff < 3000:
        print("Bad calibration")
        return False

    if (lightOff - lightOn) < 2000:
        print("Bad calibration")
        return False
    c.startLightThresh = (lightOff - lightOn) / 2
    print("Good calibration! ", c.startLightThresh)
    return True

def _wait_4(port):
    print("waiting for light!! ")
    while analog(port) > c.startLightThresh:
        pass

def DEBUG(PrintTime=True):
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    disable_servos()
    exit(0)


def EXIT():
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    print 'Program finished!\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def DEBUG_with_wait():
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    msleep(5000)
    DEBUG(False)

def moveServo(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2047:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > endPos:
        speed = -speed
    for i in range(now, endPos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, endPos)
    msleep(10)

def onBlackRight():
    return cpp.TEMP_GET_ROBOT().cliff_right_signal < 2200

def onBlackLeft():
    return cpp.TEMP_GET_ROBOT().cliff_left_signal < 2200

def onBlackFrontLeft():
    return cpp.TEMP_GET_ROBOT().cliff_front_left_signal < 2200

def onBlackFrontRight():
    return cpp.TEMP_GET_ROBOT().cliff_front_right_signal < 2200

# def moveArm(servoMain, servoAssist, endPos, speed):
#     # speed of 1 is slow
#     # speed of 2000 is fast
#     # speed of 10 is the default
#     now = get_servo_position(servoMain)
#     if now > 2048:
#         print("Servo setting too large ", servoMain)
#     if now < 0:
#         print("Servo setting too small ", servoMain)
#     if now > endPos:
#         speed = -speed
#     for i in range(now, endPos, speed):
#         if c.IS_ORANGE_BOT:
#             x = int(2043.45 - 0.987 * (i))
#         elif c.IS_BLUE_BOT:
#             x = int(1924.48 - 0.987 * (i))
#         else:
#             x = int(1906.8 - 0.976 * (i)) #Previous values
#         set_servo_position(servoMain, i)
#         set_servo_position(servoAssist, x)
#         msleep(10)
#     set_servo_position(servoMain, endPos)
#     msleep(10)


def moveArm(endPos, speed):
    if get_motor_position_counter(c.leftMotor) > endPos:
        speed = -speed
        motor(c.leftMotor, speed)
        motor(c.rightMotor, speed)
        while get_motor_position_counter(c.leftMotor) > endPos:
            pass
    else:
        motor(c.leftMotor, speed)
        motor(c.rightMotor, speed)
        while get_motor_position_counter(c.leftMotor) < endPos:
            pass
    motor(c.leftMotor, 0)
    motor(c.rightMotor, 0)

def resetArm(power, time):
    # drive both motors to full-up positon
    motor(c.leftMotor, power)
    motor(c.rightMotor, power)
    msleep(time)
    motor_power(c.leftMotor, 5)
    motor_power(c.rightMotor, 5)
    msleep(250)
    clear_motor_position_counter(c.leftMotor)
    clear_motor_position_counter(c.rightMotor)
    ao()

def resetArmLowPosition():
    moveArm(c.armStartbox,20)
    ao()
    msleep(500)
    clear_motor_position_counter(c.leftMotor)
    clear_motor_position_counter(c.rightMotor)


def testArm():
    print("Left motor up")
    motor(c.leftMotor, 40)
    msleep(125)
    motor(c.leftMotor, 0)
    print("Holding with left motor")
    msleep(1000)
    ao()
    msleep(1000)
    print("Right motor up")
    motor(c.rightMotor, 40)
    msleep(125)
    motor(c.rightMotor, 0)
    print("Holding with right motor")
    msleep(1000)
    ao()
    msleep(1000)
    # resetArm()

def igusReset():
    return digital(c.IGUS_BUTTON)

def getLinefollowvalues():
    create_connect()
    while 1:
        print ("The right front line follow sensor sees: ")
        print get_create_rfcliff_amt()



