import random
import string
from .components import Block,TitleControl,TitleBlock,GameControl,Key,Note,Hint
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
        self.h = None


    def update(self,dt):
        for w in self._w:
            w.update(dt)
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
                if self.pointer < len(self.title_name) and len(self._w)%2==0 :
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

        else:

            if not self.h:
                self.h = Hint(self, 'Press Enter key', self.control, -250, 50)
                self.h.switch_to()
                self.add_window(self.h)
            for w in self._w:
                if w.__class__ == Block:
                    w.close()





class Game(Scene):
    def __init__(self,manager,width):
        super(Game,self).__init__(scene_manager=manager)
        self.width = width

        self.pointer = 0
        self.t = 0
        self.timer = 0.5
        self.control = GameControl(self.width, 10,self)
        self.control.set_location(0, 100)
        self.keys = {}
        self.notes ={}
        self.h = None

        self.keys['a'] = Key(self,0, self.control)
        self.keys['s'] = Key(self,1, self.control)
        self.keys['d'] = Key(self,2, self.control)
        self.keys['f'] = Key(self,3, self.control)
        self.keys['g'] = Key(self,4, self.control)
        self.keys['h'] = Key(self,5, self.control)
        self.keys['j']= Key(self,6, self.control)
        self.keys['k'] = Key(self,7, self.control)
        self.keys['l'] = Key(self,8, self.control)
        self.keys[';'] = Key(self,9, self.control)
        for w in self.keys:
            self.keys[w].switch_to()



    def update(self,dt,*args):
        for w in self.notes:
            w.update(dt)
        if self.h:
            self.h.update(dt)
        if self.pointer == len(MUSIC):
            if not self.h:
                self.h = Hint(self, 'Thanks for playing', self.control, -250, 50)
                self.h.switch_to()
                self.add_window(self.h)
        else:
            self.t += dt
            if self.t >= self.timer:
                a = Note(self,MUSIC[self.pointer]+2,self.control)
                a.switch_to()
                self.notes[a] = a.text
                self.t -= self.timer
                self.timer = BEAT[self.pointer]
                self.pointer += 1





