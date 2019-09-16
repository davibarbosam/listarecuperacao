class Conta:
	#o self é uma referência para a própria coisa
	def __init__(self, numero, saldo, titular, limite=100):
		self.numero = numero
		self.saldo = saldo
		self.cliente = cliente
		self.cliente = cliente

	def transfer(self, destino, valor):
		retirou = self.sacar(valor)

		if(retirou == False):
			return False
		else:
			destino.depositar(valor)
			return True

	#Função criada para alterar o nome
	def alterar_nome(self, titular):
		self.titular = titular
		print("O novo titular é:",self.titular)
		return

	#Função criada para depósitos
	def deposito(self, valor):
		self.saldo += valor

	#Função criada para saques
	def saque(self, valor):
		#Só poderá sacar se o saldo foi maior que o valor a ser sacado
		if(self.saldo > valor):
			self.saldo -= valor
			return True
		else:
			return False