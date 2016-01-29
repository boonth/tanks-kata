import random

from sensor import Sensor
from tank import Tank

class Tank_2(Tank):
    """Dumb tank that goes in circles and avoids hitting things."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(-45, 90, 75, False), Sensor(45, 90, 75, False), 
Sensor(0, 10, 50, True)]
        self.clockwise = random.random() < 0.5
        self.tread_accel = 120
        self.tread_max = 120

    def ai(self, delta):
        self.set_turret_target(self.get_turret_angle() +
            (90 if self.clockwise else -90))
        if self.turret_ready() and self.read_sensor(1):
           self.fire(True)

        #avoid running into things
        if self.read_sensor(1):
            self.set_speed('l', 70)
            self.set_speed('r', 90)
        elif self.read_sensor(0):
            self.set_speed('l', 90)
            self.set_speed('r', 70)
        else:
            self.set_speed('l', 110)
            self.set_speed('r', 95)

    #def damage(self):
    #    pass

