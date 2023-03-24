#!/usr/bin/env python3

from ev3dev2.motor import SpeedRPM


def straight(mm, md):
    md.gyro.reset()
    for i in range(0, mm):
        while (md.gyro.angle != 0):
            if (md.gyro.angle < 0):
                md.turn_degrees(SpeedRPM(40), 1, brake = True, block = False, error_margin = 1, use_gyro = True)
            elif (md.gyro.angle > 0):
                md.turn_degrees(SpeedRPM(40), -1, brake = True, block = False, error_margin = 1, use_gyro = True)
        md.on_for_distance(SpeedRPM(60), 10, brake = False, block = False)
