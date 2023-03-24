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
_INCH_TO_MM_CONVERSION = 25.4
dist = [12 * _INCH_TO_MM_CONVERSION, 36 * _INCH_TO_MM_CONVERSION, 60 * _INCH_TO_MM_CONVERSION, 84 * _INCH_TO_MM_CONVERSION]

# main

mdiff.odometry_start()

mdiff.gyro.calibrate()

for i in range(len(dist)):

    mdiff.on_for_distance(SpeedRPM(40), dist[i], brake = True, block = True) # drive the distance required

    time.sleep(30) # stop so we can take some measurements and reset the position

mdiff.odometry_stop()