#Aula 03
#Usando Sprites melhorando a movimentação

import arcade
import random
import math

def dist(a, b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


class Estrela(object):
	"""docstring for estrela"""
	def __init__(self):
		super(Estrela, self).__init__()
		self.x = random.randint(0, 300)
		self.y = random.randint(0, 600)
		self.v = random.randint(2, 10)

	def draw(self):
		arcade.draw_circle_filled(self.x, self.y, 1, arcade.color.WHITE)
		self.y = self.y-self.v
		if(self.y < 0):
			self.x = random.randint(0, 300)
			self.y = 600
			self.v = random.randint(2,10)

class Nave(arcade.Sprite):
	"""docstring for Nave"""
	def __init__(self, arquivo, escala):
		super(Nave, self).__init__(arquivo, escala)
		self.vX = 0;
		self.vY = 0
		self.tiros = []

	def update(self):
		self.center_x += self.vX
		self.center_y += self.vY

class NaveInimiga(arcade.Sprite):
	"""docstring for Nave"""
	def __init__(self, arquivo, escala, kind):
		super(NaveInimiga, self).__init__(arquivo, escala)
		self.center_y = 400
		self.vX = 2
		self.vY = 0
		self.tiros = []
		self.angle = 180
		self.active = True
		self.kind = kind

	def update(self):

		if(self.active == True and self.center_x > 300):
			self.center_x = 0

		self.center_x += self.vX

		#Inimigo 0 só anda em linha reta
		#Inimigo 1 sobe e desce Curto
		if(self.kind == 1):
			self.center_y =  400 + 10*math.sin(self.center_x/25)
		#Inimigo 2 Sobe e desce Longo
		elif(self.kind == 2):
			self.center_y =  500 + 100*math.sin(self.center_x/50)
		#Inimigo 3 semicirculo p/ cima
		elif(self.kind == 3):
			self.center_y =  300 + 100*math.sin(self.center_x/100)
		#Inimigo 4 semicirculo p/ baixo
		elif(self.kind == 4):
			self.center_y =  300 - 100*math.sin(self.center_x/100)
		#Inimigo 5 começa em cima e desce
		elif(self.kind == 5):
			self.center_y =  300 + 100*math.cos(self.center_x/100)
		#Inimigo 6 começa em baixo e sobe
		elif(self.kind == 6):
			self.center_y =  300 - 100*math.cos(self.center_x/100)

class Tiro(object):
	"""docstring for Tiro"""
	def __init__(self, x, y):
		super(Tiro, self).__init__()
		self.x = x
		self.y = y
		self.v = 30

	def draw(self):
		arcade.draw_line(self.x, self.y, self.x, self.y+10, arcade.color.RED, 2)

	def update(self):
		self.y += self.v


class Jogo(arcade.Window):
	"""docstring for Jogo"""
	def __init__(self):
		super(Jogo, self).__init__(300, 600, "My First PyGame")
		arcade.set_background_color(arcade.color.BLACK)
		self.player = Nave("nave01.png", 1.5)
		self.player.center_x = 150;
		self.player.center_y = 100;

		self.enemies = []
		naveI = NaveInimiga("nave02.png", 1, 0)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave03.png", 1, 1)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave04.png", 1, 2)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave05.png", 1, 3)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave06.png", 1, 4)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave07.png", 1, 5)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave08.png", 1, 6)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave09.png", 1, 7)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave10.png", 1, 8)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		naveI = NaveInimiga("nave11.png", 1, 9)
		naveI.center_x += 30*len(self.enemies);
		self.enemies.append(naveI)

		self.estrelas = []
		for i in range(100):
			self.estrelas.append(Estrela())

	def on_draw(self):
		arcade.start_render()
		for e in self.estrelas:
			e.draw()

		for t in self.player.tiros:
			t.draw()
		self.player.draw()
		for e in self.enemies:
			if e.active == True: e.draw()

	def update(self, delta_time):
		for t in self.player.tiros:
			t.update()
			if t.y > 600:
				self.player.tiros.remove(t)
		self.player.update()
		for e in self.enemies:
			e.update()
			if e.active == False: self.enemies.remove(e)

		self.checkColisions()

	def checkColisions(self):
		for t in self.player.tiros:
			for e in self.enemies:
				if dist((t.x, t.y), (e.center_x, e.center_y)) < 10:
					e.active = False


	def on_key_press(self, key, modifier):
		if key == arcade.key.RIGHT:
			self.player.vX = 10
		if key == arcade.key.LEFT:
			self.player.vX = -10
		if key == arcade.key.UP:
			self.player.vY = 10
		if key == arcade.key.DOWN:
			self.player.vY = -10
		if key == arcade.key.SPACE:
			tiro = Tiro(self.player.center_x, self.player.center_y)
			self.player.tiros.append(tiro)

	def on_key_release(self, key, modifier):
		if key == arcade.key.RIGHT:
			self.player.vX = 0
		if key == arcade.key.LEFT:
			self.player.vX = 0
		if key == arcade.key.UP:
			self.player.vY = 0
		if key == arcade.key.DOWN:
			self.player.vY = 0


tela = Jogo()

arcade.run()