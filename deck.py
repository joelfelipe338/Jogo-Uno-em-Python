from random import *
class Deck:
	def __init__(self):
		self.deck = ["AZ-0","AZ-1","AZ-2","AZ-3","AZ-4","AZ-5","AZ-6","AZ-7","AZ-8","AZ-9","AZ-@","AZ-<>","AZ-+2","AZ-+2",
					"VM-0","VM-1","VM-2","VM-3","VM-4","VM-5","VM-6","VM-7","VM-8","VM-9","VM-@","VM-<>","VM-+2","VM-+2",
					"AM-0","AM-1","AM-2","AM-3","AM-4","AM-5","AM-6","AM-7","AM-8","AM-9","AM-@","AM-<>","AM-+2","AM-+2",
					"VR-0","VR-1","VR-2","VR-3","VR-4","VR-5","VR-6","VR-7","VR-8","VR-9","VR-@","VR-<>","VR-+2","VR-+2",
					"PR-COR","PR-COR","PR-COR","PR-COR","PR-+4","PR-+4","PR-+4","PR-+4"]
		self.tam = len(self.deck)
		self.descarte = []

	def __len__(self):
		return self.tam

	def comprar(self, qtd):
		if(qtd > self.tam):
			self.deck += self.descarte
			self.tam += len(self.descarte)	
		self.tam -= qtd
		cartas = []
		for i in range(qtd):
			index = randint(0,self.tam - 1)
			cartas.append(self.deck[index])
			del(self.deck[index])
		return cartas

	def descartar(self,qtd,cartas):
		for i in range(len(cartas)):
			self.descarte.append(cartas[i])
		print(self.descarte)