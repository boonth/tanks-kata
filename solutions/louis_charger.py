
import random

from sensor import Sensor
from tank import Tank

class ChargerTank(Tank):
    """Angry Tank."""

    def __init__(self):
        Tank.__init__(self)
        self.sensors = [Sensor(0, 45, 90, True)]
        #speed = int((0.5 - random.random())*500)
        self.speed = 500
        print(self.speed) 
        
        self.set_speed('l', self.speed)
        self.set_speed('r', self.speed)        

    def ai(self, delta):
        
        
        
        if self.read_sensor(0):
            angle = self.get_turret_angle() - 45
            
            angle /= 90
            angle = int(angle)
            print(angle)
            if(angle == 0):
                speed_l = self.speed
                speed_r = self.speed
            if(angle == 1):
                speed_l = self.speed
                speed_r = 0
            if(angle == 2):
                speed_l = -self.speed
                speed_r = -self.speed            

            if(angle == 3):
                speed_l =  0
                speed_r =  self.speed
            
            if(not self.turret_ready()):
                speed_l *= -1
                speed_r *= -1                
            else: self.fire(True) 
            self.set_speed('l', speed_l)
            self.set_speed('r', speed_r)  
                
            print(speed_l, speed_r)
        else:
            self.set_turret_target(self.get_turret_angle() + 90)
            
          
