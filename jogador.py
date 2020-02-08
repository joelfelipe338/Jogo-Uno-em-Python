class Jogador():
	def __init__(self):
		self.cartas = []
		self.nome = ""

	def adicionar(self, cartas):
		self.cartas += cartas

	def retirar(self,indexs):
		for i in range(len(indexs)):
			self.cartas[indexs[i]] = "X"
		self.cartas = [i for i in self.cartas if i != "X"]

	def verCartas(self):
		return self.cartas

	def setNome(self, nome):
		self.nome = nome