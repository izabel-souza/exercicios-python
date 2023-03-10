distancia = int(input("Informe a distancia esperada: "))
combustivel = int(input("Informe a quantidade de combustivel disponivel: "))
distancia_percorrida = 0
combustivel_usado = combustivel
combustivel_necessario = 0

for i in range(1, distancia+1): 
    distancia_percorrida += 1
    iteracao = 0

    for j in range(0, distancia_percorrida):
        if(j % 2 == 0):
            iteracao+=j
    combustivel_necessario = distancia/(iteracao+1)
    if(combustivel_necessario > combustivel_usado):
        break
    else:
        combustivel_usado -= combustivel_necessario

    print(distancia_percorrida, int(combustivel_usado))
