import random
import pyglet

from .prepare import *

class SceneManager(object):
    def __init__(self):
        self.current_scene = None
        self._scenes ={}

    def add_scene(self,scene_name,scene):
        self._scenes[scene_name] = scene
        self.current_scene = scene

    def set_scene(self,scene_name):
        self.current_scene = self._scenes[scene_name]

    def update(self,dt):
        self.current_scene.update(dt)


class Scene(object):
    def __init__(self,scene_manager):
        self._w = {}
        self.controls = None
        self.manager = scene_manager

    def set_scene(self,scene_name):
        self.manager.set_scene(scene_name)

    def add_window(self,window):
        self._w[window] = 0


    def update(self,dt):
        for w in self._w:
            w.update(dt)


class Block(pyglet.window.Window):
    colors = [(255,128,0),(255,255,0),(128,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
    def __init__(self,x,y,y_velocity,y_acceleration,text,manager,*args,**kwargs):
        super(Block,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.manager = manager
        self.color = random.choice(Note.colors)
        self.text = text
        self.label = pyglet.text.Label(text = self.text,font_name='Music For Your Ears',
                                       font_size=self.width//2,
                                       x=self.width//2, y=self.height//2,
                                       anchor_x='center', anchor_y='center',color = (0,0,0,255))
        self.y_velocity = y_velocity
        self.y_acceleration = y_acceleration
        self.set_location(x,y)


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


class TitleBlock(Block):
    def __init__(self,*args,**kwargs):
        super(TitleBlock,self).__init__(*args,**kwargs)

    def update(self,dt,*args):
        x,y = self.get_location()
        if y <= 300:
            pass
        else:
            self.y_velocity += self.y_acceleration*dt
            y += self.y_velocity*dt
            y = int(y)
            self.set_location(x, y)


class Note(pyglet.window.Window):
    nums = (x for x in range(10))
    colors = [(255,128,0),(255,255,0),(128,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
    texts = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';')
    def __init__(self,game,num,manager,*args,**kwargs):
        super(Note,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.game = game
        self.num = num

        if self.game.width >=1000:
            self.set_location((self.game.width - 980)//2+100*self.num,1000)
        else:
            self.set_location((self.game.width - 800) // 2 + 80*self.num, 1000)
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

    def __init__(self,width,height,scene,*args,**kwargs):
        super(Control,self).__init__(width=width,height=height,style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.scene = scene

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self,symbol,modifiers):
        pass

class TitleControl(Control):
    def __init__(self,*args,**kwargs):
        super(TitleControl,self).__init__(*args,**kwargs)

    def on_key_release(self,symbol,modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        elif symbol == pyglet.window.key.ENTER:
            if self.scene.h:
                self.scene.h.close()
            for w in self.scene._w:
                w.close()
            self.scene.set_scene('game')


class GameControl(Control):
    def __init__(self,*args,**kwargs):
        super(GameControl,self).__init__(*args,**kwargs)
        self.game = self.scene

    def on_draw(self, *args):
        x = int(self.width / 48 * self.game.pointer)
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                                 0, 0, x, 0, x, self.height, 0, self.height)),
                             ('c3B', (255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 0, 0)))
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                                 x, x, self.width, 0, self.width, self.height, x, self.height)),
                             ('c3B', (255, 255, 255, 255, 255, 255, 0, 255, 0, 0, 255, 0)))

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
        elif symbol == pyglet.window.key.ENTER:
            if self.game.pointer == len(MUSIC):
                pyglet.app.exit()
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

class Key(pyglet.window.Window):
    nums = (x for x in range(10))

    colors =[(255,0,0,255),(0,255,0,255)]
    states = ('right', 'wrong')

    def __init__(self,game,num,manager,*args,**kwargs):
        super(Key,self).__init__(width = 80,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,visible = False,*args,**kwargs)
        self.game = game
        self.num = num
        if self.game.width >=1000:
            self.set_location((self.game.width - 980)//2 + 100*self.num,0)
        else:
            self.set_location((self.game.width - 800) // 2 + 80*self.num, 0)
        self.manager = manager
        self.state = 'wrong'



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



class Hint(pyglet.window.Window):
    def __init__(self,game,text,manager,y_velocity,y_acceleration,*args,**kwargs):
        super(Hint,self).__init__(width = 400,height = 100, style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS,*args,**kwargs)
        self.game = game
        self.text = text
        self.manager = manager
        self.label = pyglet.text.Label(text=self.text, font_name='ChloesMusic',
                                       font_size=self.height // 3,
                                       x=self.width // 2, y=self.height // 2,
                                       anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
        self.y_velocity = y_velocity
        self.y_acceleration = y_acceleration
        self.set_location((self.game.width-400)//2,1000)




    def on_key_press(self, symbol, modifiers):
        return self.manager.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        return self.manager.on_key_release(symbol, modifiers)

    def on_draw(self, *args):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (
                                 0, 0, self.width, 0, self.width, self.height, 0, self.height)),
                             ('c3B', (
                             255, 255, 0, 0, 255, 255, 255, 0, 255,255,255,255)))
        self.label.draw()

    def update(self, dt, *args):
        x, y = self.get_location()
        if y <= 500 or self.y_velocity>=0:
            pass
        else:
            self.y_velocity += self.y_acceleration * dt
            y += self.y_velocity * dt
            y = int(y)
            self.set_location(x, y)
