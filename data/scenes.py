import random
import string
from .components import Block,TitleControl,TitleBlock,GameControl,Key,Note
from .components import Scene
from .prepare import SOUND,MUSIC,BEAT

class Title(Scene):
    def __init__(self,manager,width):
        super(Title,self).__init__(scene_manager=manager)
        self.width = width - 80
        self.timer = 0.1
        self.t = 0
        self.pointer = 0
        self.title_name = 'Compiano'
        self.control = TitleControl(1,1,self)
        self.control.set_location(-10,-10)
        self.sound = SOUND['laughter'].play()

    def update(self,dt):
        if self.sound.playing:
            self.t += dt
            if self.t > self.timer:
                x = random.randint(0,self.width//80)
                x *= 80
                y = 1000
                y_velocity = -800
                y_acceleration = 50
                text = random.choice(string.ascii_letters)
                w = Block(x,y,y_velocity,y_acceleration,text,self.control)
                w.switch_to()
                self.add_window(w)
                if self.pointer < len(self.title_name) and len(self._w)%3==0 :
                    x = (self.width-780)//2+ self.pointer*100
                    y = 1000
                    y_velocity = -800
                    y_acceleration = 50
                    text = self.title_name[self.pointer]
                    letter_window = TitleBlock(x,y,y_velocity,y_acceleration,text,self.control)
                    letter_window.switch_to()
                    self.add_window(letter_window)
                    self.pointer += 1
                self.t -= self.timer
            for w in self._w:
                w.update(dt)
        else:
            for w in self._w:
                if w.__class__ != TitleBlock:
                    w.close()


class Game(Scene):
    def __init__(self,manager,width):
        super(Game,self).__init__(scene_manager=manager)
        self.width = width - 80
        self.pointer = 0
        self.t = 0
        self.timer = 0.5
        self.control = GameControl(2000, 10,self)
        self.control.set_location(0, 100)
        self.keys = {}
        self.notes ={}


        self.keys['a'] = Key(0, self.control)
        self.keys['s'] = Key(1, self.control)
        self.keys['d'] = Key(2, self.control)
        self.keys['f'] = Key(3, self.control)
        self.keys['g'] = Key(4, self.control)
        self.keys['h'] = Key(5, self.control)
        self.keys['j']= Key(6, self.control)
        self.keys['k'] = Key(7, self.control)
        self.keys['l'] = Key(8, self.control)
        self.keys[';'] = Key(9, self.control)

    def update(self,dt,*args):
        if self.pointer == len(MUSIC):
            pass
        else:
            self.t += dt
            if self.t >= self.timer:
                a = Note(self,MUSIC[self.pointer]+2,self.control)
                self.notes[a] = a.text
                self.t -= self.timer
                self.timer = BEAT[self.pointer]
                self.pointer += 1
        for w in self.notes:
            w.update(dt)



