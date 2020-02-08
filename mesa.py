class Mesa:
	def __init__(self, carta):
		(self.cor,self.num) = carta[0].split("-")
		self.soma = "0"
		self.corEsp = ""
		self.corAbrv = ""

	def jogada(self, cartas, primeira, ultima):
		(cor, num) = primeira.split("-")
		if num == "+2" or num == "+4":
			for i in cartas:
				(corAux, numAux) = i.split("-")
				if(numAux != "+2" and numAux != "+4"):
					return False
		else:
			for i in cartas:
				(corAux, numAux) = i.split("-")
				if(numAux != num):
					return False
		

		if(self.num == "COR"):
			if(cor != self.corAbrv):
				self.corAbrv = ""
				self.corEsp = ""
				return False
		if(self.num == "+4" or self.num == "+2" and int(self.soma) > 0):
			if(self.num == "+4"):
				if(cor != self.corAbrv or (num != "+2" and num != "+4")):
					self.corAbrv = ""
					self.corEsp = ""
					return False
			elif(self.num == "+2" and (num != "+2" and num != "+4")):
				return False


		if(num == "COR"):
			print("Escolha a cor: ")
			print("[1] Azul")
			print("[2] Amarelo")
			print("[3] Verde")
			print("[4] Vermelho")
			op = input("")
			if op == 1:
				self.corEsp = "Azul"
				self.corAbrv = "AZ"
			elif op == 2:
				self.corEsp = "Amarelo"
				self.corAbrv = "AM"
			elif op == 3:
				self.corEsp = "Verde"
				self.corAbrv = "VR"
			elif op == 4:
				self.corEsp = "Vermelho"
				self.corAbrv = "VM"
			else:
				self.corEsp = ""
			(self.cor, self.num) = ultima.split("-")
			return True

		elif(num == "+4" or num == "+2"):
			if(num == "+4"):
				print("Escolha a cor: ")
				print("[1] Azul")
				print("[2] Amarelo")
				print("[3] Verde")
				print("[4] Vermelho")
				op = input("")
				if op == 1:
					self.corEsp = "Azul"
					self.corAbrv = "AZ"
				elif op == 2:
					self.corEsp = "Amarelo"
					self.corAbrv = "AM"
				elif op == 3:
					self.corEsp = "Verde"
					self.corAbrv = "VR"
				elif op == 4:
					self.corEsp = "Vermelho"
					self.corAbrv = "VM"
				else:
					self.corEsp = ""

			tot = int(self.soma)
			for i in cartas:
				(corAux, numAux) = i.split("-")
				tot += int(numAux)
			self.soma = str(tot)

			(self.cor, self.num) = ultima.split("-")
			return True

		elif(num == "<>"):
			(self.cor, self.num) = ultima.split("-")
			return True
		elif(num == "@"):
			(self.cor, self.num) = ultima.split("-")
			return True
		else:
			if(cor == self.cor or num == self.num or cor == self.corAbrv):
				(self.cor, self.num) = ultima.split("-")
				return True
			else:
				return False

	def verCentro(self):
		return (self.cor, self.num)

	def zerar(self):
		self.soma = "0"
		self.corAbrv = ""
		self.corEsp = ""


