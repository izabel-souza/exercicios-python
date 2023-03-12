frase = input("Informe a frase: ").lower()
caracteres_proibidos = set(',.;')
frase_sem_underscore = frase.replace("_", " ")

for char in frase_sem_underscore:
    if char in caracteres_proibidos:
        frase_sem_caracteresEspecificos = frase_sem_underscore.replace(char, '')
    else:
        frase_sem_caracteresEspecificos = frase_sem_underscore

palavras_numero = 1
for i in range(0, len(frase_sem_caracteresEspecificos)):
    if(frase_sem_caracteresEspecificos[i] == " "):
        palavras_numero+=1

palavras = input("Informe as palavras a serem encontradas na frase: ").lower()
palavras_sem_underscore = palavras.replace("_", " ")
lista_palavras = palavras_sem_underscore.split()

print(palavras_numero)
ocorrencia = 0
for i in lista_palavras:
    ocorrencia = frase_sem_caracteresEspecificos.count(i)
    print(i, ocorrencia)