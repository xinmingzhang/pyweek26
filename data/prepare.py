import pyglet

pyglet.resource.path = ['resources','resources/sound','resources/font']

pyglet.resource.reindex()

pyglet.resource.add_font('music_font.ttf')
# pyglet.font.add_file('music_font.ttf')
pyglet.font.load('Music For Your Ears')

pyglet.resource.add_font('ChloesMusic.ttf')
pyglet.font.load('ChloesMusic')

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
SOUND['laughter'] = pyglet.resource.media('sound/laughter.wav',streaming=False)

MUSIC = '535353124325535353124321224431524325535353124321'
BEAT =  '111111211114111111211114111111211114111111211112'

MUSIC = [int(x) for x in MUSIC]
BEAT = [int(x) for x in BEAT]

