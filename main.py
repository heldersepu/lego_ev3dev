#!/usr/bin/env python3

from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor

sound = Sound()
sound.speak('go!')

motors = [LargeMotor(address) for address in ('outB', 'outC')]

motors[0].run_timed(speed_sp=600, time_sp=5000)
motors[1].run_timed(speed_sp=800, time_sp=5000)

while any(m.state for m in motors):
    sleep(0.1)

sound.beep()
