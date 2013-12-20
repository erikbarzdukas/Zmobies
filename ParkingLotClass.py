from SceneClass import Scene
from SuccessModule import Win

class ParkingLot(Scene):

    def enter(self):
        print 'You get to the other end of the parking lot'
        print 'and see the Zmobies have been using three cars'
        print 'to blast their techno. A VW Beetle, a BMW Z4,'
        print 'and a Triumph Triple R (OK, not a car, but still'
        print 'really cool).'
        print '\n'
        print 'Pick your escape vehicle:'
        print "---vw', 'bmw', or 'triumph'---"
        
        self.choice = raw_input('> ')
        
        if self.choice == 'vw':
            print 'You hop into the Beetle, squeezing your frame'
            print 'into a car meant for 16 year old girls.'
            print "Hey, it doesn't take car taste to survive"
            print 'the zmobie apocolypse.'
            return 'Victory'
            
        elif self.choice == 'bmw':
            print 'You hop into the little Z4. You feel your penis'
            print 'shrink and your ego rise. You just survived a'
            print 'zmobie attack. You can do anything. You think as'
            print 'you drive off, never realizing that the car is'
            print 'a manual.'
            return 'Victory'
            
        elif self.choice == 'triumph':
            print 'Ah, you slide your leg over the motorcycle, pull'
            print 'on the throttle and feel the motor purr. You survived'
            print 'a zmobie attack AND got a sweet new bike.'
            print 'Today was a good day.'
            return 'Victory'
        else:
            print 'Bad input. Thought you would have the hang of'
            print 'this by now.'
            return 'ParkingLot'
        
        
        
