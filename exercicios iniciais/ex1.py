raio = float(input("Informe o raio: "))
perimetro = 0
	
def calculo_perimetroCircunferencia(raio):
	perimetro = 2 * raio * 3.1416
	return perimetro
		
perimetro = calculo_perimetroCircunferencia(raio)
print("Perimetro da circunferencia de raio = ", perimetro)

# raio = float(input("Informe o raio: "))
# perimetro = 2 * 3.1416 * raio
# print("Perimetro da circunferencia de raio = ", perimetro)