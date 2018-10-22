import random
import pyglet

sound = '535353124325535353124321224431524325535353124321'
pace =  '111111211114111111211114111111211114111111211112'



SOUND = {}


SOUND['d4'] = pyglet.resource.media('sound/d4.wav',streaming=False)
SOUND['e4'] = pyglet.resource.media('sound/e4.wav',streaming=False)
SOUND['f4'] = pyglet.resource.media('sound/f4.wav',streaming=False)
SOUND['g4'] = pyglet.resource.media('sound/g4.wav',streaming=False)
SOUND['a4'] = pyglet.resource.media('sound/a4.wav',streaming=False)
SOUND['b4'] = pyglet.resource.media('sound/b4.wav',streaming=False)
SOUND['c5'] = pyglet.resource.media('sound/c5.wav',streaming=False)
SOUND['d5'] = pyglet.resource.media('sound/d5.wav',streaming=False)
SOUND['e5'] = pyglet.resource.media('sound/e5.wav',streaming=False)
SOUND['f5'] = pyglet.resource.media('sound/f5.wav',streaming=False)



pyglet.font.add_file('music_font.ttf')
music_font = pyglet.font.load('Music For Your Ears')

class Key(pyglet.window.Window):
    nums = (x for x in range(10))

    colors =[(255,0,0,255),(0,255,0,255)]
    states = ('right', 'wrong')

    def __init__(self,num,manager,*args,**kwargs):
        super(Key,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,visible = False,*args,**kwargs)
        self.num = num
        self.set_location(200+self.width*self.num*2,0)
        self.manager = manager
        self.state = 'wrong'
        self.switch_to()


    def on_key_press(self,symbol, modifiers):
        return self.manager.on_key_press(symbol, modifiers)

    def on_key_release(self,symbol,modifiers):
        return self.manager.on_key_release(symbol, modifiers)

    def on_draw(self,*args):
        if self.state == 'wrong':
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             10, 10, self.width-10, 10, self.width-10, self.height-10, 10, self.height-10)),
                             ('c3B', (255,0,0,255,0,0,255,0,0,255,0,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             0, 0, self.width, 0, self.width-10, 10, 10, 10)),
                             ('c3B', (255,255,255,255,255,255,255,0,0,255,0,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             self.width, 0,self.width,self.height, self.width-10,self.height- 10, self.width-10, 10)),
                             ('c3B', (255,255,255,255,255,255,255,0,0,255,0,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             self.width, self.height,0,self.height, 10,self.height-10, self.width-10, self.height-10)),
                             ('c3B', (255,255,255,255,255,255,255,0,0,255,0,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             0, 0,0,self.height, 10,self.height-10, 10,10)),
                             ('c3B', (255,255,255,255,255,255,255,0,0,255,0,0)))
        if self.state == 'right':
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             10, 10, self.width-10, 10, self.width-10, self.height-10, 10, self.height-10)),
                             ('c3B', (0,255,0,0,255,0,0,255,0,0,255,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             0, 0, self.width, 0, self.width-10, 10, 10, 10)),
                             ('c3B', (255,255,255,255,255,255,0,255,0,0,255,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             self.width, 0,self.width,self.height, self.width-10,self.height- 10, self.width-10, 10)),
                             ('c3B', (255,255,255,255,255,255,0,255,0,0,255,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             self.width, self.height,0,self.height, 10,self.height-10, self.width-10, self.height-10)),
                             ('c3B', (255,255,255,255,255,255,0,255,0,0,255,0)))
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                             0, 0,0,self.height, 10,self.height-10, 10,10)),
                             ('c3B', (255,255,255,255,255,255,0,255,0,0,255,0)))


class Note(pyglet.window.Window):
    nums = (x for x in range(10))
    colors = [(255,128,0),(255,255,0),(128,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
    texts = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';')
    def __init__(self,game,num,manager,*args,**kwargs):
        super(Note,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.game = game
        self.num = num

        self.set_location(200+self.width*self.num*2,1000)
        self.y_velocity = -500
        self.y_acceleration = 100

        self.manager = manager
        self.color = Note.colors[self.num]
        self.text = Note.texts[self.num]
        self.label = pyglet.text.Label(text = self.text,font_name='Music For Your Ears',
                                       font_size=self.width//2,
                                       x=self.width//2, y=self.height//2,
                                       anchor_x='center', anchor_y='center',color = (0,0,0,255))
        self.switch_to()

    def on_key_press(self,symbol, modifiers):
        return self.manager.on_key_press(symbol, modifiers)

    def on_key_release(self,symbol,modifiers):
        return self.manager.on_key_release(symbol, modifiers)

    def on_draw(self,*args):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                                 0, 0, self.width, 0, self.width, self.height, 0,self.height)),
                             ('c3B', (255, 255, 255, 255, 255, 255, self.color[0],self.color[1],self.color[2],self.color[0],self.color[1],self.color[2])))
        self.label.draw()

    def update(self,dt,*args):
        x,y = self.get_location()
        self.y_velocity += self.y_acceleration*dt
        y += self.y_velocity*dt
        y = int(y)
        self.set_location(x, y)
        if y <= 0 or self.y_velocity >= 0:
            self.close()





class Control(pyglet.window.Window):

    def __init__(self,game,*args,**kwargs):
        super(Control,self).__init__(style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.game = game
        self.switch_to()

    def on_key_press(self,symbol, modifiers):
        if symbol == pyglet.window.key.A:
            self.game.keys['a'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'a' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['a'].state= 'right'
            self.game.keys['a'].set_visible()
            SOUND['d4'].play()
        elif symbol == pyglet.window.key.S:
            self.game.keys['s'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 's' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['s'].state= 'right'
            self.game.keys['s'].set_visible()
            SOUND['e4'].play()
        elif symbol == pyglet.window.key.D:
            self.game.keys['d'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'd' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['d'].state= 'right'
            self.game.keys['d'].set_visible()
            SOUND['f4'].play()
        elif symbol == pyglet.window.key.F:
            self.game.keys['f'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'f' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['f'].state= 'right'
            self.game.keys['f'].set_visible()
            SOUND['g4'].play()
        elif symbol == pyglet.window.key.G:
            self.game.keys['g'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'g' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['g'].state= 'right'
            self.game.keys['g'].set_visible()
            SOUND['a4'].play()
        elif symbol == pyglet.window.key.H:
            self.game.keys['h'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'h' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['h'].state= 'right'
            self.game.keys['h'].set_visible()
            SOUND['b4'].play()
        elif symbol == pyglet.window.key.J:
            self.game.keys['j'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'j' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['j'].state= 'right'
            self.game.keys['j'].set_visible()
            SOUND['c5'].play()
        elif symbol == pyglet.window.key.K:
            self.game.keys['k'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'k' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['k'].state= 'right'
            self.game.keys['k'].set_visible()
            SOUND['d5'].play()
        elif symbol == pyglet.window.key.L:
            self.game.keys['l'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == 'l' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys['l'].state= 'right'
            self.game.keys['l'].set_visible()
            SOUND['e5'].play()
        elif symbol == pyglet.window.key.SEMICOLON:
            self.game.keys[';'].state = 'wrong'
            for key,val in self.game.notes.items():
                if val == ';' and key._context:
                    x,y = key.get_location()
                    if 10 <= y <= 160:
                        self.game.keys[';'].state= 'right'
            self.game.keys[';'].set_visible()
            SOUND['f5'].play()
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()

    def on_key_release(self,symbol,mofidifers):
        if symbol == pyglet.window.key.A:
            self.game.keys['a'].set_visible(False)
        elif symbol == pyglet.window.key.S:
            self.game.keys['s'].set_visible(False)
        elif symbol == pyglet.window.key.D:
            self.game.keys['d'].set_visible(False)
        elif symbol == pyglet.window.key.F:
            self.game.keys['f'].set_visible(False)
        elif symbol == pyglet.window.key.G:
            self.game.keys['g'].set_visible(False)
        elif symbol == pyglet.window.key.H:
            self.game.keys['h'].set_visible(False)
        elif symbol == pyglet.window.key.J:
            self.game.keys['j'].set_visible(False)
        elif symbol == pyglet.window.key.K:
            self.game.keys['k'].set_visible(False)
        elif symbol == pyglet.window.key.L:
            self.game.keys['l'].set_visible(False)
        elif symbol == pyglet.window.key.SEMICOLON:
            self.game.keys[';'].set_visible(False)



class Game(object):
    def __init__(self):
        self.t = 0
        self.timer = 0.75


        self.control = Control(self,width=2000, height=10)
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
        self.t += dt
        if self.t >= self.timer:
            num = random.randint(0, 9)
            a = Note(self, num, self.control)
            self.notes[a] = a.text

            self.t -= self.timer
        for w in self.notes:
            w.update(dt)


    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()



game = Game()
game.run()