#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.control.rc_tank import RemoteControlledTank


sound = Sound()
sound.beep()

tank = RemoteControlledTank('outB', 'outC')
tank.on_for_seconds(50, 50, 0.2)
tank.main()
