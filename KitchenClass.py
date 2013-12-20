from SceneClass import Scene
from random import randint

class Kitchen(Scene):

    def enter(self):
        self.zmobieHealth = 400
        self.playerHealth = 500
        
        print "You stumble into the McSpanky's kitchen. It is"
        print "clear of Zmobies. You relax a little and run some"
        print "hot water on your frozen digits."
        print "\n"
        print "Once your head clears, you take a look around."
        print "You figure that you need to escape the building,"
        print "but first you should arm yourself."
        print "You see the frying basket, a knife block and an axe"
        print "--- Choose 'frying basket', 'knife', or 'axe'---"
        
        self.weapon = raw_input("> ")
        
        if self.weapon == 'frying basket':
            print "\n"
            print "You grab the frying basket from the deep fryer."
            print "It's dripping smoldering hot oil and smells like"
            print "french fries. It might take down a Zmobie yet."
            print "Or just make you really hungry"
            
        elif self.weapon == 'knife':
            print "\n"
            print "You reach into the knife block and pull out the"
            print "largest knife you find. Given that the McSpanky's"
            print "food all came frozen and preprepared, you wonder"
            print "why there is a knife block in the kitchen. After"
            print "some thought you decide to just thank your lucky" 
            print "stars that there was Zmobie fighting equipment"
            print "in the kitchen at all."
            
        elif self.weapon == 'axe':
            print "\n"
            print "You grab the emergency fire axe, you sneaky one"
            print "you."
            
        else:
            print "---Input is case sensitive in this game---"
            print "---Pick from the choices---"
            
            return 'Kitchen'
        
        #First combat scene
        print "\n"
        print "You grab a few BigMicks, because food restores health"
        print "in computer games, and you probably want that."
        print "\n"
        print "A Zmobie boogies around the corner, and spots you from"
        print "the register counter. He squares up, like a groovy boxer."
        
        #Combat time! 
        while True:
            
           
           print "\n"
           print "The Zmoby boogies up and scrapes you, leaving you"
           self.playerHealth -= randint(12,50)
           print "with %d health." % self.playerHealth
           
           if self.playerHealth <= 0:
               return 'Death'
               
           print "--- 'use weapon' 'punch' 'eat BigMick'---"
           print "\n"
           
           self.choice = raw_input("> ")
            
           if self.choice == 'use weapon':
               self.zmobieHealth -= randint(25,75)      
               print "You attack with your %s, leaving the Zmobie with" % self.weapon
               print "%d health." % self.zmobieHealth 
               print "\n"
                   
               if self.zmobieHealth <= 0:
                   return 'DiningArea'
                       
           elif self.choice == 'punch':
               self.zmobieHealth -= randint(12,50)
               print "You punch the Zmobie. Why? Don't you know they bite?"
               print "The Zmobie has %s health" % self.zmobieHealth
               print "\n"
               
               if self.zmobieHealth <= 0:
                   return 'DiningArea'
                   
           elif self.choice == 'eat BigMick':
               self.playerHealth += randint(10,50)
               print "You gobble down a BigMick. Ewww...."
               print "Your health... went up to %d! But how?.." % self.playerHealth    
               print "\n"
           else: 
               self.playerHealth -= randint(12,50)
               print "I don't understand that input." 
               print "You take a damage penalty for being silly."
    	       print "Player health: %d" % self.playerHealth
    	       
    	       if self.playerHealth <= 0:
    	           return 'Death'
    	               
    	       print "\n" 
    	       
    	          
        return 'DiningArea'
