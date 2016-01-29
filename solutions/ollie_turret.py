__author__ = 'ollie'
import random

from sensor import Sensor
from tank import Tank

class TurretTank(Tank):
    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(30, 60, 150, True),
                        Sensor(-30, 60,150, True),
                        Sensor(0, 10, 50, True)]
        self.clockwise = True # random.random() < 0.5

    def ai(self, delta):
        self.set_turret_target(self.get_turret_angle() +
                               (90 if self.clockwise else -90))
        if self.turret_ready() and self.read_sensor(2):
            self.fire(True)

        if self.read_sensor(0) and not self.read_sensor(0):
            self.set_turret_target(self.get_turret_angle() + 90)
        elif not self.read_sensor(0) and self.read_sensor(1):
            self.set_turret_target(self.get_turret_angle() - 90)
