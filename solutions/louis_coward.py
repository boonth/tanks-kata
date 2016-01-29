
import random

from sensor import Sensor
from tank import Tank

class CowardTank(Tank):
    """Tank that is afraid of its own shadow."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 90, 75, False), Sensor(90, 90, 75, False),Sensor(180, 90, 75, False),Sensor(270, 90, 75, False)]
        self.clockwise = random.random() < 0.5

    def ai(self, delta):
        speed_l = 0
        speed_r = 0
        

        #avoid running into things
        if self.read_sensor(0):
            speed_l += -30
            speed_r += -30
        if self.read_sensor(1):
            speed_l += 20
            speed_r -= 20
        if self.read_sensor(2):
            speed_l += 30
            speed_r += 30
        if self.read_sensor(3):
            speed_r += 20
            speed_l -= 20
        
        if(not speed_r):
            speed_l = 30
            speed_r = 30
        self.set_speed('l', speed_l)
        self.set_speed('r', speed_r)
        
        