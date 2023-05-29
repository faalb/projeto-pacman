if __name__ == '__main__':
    from random import randint
    import os
    from time import sleep

    MAPA = 20
    PACMAN = ['O', 'o']
    COMIDA = 'X'
    TEMPO_ESPERA = 0.3
    posicao_pacman = [randint(0, MAPA - 1), randint(0, MAPA - 1)]
    posicao_comida = [randint(0, MAPA - 1), randint(0, MAPA - 1)]
    animacao = True
    pontuacao = 0

    def gerar_mapa():
        os.system('cls')
        for i in range(MAPA):
            for j in range(MAPA):
                if i == posicao_pacman[0] and j == posicao_pacman[1]:
                    if animacao:
                        print(PACMAN[0], end='')
                    else:
                        print(PACMAN[1], end='')
                elif i == posicao_comida[0] and j == posicao_comida[1]:
                    print(COMIDA, end='')
                else:
                    print('.', end='')
            print()
        print("Pontuação:", pontuacao)

    def movimentar_pacman():
        global posicao_pacman, posicao_comida, pontuacao
        if posicao_pacman[0] < posicao_comida[0]:
            posicao_pacman[0] += 1
        elif posicao_pacman[0] > posicao_comida[0]:
            posicao_pacman[0] -= 1
        elif posicao_pacman[1] < posicao_comida[1]:
            posicao_pacman[1] += 1
        elif posicao_pacman[1] > posicao_comida[1]:
            posicao_pacman[1] -= 1

        if posicao_pacman == posicao_comida:
            posicao_comida = [randint(0, MAPA - 1), randint(0, MAPA - 1)]
            pontuacao += 1


    while True:
        gerar_mapa()
        movimentar_pacman()
        animacao = not animacao
        sleep(TEMPO_ESPERA)
