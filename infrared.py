#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.motor import MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

sound = Sound()


def beep(state):
    if state:
        sound.beep()
    else:
        sound.tone([(900, 500, 500)])


remote = InfraredSensor()
remote.on_channel1_top_left = beep
remote.on_channel1_bottom_left = beep
remote.on_channel1_top_right = beep
remote.on_channel1_bottom_right = beep


sound.tone([(1000, 500, 500)])
while True:
    remote.process()
    sleep(0.01)
