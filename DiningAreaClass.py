from SceneClass import Scene

class DiningArea(Scene):

    def enter(self):
        print "Phew, you made it past the Zmobie."
        print 'Now you just have to get out of the restaurant.'
        print 'As you are shuffling towards the door, you'
        print 'see a horde of zmobies boogie-ing in the parking'
        print 'lot.'
        print "That is one dance party you don't want in on."
        print '\n'
        print "--- 'sneak around', 'run through' them, or 'dig under'---"
        
        self.choice = raw_input("> ")
        
        if self.choice == 'sneak around':    	
            print 'You dodge, duck, dive, dip and dodge behind the'
            print 'building, expertly crawling from cover to cover.'
            print 'Too bad the zmobies were partying so hard to'
            print "their mindless techno and couldn't see you in action."
            return 'ParkingLot'
            
        elif self.choice == 'run through':
            print 'You charge right through the crowd of undead'
            print 'partiers. They slowly start to see you bum rushing'
            print 'them and kind of freeze up. Until you trip on one'
            print 'of their legs that is. Then they all jump on you'
            print 'like lions on an antelope. Really, really groovy lions.'
            return 'Death'
            
        elif self.choice == 'dig under':
            print 'You spend some time digging by the asphalt in the'
            print 'back of the store. Then you spend some more time.'
            print 'And some more time. After a few hours you fall aslee['
            print 'and a Zmobie eats you, in a choreographed and stylized way.'
            return 'Death'
            
        else:
            print 'Bad input, guy.'
            return 'DiningArea'

