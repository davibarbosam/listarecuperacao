from contacorrente import Conta
from contacorrente1 import Cliente

cliente1 =  Cliente("David","Barbosa",43076)

conta1 = Conta(2009,1500.0,cliente1)

print(conta1.titular.sobrenome)

print("Numero da conta:",conta1.numero,"\n Titular da conta:",conta1.titular,"\n Saldo disponivel:",conta1.saldo)


novo_titular = input("Digite um nome para o titular: ")
conta1.alterar_nome(novo_titular)	

deucerto = conta1.saque(200)

if(deucerto):
	print("Novo saldo:", conta1.saldo)
else:
	print("Saque não efetuado!")

conta1.deposito(300)
print("Após o deposito, o seu novo saldo é:",conta1.saldo)

conta1.transfere_para(500,conta2)