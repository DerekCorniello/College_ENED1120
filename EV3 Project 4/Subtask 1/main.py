#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from ev3dev.motor import MoveDifferential, SpeedRPM
from ev3dev.wheel import EV3Tire

STUD_MM = 70

# mdiff documentation at https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/motors.html#move-differential
# gryo diocumentation at https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/sensors.html#gyro-sensor

# test with a robot that:
# - uses the standard wheels known as EV3Tire
# - wheels are 70 mm apart

mdiff = MoveDifferential(Port.A, Port.D, EV3Tire, STUD_MM)
gyro = GyroSensor(Port.S1)

# Static Vars:
#DO NOT CHANGE HERE
_RIGHT_TURN = -90
_LEFT_TURN = 90
_STRAIGHT = -10

# Create your objects here.
# Enable odometry
mdiff.odometry_start()

mdiff.on_to_coordinates(SpeedRPM(60), 0, 50)
mdiff.on_to_coordinates(SpeedRPM(60), 50, 50)
mdiff.on_to_coordinates(SpeedRPM(60), 50, 0)
mdiff.on_to_coordinates(SpeedRPM(60), 0, 0)

mdiff.odometry_stop()