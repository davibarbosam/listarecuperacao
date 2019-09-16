class Quadrado:
	def __init__(self, tam_lado):
		self.tam_lado = tam_lado

	def muda_valor(self, tam_lado):
		self.tam_lado = tam_lado
		return

	def retorna_valor_lado(self):
		return self.tam_lado

	def calcula_area(self):
		area = self.tam_lado * self.tam_lado
		return area