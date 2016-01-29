import random

from sensor import Sensor
from tank import Tank

class CowardTank(Tank):
    """Dumb tank that goes in circles and avoids hitting things."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [
			Sensor(0,   90,  50, False), 
			Sensor(90,  90,  50, False),
			Sensor(180, 90,  50, False),
			Sensor(270, 90,  50, False)
			]
        self.clockwise = random.random() < 0.5
        print("starting coward!")

    def ai(self, delta):
        self.set_turret_target(self.get_turret_angle() +
            (90 if self.clockwise else -90))
        if self.turret_ready() and self.read_sensor(1):
            #self.fire(True)
            ''''''
        #avoid running into things
        if self.read_sensor(0):
            self.set_speed('l', -100)
            self.set_speed('r', -100)
        elif self.read_sensor(1):
            self.set_speed('l', 100)
            self.set_speed('r', 0)
        elif self.read_sensor(2):
            self.set_speed('l', 100)
            self.set_speed('r', 100)
        elif self.read_sensor(3):
            self.set_speed('l', 0)
            self.set_speed('r', 100)
        else:
            self.set_speed('l',20)
            self.set_speed('r',20)
