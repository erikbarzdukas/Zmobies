from Scene import Scene
from random import randint
from DeathClass import Death

Death = Death()


class Freezer(Scene):

    def enter(self):
        print "A horde of Zmobies has overrun the McSpanky's"
        print "in which you work. You barely escaped the wrath of the"
        print "first wave by hiding in the freezer. There are" 
        print "some Zmobies still drooling and grooving to the"
        print "agnostic sounds of Moby, but you think you can"
        print "make a break for it."
        print "\n"
        print "You try the freezer handle but it won't budge."
        print "There's a keypad. But you've forgotten the code!"
        print "Good thing there are only six keys!"
        print "---Enter the 3 digit keypad code [1-6]---"
        print "\n"
        
        guess = raw_input("[Keypad]> ")
        guesses = 0
        code = "%d%d%d" % (randint(1,6), randint(1,6), randint(1,6))
        # Debugging cheat// code = "111"
        
        #help the player by introducing some chance, should the code
        #not be guessed
        chance = randint(1,100)
        
        while guess != code and guesses <10:
            print "\n"
            print "BZZZZD"
            guesses +=1
            guess = raw_input("[Keypad]> ")
            
        if guess == code: 
            print "\n"
            print "The freezer door swings open slowly."
            print "Good thing too, your hands were getting numb"
            print "from the frozen keypad."
        
            return 'Kitchen'
            
        elif guess != code and chance >= 50:
        
            self.events = [
            "You smack the keypad out of frustration. It fractures.\n You knew the McSpanky's owners were cheap.",
            "A customer runs by and sees you in the freezer through\n the window. He stops and opens the door, blurting out 'You\n-always-made-the-best-BigMicks-thank-you, and runs off. You are grateful,\n for he saved your life and judging by his grease stained shirt, kept\n you employed.",
            "You have a temperature-induced epiphany and remember\n the code. You punch it in using the tip of your nose, as your\n hands are too numb."  ] 
            
            print "\n"
            print self.events[randint(0, len(self.events)-1)]
            print"\n"
            return 'Kitchen'
            
        else:
            print "\n"
            print "Your hands turn numb and waxy from touching"
            print "the cold keypad. You start swimming in your head"
            print "and decide to take a nap. Cold you doesn't"
            print "realize that people don't wake up from freezer naps."
            
            Death.enter()
