import random

from sensor import Sensor
from tank import Tank

class ChargerTank(Tank):
    """Dumb tank that goes in circles and avoids hitting things."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 90, 50, False), Sensor(0, 5, 400, True)]
        self.clockwise = random.random() < 0.5

    def ai(self, delta):
        self.set_turret_target(0)

        if self.read_sensor(1):
            self.set_speed('l', 240)
            self.set_speed('r', 240)
        else:
            self.set_speed('l', 5)
            self.set_speed('r', -5)

        if self.read_sensor(0) and self.read_sensor(1) and self.turret_ready():
            self.fire(True)

