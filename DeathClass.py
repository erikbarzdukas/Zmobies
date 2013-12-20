###############################################################
# Death, this handles a player death
#
###############################################################

from sys import exit
from random import randint
from SceneClass import Scene


class Death(Scene):
    
   
    
    def enter(self):
        self.quips = [
        'Man, the Zmobies won!',
        'I was rooting for the Zmobies anyways.',
        'The world will find a different hero.',
        'Watch more action movies.'
    ]
        print "\n"
        print self.quips[randint(0, len(self.quips)-1)]
        print "---You are dead---"
        exit(1)
        
        
