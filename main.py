import random
import pyglet

class KeyWindow(pyglet.window.Window):
    nums = (x for x in range(10))

    colors =[(255,0,0,255),(0,255,0,255)]
    states = ('right', 'wrong')

    def __init__(self,num,manager,*args,**kwargs):
        super(KeyWindow,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,visible = False,*args,**kwargs)
        self.num = num
        self.set_location(200+self.width*self.num*2,0)
        self.manager = manager
        self.state = 'right'
        self.switch_to()


    def on_key_press(self,symbol, modifiers):
        return self.manager.on_key_press(symbol, modifiers)

    def on_key_release(self,symbol,modifiers):
        return self.manager.on_key_release(symbol, modifiers)

    def on_draw(self,*args):
        if self.state == 'right':
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



class NoteWindow(pyglet.window.Window):
    nums = (x for x in range(10))
    colors = [(255,128,0),(255,255,0),(128,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
    texts = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';')
    def __init__(self,num,manager,*args,**kwargs):
        super(NoteWindow,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.num = num
        self.set_location(200+self.width*self.num*2,2000)
        self.manager = manager
        self.color = NoteWindow.colors[self.num]
        self.text = NoteWindow.texts[self.num]
        self.label = pyglet.text.Label(text = self.text,
                                       font_size=self.height//2,
                                       x=self.width//2, y=self.height//2,
                                       anchor_x='center', anchor_y='center')
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
        if y <= 0:
            self.close()
        else:
            y -= 20
            self.set_location(x,y)





class ControlWindow(pyglet.window.Window):

    def __init__(self,game,*args,**kwargs):
        super(ControlWindow,self).__init__(style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.game = game
        self.switch_to()

    def on_key_press(self,symbol, modifiers):
        if symbol == pyglet.window.key.A:
            self.game.key_windows['a'].set_visible()
        elif symbol == pyglet.window.key.S:
            self.game.key_windows['s'].set_visible()
        elif symbol == pyglet.window.key.D:
            self.game.key_windows['d'].set_visible()
        elif symbol == pyglet.window.key.F:
            self.game.key_windows['f'].set_visible()
        elif symbol == pyglet.window.key.G:
            self.game.key_windows['g'].set_visible()
        elif symbol == pyglet.window.key.H:
            self.game.key_windows['h'].set_visible()
        elif symbol == pyglet.window.key.J:
            self.game.key_windows['j'].set_visible()
        elif symbol == pyglet.window.key.K:
            self.game.key_windows['k'].set_visible()
        elif symbol == pyglet.window.key.L:
            self.game.key_windows['l'].set_visible()
        elif symbol == pyglet.window.key.SEMICOLON:
            self.game.key_windows[';'].set_visible()

    def on_key_release(self,symbol,mofidifers):
        if symbol == pyglet.window.key.A:
            self.game.key_windows['a'].set_visible(False)
        elif symbol == pyglet.window.key.S:
            self.game.key_windows['s'].set_visible(False)
        elif symbol == pyglet.window.key.D:
            self.game.key_windows['d'].set_visible(False)
        elif symbol == pyglet.window.key.F:
            self.game.key_windows['f'].set_visible(False)
        elif symbol == pyglet.window.key.G:
            self.game.key_windows['g'].set_visible(False)
        elif symbol == pyglet.window.key.H:
            self.game.key_windows['h'].set_visible(False)
        elif symbol == pyglet.window.key.J:
            self.game.key_windows['j'].set_visible(False)
        elif symbol == pyglet.window.key.K:
            self.game.key_windows['k'].set_visible(False)
        elif symbol == pyglet.window.key.L:
            self.game.key_windows['l'].set_visible(False)
        elif symbol == pyglet.window.key.SEMICOLON:
            self.game.key_windows[';'].set_visible(False)




d4 = pyglet.resource.media('sound/d4.wav',streaming=False)
e4 = pyglet.resource.media('sound/e4.wav',streaming=False)
f4 = pyglet.resource.media('sound/f4.wav',streaming=False)
g4 = pyglet.resource.media('sound/g4.wav',streaming=False)
a4 = pyglet.resource.media('sound/a4.wav',streaming=False)
b4 = pyglet.resource.media('sound/b4.wav',streaming=False)
c5 = pyglet.resource.media('sound/c5.wav',streaming=False)
d5 = pyglet.resource.media('sound/d5.wav',streaming=False)
e5 = pyglet.resource.media('sound/e5.wav',streaming=False)
f5 = pyglet.resource.media('sound/f5.wav',streaming=False)






t = 0
delt_t = 1




class Game(object):
    def __init__(self):
        self.t = 0
        self.timer = 1

        self.control_window = ControlWindow(self,width=2000, height=10)
        self.control_window.set_location(0, 100)
        self.key_windows = {}

        self.key_windows['a'] = KeyWindow(0, self.control_window)
        self.key_windows['s'] = KeyWindow(1, self.control_window)
        self.key_windows['d'] = KeyWindow(2, self.control_window)
        self.key_windows['f'] = KeyWindow(3, self.control_window)
        self.key_windows['g'] = KeyWindow(4, self.control_window)
        self.key_windows['h'] = KeyWindow(5, self.control_window)
        self.key_windows['j']= KeyWindow(6, self.control_window)
        self.key_windows['k'] = KeyWindow(7, self.control_window)
        self.key_windows['l'] = KeyWindow(8, self.control_window)
        self.key_windows[';'] = KeyWindow(9, self.control_window)


    def update(self,dt,*args):
        self.t += dt
        if self.t >= self.timer:
            num = random.randint(0,9)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()



game = Game()
game.run()