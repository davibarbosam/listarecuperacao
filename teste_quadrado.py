from quadrado import Quadrado

tam_lado = int(input("Qual o tamanho do lado: "))

quadrado1 = Quadrado(tam_lado)

nov_tam_lado = int(input("Qual o novo tamanho do lado: "))

quadrado1.muda_valor(nov_tam_lado)

print("O novo valor eh: ",quadrado1.retorna_valor_lado())

print("O valor da area eh: ",quadrado1.calcula_area())