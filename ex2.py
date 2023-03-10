a, b, c = map(int, input("Informe 3 valores inteiros: ").split())

def retorno_maior_menor(a, b, c):
    if(a > b and a > b):
        maior = a
        if(b > c):
            menor = c
        else:
            menor = b
    if(b > a and b > c):
        maior = b
        if(a > c):
            menor = c
        else:
            menor = a
        maior = b
    else:
        maior = c
        if(a > b):
            menor = b
        else:
            menor = a

    print("Maior = ",maior)
    print("Menor = ",menor)

def pares(a, b, c):
    if(a % 2 == 0):
        print("A é par = ",a)
    if(b % 2 == 0):
        print("B é par = ",b)
    if(c % 2 == 0):
        print("C é par = ",c)

def media(a, b, c):
    media = (a + b + c)/3
    print("Media dos valores de a, b e c = ", media)

retorno_maior_menor(a,b,c)
pares(a,b,c)
media(a,b,c)