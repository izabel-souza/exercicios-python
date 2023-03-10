lista = []
n = 3

while(n > 0):
    valor = (int(input("Informe um valor: ")))

    primeiro_digito = valor//10000
    valor%=10000
    segundo_digito = valor//1000
    valor%=1000
    terceiro_digito = valor//100
    valor%=100
    quarto_digito = valor//10
    valor%=10
    quinto_digito = valor//1
    valor%=1
    n-=1

    if((primeiro_digito == 2 or primeiro_digito == 5 or primeiro_digito == 9) and (segundo_digito**4 % 3 == 0 and quarto_digito**4 % 3 == 0) and (terceiro_digito != 1 and terceiro_digito != 0) and (terceiro_digito + quinto_digito > 3)):
        lista.append("True")
    else:
        lista.append("False")

for i in range(0, 3):
    print(lista[i])

