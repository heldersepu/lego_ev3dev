#!/usr/bin/env python3

import motors
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor


class SUP3R_CAR(motors.BaseCar):
    def __init__(self):
        motors.BaseCar.__init__(self)
        self.remote = InfraredSensor()
        self.remote.on_channel1_top_left = self.left
        self.remote.on_channel1_top_right = self.right
        self.remote.on_channel1_beacon = self.move
        self.remote.on_channel1_bottom_left = self.stop
        self.remote.on_channel1_bottom_right = self.rev
        self.remote.on_channel4_beacon = self.exit
        self.go = True

    def main(self):
        while self.go:
            self.remote.process()

    def exit(self, state):
        self.go = False

    def rev(self, state):
        if state:
            self.run_timed(600, 600, 5000)

    def move(self, state):
        if state:
            self.run_timed(-800, -800, 10000)

    def turn(self, state, pos):
        if state:
            self.steer.run_to_rel_pos(speed_sp=400, position_sp=pos)
        else:
            self.steer.stop()

    def left(self, state):
        self.turn(state, 5)

    def right(self, state):
        self.turn(state, -5)


sound = Sound()
sound.beep()

car = SUP3R_CAR()
car.main()
