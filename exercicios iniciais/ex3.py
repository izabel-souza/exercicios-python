valor = int(input("Informe valor: "))

def conversao(valor):
    
    moedas_100 = moedas_50 = moedas_25 = moedas_10 = moedas_5 = moedas_1 = 0
    
    if(valor >= 100):
            moedas_100 = valor // 100
            valor %= 100
    if(valor >= 50):
            moedas_50 = valor // 50
            valor %= 50
    if(valor >= 25):
            moedas_25 = valor // 25
            valor %= 25
    if(valor >= 10):
            moedas_10 = valor // 10
            valor %= 10
    if(valor >= 5):
            moedas_5 = valor // 5
            valor %= 5
    else:
            moedas_1 = valor // 1
            valor %= 1

    print(f"Moedas de 1 real = {moedas_100}\nMoedas de 50 centavos = {moedas_50}\nMoedas de 25 centavos = {moedas_25}\nMoedas de 10 centavos = {moedas_10}\nMoedas de 5 centavos = {moedas_5}\nMoedas de 1 centavos = {moedas_1}")

conversao(valor)
