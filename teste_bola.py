from bola import Bola

modelo1 = Bola("Verde", 3, "Canarinha")

print("***Modelando a Bola***")
print("Cor:", modelo1.cor, "Circunferencia:", modelo1.circunferencia, "Material:", modelo1.material)

nova_cor = input("Digite uma nova cor para a bola: ")

modelo1.troca_cor(nova_cor)

modelo1.mostra_cor()