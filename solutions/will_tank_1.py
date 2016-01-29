import random

from sensor import Sensor
from tank import Tank

class Tank_1(Tank):
    """Dumb tank that goes in circles and avoids hitting things."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 180, 75, False), Sensor(0, 180, 50, False), Sensor(0, 180, 25, False)]
#, Sensor(0, 10, 50, True)]
        self.clockwise = random.random() < 0.5

    def ai(self, delta):
        self.set_turret_target(self.get_turret_angle() +
            (90 if self.clockwise else -90))
        if self.turret_ready() and self.read_sensor(1):
           self.fire(True)

        #avoid running into things
        if self.read_sensor(2):
            self.set_speed('l', -60)
            self.set_speed('r', -60)
        if self.read_sensor(1):
            self.set_speed('l', -40)
            self.set_speed('r', -40)
        elif self.read_sensor(0):
            self.set_speed('l', -20)
            self.set_speed('r', -20)
        else:
            self.set_speed('l', 50)
            self.set_speed('r', 45)


