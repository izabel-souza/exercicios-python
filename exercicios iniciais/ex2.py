tempo = float(input("Informe tempo: "))

def distancia_km(tempo):
    distancia = tempo * 0.34
    return distancia

distancia_s = distancia_km(tempo)
print("Distancia em quilômetros de um raio para o observador = ", distancia_s)