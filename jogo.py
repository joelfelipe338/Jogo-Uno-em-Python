from mesa import Mesa
from jogador import Jogador
from deck import Deck
import os

jogadores = [Jogador(), Jogador(), Jogador()]
deck = Deck()
cartaCentro = deck.comprar(1)
(cor,num) = cartaCentro[0].split("-")
pulo = 0

while num == "+2" or num == "@" or num == "<>" or num == "+4" or num=="COR":
	cartaCentro = deck.comprar(1)
	(cor,num) = cartaCentro[0].split("-")
mesa = Mesa(cartaCentro)

def menuInicial(j):
	while True:
		print("------UNO-PYTHON------")
		print("                      ")
		print("--[1] Iniciar jogo----")
		print("                      ")
		print("--[2] Sair -----------")
		print("                      ")
		print("----------------------")
		opMenu = input("")
		if opMenu == 2:
			print("Saindo...")
			os._exit(0)
		elif opMenu == 1:
			for i in range(3):
				os.system("clear")
				print("------UNO-PYTHON------------------")
				print("                                  ")
				print("--Escolha o nome do jogador "+str(i+1)+" ----")
				print("                                  ")
				print("----------------------------------")
				nome = raw_input("Digite o nome: ")
				j[i].setNome(nome)
			os.system("clear")
			print("------UNO-PYTHON------------------")
			print("                                  ")
			print("--Cartas por jogador -------------")
			print("                                  ")
			print("----------------------------------")
			numCartas = input("Digite a quantidade de cartas: ")
			for j in jogadores:
				j.adicionar(deck.comprar(numCartas))
			break

def mostrarTela(j,cor,num):
	print("------UNO-PYTHON------")
	print("    Carta do centro           "+mesa.corEsp+"    ")
	print("----------------------")
	print("         "+cor+" "+num+"                 +"+mesa.soma+"   ")
	print("----------------------")
	print("Vez de "+j.nome+", Aqui esta suas cartas:")
	print(cards)
	print("---------OPCOES-------")

def escolherCartas(j):
	selecionadas = []
	indexs = []
	primeira = ""
	ultima = ""
	print("Escolha as cartas pela ordem que sao mostradas,\nexemplo: para escolher a carta ["+j.verCartas()[0]+"] digite 1.\nDigite 0 para voltar as opcoes.")
	print(j.verCartas())
	while True:
		op = input("")
		if op > 0 and op <= len(j.verCartas()):
			if(primeira == ""):
				primeira = j.verCartas()[op-1]
			ultima = j.verCartas()[op-1]
			selecionadas.append(j.verCartas()[op-1])
			indexs.append(op-1)
			selecionadas = list(set(selecionadas))
			indexs = list(set(indexs))
			print("Selecionadas:")
			print(selecionadas)
			print("Colocar mais cartas em sequencia? ")
			print("[1] Sim")
			print("Digite qualquer outro numero para cancelar")
			op2 = input("")
			if op2 == 1:
				os.system("clear")
				mostrarTela(j,cor,num)
				print("Escolha as cartas pela ordem que sao mostradas,\nexemplo: para escolher a carta ["+j.verCartas()[0]+"] digite 1")
				print(j.verCartas())
				continue
			else:
				break
		elif op == 0:
			return False
		else:
			os.system("clear")
			mostrarTela(j,cor,num)
			print("Escolha as cartas pela ordem que sao mostradas,\nexemplo: para escolher a carta ["+j.verCartas()[0]+"] digite 1")
			print(j.verCartas())
			print("Numero invalido!!!")
	return [(selecionadas, indexs), primeira, ultima]

menuInicial(jogadores)
while True:
	for j in range(3):
		j += pulo
		while j > 2:
			j -= 3

		cards = jogadores[j].verCartas()
		(cor , num) = mesa.verCentro()
		mostrarTela(jogadores[j],cor,num)



		while True:
	
			print("[1] Jogar uma carta")
			print("[2] puxar carta e passar a vez")
			print("[3] sair do jogo")
			op = input("")
			if(op == 3):
				os.system("clear")
				mostrarTela(jogadores[j],cor,num)
				print("Tem Certeza?\n[1] para sair do jogo\nDigite qualquer outro numero para continuar")
				op2 = input()
				if op2 == 1:
					print("Saindo...")
					os._exit(0)
				else:
					os.system("clear")
					mostrarTela(jogadores[j],cor,num)
					continue 
			if op > 0 and op <= 3:
				break
			else:
				os.system("clear")
				mostrarTela(jogadores[j],cor,num)
				print("Numeo Invalido!!!")

		if op == 1:
			os.system("clear")
			mostrarTela(jogadores[j],cor,num)
			cartasEscolhidas = escolherCartas(jogadores[j])
			if( cartasEscolhidas == False):
				os.system("clear")
				break
			(escolhas, indexs) = cartasEscolhidas[0]
			primeira = cartasEscolhidas[1]
			ultima = cartasEscolhidas[2]
			while True:
				result = mesa.jogada(escolhas, primeira,ultima)
				if result == True:
					jogadores[j].retirar(indexs)
					(corAux, numAux) = primeira.split("-")
					if(numAux == "@"):
						pulo += len(escolhas)
					if(numAux == "<>"):
						print(jogadores)
						aux = jogadores[j]
						jogadores.pop(j)
						jogadores = jogadores[::-1]
						jogadores.insert(j, aux)

					break
				os.system("clear")
				mostrarTela(jogadores[j],cor,num)
				print("!!!!!!!!!!!!!!!!!!!!!")
				print("!!!JOGADA INVALIDA!!!")
				print("!!!!!!!!!!!!!!!!!!!!!")
				cartasEscolhidas = escolherCartas(jogadores[j])
				(escolhas, indexs) = cartasEscolhidas[0]
				primeira = cartasEscolhidas[1]
				ultima = cartasEscolhidas[2]


		elif op == 2:
			if(int(mesa.soma) == 0):
				jogadores[j].adicionar(deck.comprar(1))
			else:
				jogadores[j].adicionar(deck.comprar(int(mesa.soma)))
				mesa.zerar()
		if len(jogadores[j].verCartas()) == 0:
			os.system("clear")
			print("------UNO-PYTHON------------------")
			print("                                  ")
			print("  Parabens, "+jogadores[j].nome+" vc venceu!!!")
			print("                                  ")
			print("----------------------------------")
			os._exit(0)
		os.system("clear")

