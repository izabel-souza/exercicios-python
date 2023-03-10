print("COMANDOS: \nD para direita\nE para esquerda\nC para cima\nB para baixo")
comando = input("Informe comando desejado: ")

if(comando != 'D' and comando != 'E' and comando != 'C' and comando != 'B'):
    print('E')

else:
    if(comando != 'D'):
        print('X')
    else:
        if(comando == 'D'):
            comando = input("Informe comando desejado: ")
            if(comando == 'B'):
                print("P3")
            elif(comando == 'E'):
                print('V')
            elif(comando == 'D'):
                comando = input("Informe comando desejado: ")
                if(comando == 'D'):
                    print('X')
                elif(comando == 'B'):
                    comando = input("Informe comando desejado: ")
                    if(comando == 'B'):
                        print("P2")
                    if(comando == 'D'):
                        print("P1")
                    if(comando == 'E'):
                        print("P3")
                    if(comando == 'C'):
                        print('E')
                    else:
                        print('E')
                elif(comando == 'E'):
                    print('V')
                else:
                    print('E')
            else:
                print('E')