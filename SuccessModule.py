from SceneClass import Scene
from random import randint

class Win(Scene):

    quips = [
        'For an ugly little guy, you did pretty well.',
        'I saw a one eyed midget do it faster, but I guess you got it done.',
        'Hey, good job. You beat a word game.',
        'Absolutely thrilling performance. XO the NSA'
        ]
    def enter(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)
