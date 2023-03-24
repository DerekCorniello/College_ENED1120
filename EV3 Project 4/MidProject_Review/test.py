#!/usr/bin/env python3
#!/usr/bin/env pybricks-micropython

import time
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor.lego import GyroSensor

import gyro_functs

STUD_MM = 260
# mdiff documentation at https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/motors.html#move-differential
# gryo diocumentation at https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/sensors.html#gyro-sensor

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, STUD_MM)
mdiff.gyro = GyroSensor(INPUT_2)


# Constant Vars:
# Testing Vars:


# Create your objects here.

mdiff.odometry_start()

mdiff.gyro.calibrate()

mdiff.turn_right(SpeedRPM(30), 90, brake = True, block = True, error_margin = 2, use_gyro = True)

time.sleep(5)

mdiff.odometry_stop()