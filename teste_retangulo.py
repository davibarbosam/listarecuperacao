from retangulo import Retangulo

#receber do usuarios as medidas
lado_a = int(input("Informe a medida do lado A  do local:"))
lado_b = int(input("Informe a medida do lado B do local:"))
lado_a_piso = int(input("Informe a medida do lado A  do piso:"))
lado_b_piso = int(input("Informe a medida do lado B do piso:"))

sala= Retangulo(lado_a, lado_b)
piso= Retangulo(lado_a_piso, lado_b_piso)

sala.retornar_vlr_lado()
area_sala = sala.calculo_area()
area_piso = piso.calculo_area()
perimetro_sala = sala.calculo_perimetro()
piso.calculo_perimetro()

qtd_pisos = (area_sala/area_piso)
print("A qtd de pisos necessarios é:", qtd_pisos)
qtd_rodape = (perimetro_sala/lado_a_piso)
print("A qtd de rodape necessarios é:", qtd_rodape)