#######################p########################
# Map class, it houses the scenes and handles the
# order through which they are played
#
###############################################

from FreezerClass import Freezer
from KitchenClass import Kitchen
from DiningAreaClass import DiningArea
from ParkingLotClass import ParkingLot
from DeathClass import Death
from SuccessModule import Win

Freezer = Freezer()
Kitchen = Kitchen()
DiningArea = DiningArea()
ParkingLot = ParkingLot()
Death = Death()
Victory = Win()

class Map(object):

    scenes = {
        'Freezer' : Freezer,
        'Kitchen' : Kitchen,
        'DiningArea' : DiningArea,
        'ParkingLot' : ParkingLot,
        'Death' : Death,
        'Victory' : Victory
    }
    
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
         
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)  
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)       
