from ev3dev2.motor import LargeMotor, MediumMotor


class BaseCar:
    def __init__(self):
        self.motors = [LargeMotor(a) for a in ('outB', 'outC')]
        self.steer = MediumMotor('outA')

    def run_timed(self, s1, s2, t):
        self.motors[0].run_timed(speed_sp=s1, time_sp=t)
        self.motors[1].run_timed(speed_sp=s2, time_sp=t)

    def stop(self, *args):
        self.motors[0].stop()
        self.motors[1].stop()
