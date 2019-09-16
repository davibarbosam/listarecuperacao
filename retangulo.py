class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def mudar_vlr_lado(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def retornar_vlr_lado(self):
         print("Os valores do lado_a e lado_b, são respectivamente:",self.lado_a,self.lado_b)

    def calculo_area(self):
        area = ((self.lado_a)*(self.lado_b))
        print("A area do objeto é:", area)
        return area

    def calculo_perimetro(self):
        perimetro = ((self.lado_a*2)+(self.lado_b*2))
        print("O perimetro do objeto é:",perimetro)
        return perimetro