
import pygame
import os
import sys
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

tamanhoBordaExterna = 32
tamanhoAdicionalBordaExterna = tamanhoBordaExterna / 2
tamanhoTile = 64
tamanhoAdicional = tamanhoBordaExterna + tamanhoTile / 2
tilesJogo = [7, 12]
tilesBorda = [2, 2]
tiles = [tilesJogo[1]+(tilesBorda[1]*2), tilesJogo[0]+(tilesBorda[0]*2)]

posicaoInicialJogador = {"x": 6, "y": 0}

posicaoJogador = [
	posicaoInicialJogador["x"]+1,
	posicaoInicialJogador["y"]+2
]

mapa = [
	[2, 3, 0, 0, 0, 0, 0, 0, 1, 0, 3, 2],
	[3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
	[2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2]
]

configTiles = {
	0: {
		"block": False,
		"nomeArquivo": "tile"
	},
	1: {
		"block": True,
		"nomeArquivo": "parede"
	},
	2: {
		"block": False,
		"nomeArquivo": "tile2"
	},
	3: {
		"block": False,
		"nomeArquivo": "tile3"
	}
}

tamanhoTela = (int(tiles[0]*tamanhoTile+tamanhoBordaExterna*2), int(tiles[1]*tamanhoTile+tamanhoBordaExterna*2))

screen = pygame.display.set_mode(tamanhoTela)

jogo = []

for x in range(tiles[0]):
	jogo.insert(x, [])
	for y in range(tiles[1]):
		if ((x < 2) or
			(y < 2) or
			(x > tiles[0] - 3) or
			(y > tiles[1] - 3)):
			valor = 1
		else:
			valor = 0
		jogo[x].insert(y, valor)

clock = pygame.time.Clock()

def calcularPosicao(posicao):
	return (posicao[0]*tamanhoTile+tamanhoAdicional, posicao[1]*tamanhoTile+tamanhoAdicional)

class BordasExternas(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(os.path.join(sys.path[0], "imagens/bordaExterna.png"))
		self.pos = [0.0, 0.0]
		self.pos[0] = startpos[0]*1.0
		self.pos[1] = startpos[1]*1.0
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]
		self.area = screen.get_rect()

class Bordas(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(os.path.join(sys.path[0], "imagens/borda.png"))
		self.pos = [0.0, 0.0]
		self.pos[0] = startpos[0]*1.0
		self.pos[1] = startpos[1]*1.0
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]
		self.area = screen.get_rect()

class Tiles(pygame.sprite.Sprite):
	def __init__(self, startpos, tipo = 1):
		pygame.sprite.Sprite.__init__(self, self.groups)
		# if tipo == 0:
			# arquivo = "tile"
		# elif tipo == 1:
			# arquivo = "parede"
		# elif tipo == 2:
			# arquivo = "tile2"
		# elif tipo == 3:
			# arquivo = "tile3"
		arquivo = configTiles[tipo]["nomeArquivo"]
		self.image = pygame.image.load(os.path.join(sys.path[0], "imagens/"+arquivo+".png"))
		self.pos = [0.0, 0.0]
		self.pos[0] = startpos[0]*1.0
		self.pos[1] = startpos[1]*1.0
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]
		self.area = screen.get_rect()

class Jogador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.image.load(os.path.join(sys.path[0], "imagens/jogador.png"))
		self.pos = [0.0, 0.0]
		startpos = calcularPosicao(posicaoJogador)
		self.pos[0] = startpos[0]*1.0
		self.pos[1] = startpos[1]*1.0
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]
		self.area = screen.get_rect()
	def update(self, seconds):
		novaPos = calcularPosicao(posicaoJogador)
		valor = 16

		direcaox, direcaoy = 0, 0
	
		if self.pos[0] < novaPos[0]:
			direcaox = 1
		elif self.pos[0] > novaPos[0]:
			direcaox = -1

		if self.pos[1] < novaPos[1]:
			direcaoy = 1
		elif self.pos[1] > novaPos[1]:
			direcaoy = -1

		valorx = valor * direcaox
		valory = valor * direcaoy

		if valorx != 0 or valory != 0:
			self.rect.centerx += valorx
			self.rect.centery += valory
			self.pos[0] += valorx
			self.pos[1] += valory
		else:
			self.rect.centerx += 0
			self.rect.centery += 0
			self.pos[0] += 0
			self.pos[1] += 0

bordasExternasGroup = pygame.sprite.Group()
bordasGroup = pygame.sprite.Group()
tilesGroup = pygame.sprite.Group()
jogadorGroup = pygame.sprite.Group()
allGroup = pygame.sprite.Group()

BordasExternas.groups = bordasExternasGroup, allGroup
Bordas.groups = bordasGroup, allGroup
Tiles.groups = tilesGroup, allGroup
Jogador.groups = jogadorGroup

tamanhoBorda = [
	int(tamanhoTela[0]/tamanhoBordaExterna),
	int(tamanhoTela[1]/tamanhoBordaExterna)
]

for i in range(tamanhoBorda[0]):
	for j in range(tamanhoBorda[1]):
		if ((i == 0 or i == tamanhoBorda[0]-1) or
			((i > 0 and i < tamanhoBorda[0]-1) and (j == 0 or j == tamanhoBorda[1]-1))):
			posicaoBordaExterna = (i * tamanhoBordaExterna + tamanhoAdicionalBordaExterna, j * tamanhoBordaExterna + tamanhoAdicionalBordaExterna)
			BordasExternas(posicaoBordaExterna)

for i in range(len(jogo)):
	for j in range(len(jogo[i])):
		posicaoTile = calcularPosicao((i, j))
		if jogo[i][j] == 1:
			Bordas(posicaoTile)
		else:
			jogo[i][j] = mapa[j-2][i-2]
			Tiles(posicaoTile, mapa[j-2][i-2])

Jogador()

background = pygame.Surface((screen.get_width(), screen.get_height()))
background.fill((255, 255, 255))
background = background.convert()

def checarPosicaoBlock(posicao):
	return configTiles[jogo[posicao[0]][posicao[1]]]["block"]

def movimentarJogador(movimento):
	novaPosicao = [posicaoJogador[0]+movimento[0], posicaoJogador[1]+movimento[1]]
	if not checarPosicaoBlock(novaPosicao):
		posicaoJogador[0] = novaPosicao[0]
		posicaoJogador[1] = novaPosicao[1]

while True:
	milliseconds = clock.tick(60)
	seconds = milliseconds / 1000.0

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				movimentarJogador([0, -1])
			elif e.key == pygame.K_DOWN:
				movimentarJogador([0, 1])
			elif e.key == pygame.K_RIGHT:
				movimentarJogador([1, 0])
			elif e.key == pygame.K_LEFT:
				movimentarJogador([-1, 0])

	screen.blit(background, (0, 0))

	allGroup.clear(screen, background)
	allGroup.update(seconds)
	allGroup.draw(screen)

	jogadorGroup.update(seconds)
	jogadorGroup.draw(screen)

	caption = "FPS: {:.2f}".format(clock.get_fps())
	pygame.display.set_caption(caption)

	pygame.display.flip()