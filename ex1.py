segundos = int(input("Informe um inteiro: "))

def conversao(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos_s = resto % 60

    print(horas,":",minutos,":",segundos_s)

conversao(segundos);