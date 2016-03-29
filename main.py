
import pygame as pg
import os
import sys
import random

config = {
	"janela": {
		"titulo": "Jogo",
		"tamanho": [0, 0],
		"corFundo": (118, 93, 57)
	},
	"jogo": {
		"area": (28, 18),
		"areaJanela": (14, 9),
		"areaVisao": 2
	},
	"tiles": {
		"tamanho": 64,
		"tipos": {
			0: {
				"nomeArquivo": "piso",
				"block": False,
				"arquivo": ""
			},
			1: {
				"nomeArquivo": "parede",
				"block": True,
				"arquivo": ""
			},
			2: {
				"nomeArquivo": "porta_fechada",
				"block": True,
				"arquivo": ""
			},
			3: {
				"nomeArquivo": "porta_aberta",
				"block": False,
				"arquivo": ""
			},
			4: {
				"nomeArquivo": "buraco",
				"block": False,
				"arquivo": ""
			}
		}
	},
	"jogador": {
		"nomeArquivo": "skelly",
		"arquivo": "",
		"tamanho": (50, 50),
		"tamanhoReal": (31, 44)
	},
	"direcoes": {
		"diretas": {
			pg.K_LEFT: (-1, 0),
			pg.K_RIGHT: ( 1, 0),
			pg.K_UP: ( 0,-1),
			pg.K_DOWN: ( 0, 1)
		},
		"opostas": {
			pg.K_LEFT: "right",
			pg.K_RIGHT: "left",
			pg.K_UP: "bottom",
			pg.K_DOWN: "top"
		}
	},
	"mapa": [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 2, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
}

def definirTamanhoJanela():
	configJogo = config["jogo"]
	areaJanela = configJogo["areaJanela"]
	tamanhoTile = config["tiles"]["tamanho"]
	config["janela"]["tamanho"][0] = (areaJanela[0]) * tamanhoTile
	config["janela"]["tamanho"][1] = (areaJanela[1]) * tamanhoTile

def calcularPosicao(x, y):
	tamanhoTile = config["tiles"]["tamanho"]
	posicaoX = x * tamanhoTile
	posicaoY = y * tamanhoTile
	return (posicaoX, posicaoY)

def checarPosicao(w, h):
	tamanhoTile = config["tiles"]["tamanho"]
	tamanhoRealJogador = config["jogador"]["tamanhoReal"]
	x = int((h + tamanhoRealJogador[1]) / tamanhoTile)
	y = int((w + tamanhoRealJogador[0]) / tamanhoTile)
	return (x, y)

def carregarImagem(arquivo):
	return pg.image.load(os.path.join(sys.path[0], "imagens/"+arquivo+".png")).convert_alpha()

def carregarImagensTiles():
	for i in range(len(config["tiles"]["tipos"])):
		nomeArquivo = config["tiles"]["tipos"][i]["nomeArquivo"]
		config["tiles"]["tipos"][i]["arquivo"] = carregarImagem(nomeArquivo)

def carregarImagemJogador():
	config["jogador"]["arquivo"] = carregarImagem(config["jogador"]["nomeArquivo"])

class Player(pg.sprite.Sprite):
	def __init__(self, rect, speed, direction = pg.K_RIGHT):
		pg.sprite.Sprite.__init__(self)
		self.rect = pg.Rect(rect)
		self.mask = self.make_mask()
		self.speed = speed
		self.direction = direction
		self.collision_direction = None
		self.first_collision_per_frame = None
		self.old_direction = None
		self.direction_stack = []
		self.redraw = False
		self.image = None
		self.frame  = 0
		self.frames = self.get_frames()
		self.animate_timer = 0.0
		self.animate_fps = 7.0
		self.walkframes = []
		self.walkframe_dict = self.make_frame_dict()
		self.adjust_images()

		self.frame_start_pos = None
		self.total_displacement = None
		self.speed = speed

		self.velocity = [0, 0]

		self.posicaoJogador = checarPosicao(self.rect.x, self.rect.y)

	def make_mask(self):
		mask_surface = pg.Surface(self.rect.size).convert_alpha()
		mask_surface.fill((0, 0, 0, 0))
		mask_surface.fill(pg.Color("white"), (10, 20, 30, 30))
		mask = pg.mask.from_surface(mask_surface)
		return mask

	def get_frames(self):
		indices = [[0, 0], [1, 0], [2, 0], [3, 0]]
		return get_images(config["jogador"]["arquivo"], indices, self.rect.size)

	def make_frame_dict(self):
		frames = {
			pg.K_LEFT: [self.frames[0], self.frames[1]],
			pg.K_RIGHT: [pg.transform.flip(self.frames[0], True, False), pg.transform.flip(self.frames[1], True, False)],
			pg.K_DOWN: [self.frames[3], pg.transform.flip(self.frames[3], True, False)],
			pg.K_UP: [self.frames[2], pg.transform.flip(self.frames[2], True, False)]
		}

		return frames

	def adjust_images(self):
		if self.direction != self.old_direction:
			self.walkframes = self.walkframe_dict[self.direction]
			self.old_direction = self.direction
			self.redraw = True

		self.make_image()

	def make_image(self):
		now = pg.time.get_ticks()
		if self.collision_direction == None:
			if self.redraw or now-self.animate_timer > 1000/self.animate_fps:
				if self.direction_stack:
					self.frame = (self.frame+1)%len(self.walkframes)
					self.image = self.walkframes[self.frame]
				self.animate_timer = now
			if not self.image:
				self.image = self.walkframes[self.frame]
			self.redraw = False

	def add_direction(self, key):
		if key in config["direcoes"]["diretas"]:
			if key in self.direction_stack:
				self.direction_stack.remove(key)
			self.direction_stack.append(key)
			self.direction = self.direction_stack[-1]

	def pop_direction(self, key):
		if key in config["direcoes"]["diretas"]:
			if key in self.direction_stack:
				self.direction_stack.remove(key)
			if self.direction_stack:
				self.direction = self.direction_stack[-1]

	def pre_update(self, obstacles):
		self.frame_start_pos = self.rect.topleft

	def check_keys(self, keys):
		self.velocity[0] = 0
		if keys[pg.K_LEFT] or keys[pg.K_a]:
			self.velocity[0] -= self.speed
		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			self.velocity[0] += self.speed

	def update(self, obstaculos, keys):
		checarPosicao(self.rect.x, self.rect.y)
		self.adjust_images()
		self.collision_direction = None

		if self.direction_stack:
			self.movement(obstaculos, 0)
			self.movement(obstaculos, 1)

		self.check_keys(keys)
		start = self.frame_start_pos
		end = self.rect.topleft
		self.total_displacement = (end[0] - start[0], end[1] - start[1])

	def movement(self, obstaculos, i):
		change = self.speed * config["direcoes"]["diretas"][self.direction][i]
		self.rect[i] += change
		collisions = pg.sprite.spritecollide(self, obstaculos, False)
		callback = pg.sprite.collide_mask
		collide = pg.sprite.spritecollideany(self, collisions, callback)

		if collide and not self.collision_direction:
			self.collision_direction = self.get_collision_direction(collide)
		if not collide and change != 0:
			posicaoJogador = checarPosicao(self.rect.x, self.rect.y)
			if self.posicaoJogador != posicaoJogador:
				self.posicaoJogador = posicaoJogador

		while collide:
			self.rect[i] += (1 if change < 0 else -1)
			collide = pg.sprite.spritecollideany(self, collisions, callback)

	def get_collision_direction(self, other_sprite):
		dx = self.get_finite_difference(other_sprite, 0, self.speed)
		dy = self.get_finite_difference(other_sprite, 1, self.speed)
		abs_x, abs_y = abs(dx), abs(dy)
		if abs_x > abs_y:
			return ("right" if dx > 0 else "left")
		elif abs_x < abs_y:
			return ("bottom" if dy > 0 else "top")
		else:
			return config["direcoes"]["opostas"][self.direction]

	def get_finite_difference(self, other_sprite, index, delta = 1):
		base_offset = [other_sprite.rect.x-self.rect.x, other_sprite.rect.y-self.rect.y]
		offset_high = base_offset[:]
		offset_low = base_offset[:]
		offset_high[index] += delta
		offset_low[index] -= delta
		first_term = self.mask.overlap_area(other_sprite.mask, offset_high)
		second_term = self.mask.overlap_area(other_sprite.mask, offset_low)
		return first_term - second_term

	def draw(self, surface):
		surface.blit(self.image, self.rect)

class Tiles(pg.sprite.Sprite):
	def __init__(self, posicao, id):
		pg.sprite.Sprite.__init__(self)
		self.image = config["tiles"]["tipos"][id]["arquivo"]
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class Control(object):
	def __init__(self):
		self.screen = pg.display.get_surface()
		self.clock = pg.time.Clock()
		self.fps = 60.0
		self.done = False
		self.keys = pg.key.get_pressed()

		self.player = Player(
			(
				config["tiles"]["tamanho"] * 2,
				config["tiles"]["tamanho"] * 2,
				config["jogador"]["tamanho"][0],
				config["jogador"]["tamanho"][1]
			),
			3
		)

		self.posicaoJogador = self.player.posicaoJogador

		self.posicaoImagemVisao = (0, 0)

		self.cenario = None
		self.obstaculos = None
		self.definirCenario()

		self.level = pg.Surface((config["jogo"]["area"][0]*config["tiles"]["tamanho"], config["jogo"]["area"][1]*config["tiles"]["tamanho"])).convert()
		self.level_rect = self.level.get_rect()
		self.viewport = self.screen.get_rect(top = self.level_rect.top)

	def criarCenario(self):
		cenario, obstaculos = [], []
		mapa = config["mapa"]
		posicaoJogador = self.posicaoJogador
		areaVisao = range(config["jogo"]["areaVisao"] * -1, config["jogo"]["areaVisao"] + 1)

		for i in areaVisao:
			for j in areaVisao:
				x = i + posicaoJogador[0]
				y = j + posicaoJogador[1]
				tipo = mapa[x][y]
				tile = config["tiles"]["tipos"][tipo]
				tileCarregado = Tiles(calcularPosicao(y, x), tipo)

				if tile["block"]:
					obstaculos.append(tileCarregado)

				cenario.append(tileCarregado)

		return (pg.sprite.Group(cenario), pg.sprite.Group(obstaculos))

	def definirCenario(self):
		cenarioCriado = self.criarCenario()
		self.cenario = cenarioCriado[0]
		self.obstaculos = cenarioCriado[1]

	def verificarMudancaPosicaoJogador(self):
		tamanhoTile = config["tiles"]["tamanho"]
		self.posicaoImagemVisao = (self.player.rect.x - tamanhoTile * (config["jogo"]["areaVisao"] + 1), self.player.rect.y - tamanhoTile * (config["jogo"]["areaVisao"] + 1))
		if self.posicaoJogador != self.player.posicaoJogador:
			self.posicaoJogador = self.player.posicaoJogador
			self.definirCenario()

	def update_viewport(self, speed):
		for i in (0, 1):
			first_third = self.viewport[i] + self.viewport.size[i] // 3
			second_third = first_third+self.viewport.size[i] // 3
			player_center = self.player.rect.center[i]
			mult = 0
			if speed[i] > 0 and player_center >= first_third:
				mult = 0.5 if player_center < self.viewport.center[i] else 1
			elif speed[i] < 0 and player_center <= second_third:
				mult = 0.5 if player_center > self.viewport.center[i] else 1
			self.viewport[i] += mult * speed[i]
		self.viewport.clamp_ip(self.level_rect)

	def event_loop(self):
		for event in pg.event.get():
			self.keys = pg.key.get_pressed()
			if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
				self.done = True
			elif event.type == pg.KEYDOWN:
				self.player.add_direction(event.key)
			elif event.type == pg.KEYUP:
				self.player.pop_direction(event.key)

	def update(self):
		self.keys = pg.key.get_pressed()
		self.player.pre_update(self.obstaculos)
		self.player.update(self.obstaculos, self.keys)
		self.verificarMudancaPosicaoJogador()
		self.update_viewport(self.player.total_displacement)

	def draw(self):
		self.level.fill(config["janela"]["corFundo"], self.viewport)
		self.cenario.draw(self.level)
		self.player.draw(self.level)
		self.level.blit(imagemVisao, self.posicaoImagemVisao)
		self.screen.blit(self.level, (0, 0), self.viewport)

	def display_fps(self):
		tituloJanela = "{} - FPS: {:.2f}".format(config["janela"]["titulo"], self.clock.get_fps())
		pg.display.set_caption(tituloJanela)

	def main_loop(self):
		while not self.done:
			self.event_loop()
			self.update()
			self.draw()
			pg.display.update()
			self.clock.tick(self.fps)
			self.display_fps()

def get_images(sheet, frame_indices, size):
	frames = []
	for cell in frame_indices:
		frame_rect = ((size[0]*cell[0],size[1]*cell[1]), size)
		frames.append(sheet.subsurface(frame_rect))
	return frames

def main():
	global imagemVisao
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pg.init()
	pg.display.set_caption(config["janela"]["titulo"])
	definirTamanhoJanela()
	pg.display.set_mode(config["janela"]["tamanho"])
	carregarImagensTiles()
	carregarImagemJogador()
	imagemVisao = carregarImagem("visao")
	Control().main_loop()
	pg.quit()
	sys.exit()

if __name__ == "__main__":
	main()
