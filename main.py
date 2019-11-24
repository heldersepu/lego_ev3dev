#!/usr/bin/env python3

from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor


class Motors:
    def __init__(self, ports):
        self.motors = [LargeMotor(address) for address in ports]

    def move(self, s1, s2, t):
        self.motors[0].run_timed(speed_sp=s1, time_sp=t)
        self.motors[1].run_timed(speed_sp=s2, time_sp=t)
        sleep((t-10)/1000)


sound = Sound()
sound.speak('go!')

motors = Motors(('outB', 'outC'))

for i in range(2):
    for i in range(2):
        motors.move(600, 800, 3000)
        motors.move(800, 600, 3000)
    motors.move(100, 900, 2400)

sound.beep()
