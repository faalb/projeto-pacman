if __name__ == '__main__':
    from random import randint
    import os
    from time import sleep
    import winsound

    TAMANHO_MAPA = 20
    PACMAN = ['O', 'o']
    COMIDA = 'X'
    TEMPO_ESPERA = 0.1
    animacao = True
    pontos = 0
    nivel = 1

    def gerar_posicao():
        return [randint(1, TAMANHO_MAPA - 2), randint(1, TAMANHO_MAPA - 2)]

    pos_pacman = gerar_posicao()
    pos_comida = gerar_posicao()

    def gerar_mapa():
        os.system('cls')
        l = 0
        while l < TAMANHO_MAPA:
            c = 0
            while c < TAMANHO_MAPA:
                if l == pos_pacman[0] and c == pos_pacman[1]:
                    if animacao:
                        print(PACMAN[0], end='')
                    else:
                        print(PACMAN[1], end='')
                elif l == pos_comida[0] and c == pos_comida[1]:
                    print(COMIDA, end='')
                else:
                    print('.', end='')
                c += 1
            print()
            l += 1


    def movimentar_pacman():
        if pos_pacman[0] < pos_comida[0]:
            pos_pacman[0] += 1
            winsound.Beep(440, 200)
        elif pos_pacman[0] > pos_comida[0]:
            pos_pacman[0] -= 1
            winsound.Beep(440, 200)  
        elif pos_pacman[1] < pos_comida[1]:
            pos_pacman[1] += 1
            winsound.Beep(440, 200)  
        elif pos_pacman[1] > pos_comida[1]:
            pos_pacman[1] -= 1
            winsound.Beep(440, 200)  


    print("Pontos: {}".format(pontos))
    print("\nNível: {}".format(nivel))

    while True:
        gerar_mapa()
        movimentar_pacman()
        if pos_pacman == pos_comida:
            winsound.Beep(880, 500)  
            pos_comida = gerar_posicao()
            pontos += 1
        if pontos == 11:
            nivel += 1
            pontos = 0
            print("Parabéns! Você passou para o nível {}!".format(nivel))
            sleep(3)
        animacao = not animacao
        sleep(TEMPO_ESPERA)
