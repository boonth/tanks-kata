
import random

from sensor import Sensor
from tank import Tank

class CowardTank(Tank):
    """This tank is a coward"""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 90, 75, False), Sensor(180, 90, 75, False)]
        self.clockwise = True
        self.forward = 1

        r = 200
        g = 50
        b = 50
        self.primary_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)

        r = 10
        g = 10
        b = 10
        self.secondary_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)

    def ai(self, delta):
        self.set_turret_target(self.get_turret_angle() +
            (90 if self.clockwise else -90))
        if self.turret_ready() and self.read_sensor(1):
           self.fire(True)

        #avoid running into things
        if self.read_sensor(0) and self.read_sensor(1):
            self.set_speed('l', 0)
            self.set_speed('r', 0)
        elif self.read_sensor(0):
            self.set_speed('l', -50)
            self.set_speed('r', -50)
            self.forward = 1
        elif self.read_sensor(1):
            self.set_speed('l', 50)
            self.set_speed('r', 50)
            self.forward = -1
        else:
            self.set_speed('l', 50*self.forward)
            self.set_speed('r', 50*self.forward)

