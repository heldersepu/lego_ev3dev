#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.motor import MediumMotor
from ev3dev2.control.rc_tank import RemoteControlledTank


class SUP3R_CAR():
    def move(self, state):
        if state:
            self.steer.run_to_rel_pos(speed_sp=400, position_sp=10)
        else:
            self.steer.stop()

    def __init__(self):
        self.tank = RemoteControlledTank('outB', 'outC')
        self.tank.on_for_seconds(50, 50, 0.2)
        self.steer = MediumMotor('outA')
        self.tank.remote.on_channel1_beacon = self.move
        self.tank.main()


sound = Sound()
sound.beep()
car = SUP3R_CAR()
