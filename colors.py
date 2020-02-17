#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

sound = Sound()
cs = ColorSensor()

sound.beep()
for x in range(10):
    color = cs.color
    if color != cs.COLOR_NOCOLOR:
        sound.speak(cs.COLORS[color])
    else:
        sound.tone([(900, 500, 500)])
    sleep(1)
