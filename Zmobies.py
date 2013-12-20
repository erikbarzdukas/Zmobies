##########################################
# Zmobies is a text game by Erik. This is 
# for ex45 on Learn Python the Hard Way
#
# I fully expect this to be hard hehe
#
#  Dev notes
#  8/14 - The module filenames all end in
#       Class.py even though they are
#       Modules. This will be kept the
#       same for efficiency.
#
#
#   Current Bug:
#   [Fixed] NameError: global name 'start_scene' is not defined
#
##########################################
# Construction notes/brainstorming:
#Classes
#-Scenes
#    Death
#    Freezer
#    Kitchen
#    Dining Area
#    Parking Lot

from MapClass import Map
from EngineClass import Engine            

            
a_map = Map('Freezer')
a_game = Engine(a_map)
a_game.play()    
