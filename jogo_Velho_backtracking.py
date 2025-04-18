# // Criar tabuleiro vazio com 9 posições
# tabuleiro ← lista com 9 espaços vazios
tabuleiro = [""] * 9

# FUNÇÃO exibir_tabuleiro()
def exibir_tabuleiro():
#     imprimir linhas do tabuleiro no formato 3x3
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

# FUNÇÃO verificar_vencedor(tabuleiro, jogador)
def verificar_vencedor(tabuleiro, jogador):
#     combinacoes_vencedoras ← todas as linhas, colunas e diagonais possíveis
    combinacoes_vencedores = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
#     PARA cada combinacao EM combinacoes_vencedoras
    for combinacao in combinacoes_vencedores:
#         SE todas as posições da combinação forem iguais ao jogador
         if all(tabuleiro[pos] == jogador for pos in combinacao):
#             RETORNE verdadeiro
            return True
#     RETORNE falso
    return False

# FUNÇÃO verificar_empate(tabuleiro)
def verificar_empate(tabuleiro):
#     RETORNE verdadeiro se não houver espaços vazios no tabuleiro
    return all(pos != "" for pos in tabuleiro)

# FUNÇÃO minimax(tabuleiro, profundidade, maximizando)
def minimax(tabuleiro, profundidade, maximizado):
#     SE verificar_vencedor(tabuleiro, "X")
    if(verificar_vencedor(tabuleiro, "X")):
#         RETORNE -10 + profundidade
        return (-10 + profundidade)
#     SE verificar_vencedor(tabuleiro, "O")
    if(verificar_vencedor(tabuleiro, "O")):
#         RETORNE 10 - profundidade
        return (10 - profundidade)
#     SE verificar_empate(tabuleiro)
    if verificar_empate(tabuleiro):
#         RETORNE 0
        return 0

#     // Testa as jogadas 
#     SE maximizando == verdadeiro // Maximiza a jogada do computador
    if(maximizado == True):
#         melhor_valor ← -infinito // Menor valor possível. Podemos utilizar o -float("inf")
        melhor_valor = -float("inf")
#         PARA i de 0 até 8
        for i in range (9):
#             SE tabuleiro[i] estiver vazio
            if (tabuleiro[i] == ""):
#                 tabuleiro[i] ← "O"
                tabuleiro[i] = "O"
#                 valor ← minimax(tabuleiro, profundidade + 1, falso)
                valor = minimax(tabuleiro, profundidade + 1, False)
#                 tabuleiro[i] ← " "
                tabuleiro[i] = ""
#                 melhor_valor ← máximo(melhor_valor, valor) // Função max() pode ser usada aqui
                melhor_valor = max(melhor_valor, valor)
#         RETORNE melhor_valor
        return melhor_valor
#     SENÃO (Testa a minimização da jogada do adversario)
    else:
#         melhor_valor ← +infinito // Maior valor possível. Podemos utilizar o float("inf")
        melhor_valor = float("inf")
#         PARA i de 0 até 8
        for i in range (9):
#             SE tabuleiro[i] estiver vazio
            if (tabuleiro[i] == ""):
#                 tabuleiro[i] ← "X"
                tabuleiro[i] = "X"
#                 valor ← minimax(tabuleiro, profundidade + 1, verdadeiro)
                valor = minimax(tabuleiro, profundidade + 1, True)
#                 tabuleiro[i] ← " "
                tabuleiro[i] = ""
#                 melhor_valor ← mínimo(melhor_valor, valor) // Função min() pode ser usada aqui
                melhor_valor = min(melhor_valor, valor)
#         RETORNE melhor_valor
        return melhor_valor

# FUNÇÃO melhor_jogada(tabuleiro)
def melhor_jogada(tabuleiro):
#     melhor_valor ← -infinito // menor valor possível
    melhor_valor = -float("inf")
#     melhor_posicao ← -1
    melhor_posicao = -1

#     PARA i de 0 até 8
    for i in range(9):
#         SE tabuleiro[i] estiver vazio
        if(tabuleiro[i] == ""):
#             tabuleiro[i] ← "O"
            tabuleiro[i] = "O"
#             valor ← minimax(tabuleiro, 0, falso)
            valor = minimax(tabuleiro, 0, False)
#             tabuleiro[i] ← " "
            tabuleiro[i] = ""
#             SE valor > melhor_valor
            if(valor > melhor_valor):
#                 melhor_valor ← valor
                melhor_valor = valor
#                 melhor_posicao ← i
                melhor_posicao = i
#     RETORNE melhor_posicao
    return melhor_posicao

# FUNÇÃO jogar_jogo()
def jogar_jogo():
#     ENQUANTO VERDADEIRO
    while True:
#         exibir_tabuleiro()
        exibir_tabuleiro()

#         // Turno do jogador (X)
#         REPITA
        while True:
#             solicitar entrada do jogador entre 0 e 8
            entrada = input("\nEscolha uma posição entre 0 e 8:")
#             SE posição for válida e estiver vazia
            if entrada.isdigit() and 0 <= int(entrada) < 9 and tabuleiro[int(entrada)] == "": 
#                 tabuleiro[jogada] ← "X"
                tabuleiro[int(entrada)] = "X"
#                 SAIR do loop
                break
#             SENÃO
            else:
#                 mostrar mensagem de erro
                print("Posição inválida ou já está sendo usada. Tente novamente.")

#         SE verificar_vencedor(tabuleiro, "X")
        if(verificar_vencedor(tabuleiro, "X")):
#             exibir_tabuleiro()
            exibir_tabuleiro()
#             imprimir "Você venceu!"
            print("Você venceu!")
#             SAIR
            break
#         SE verificar_empate(tabuleiro)
        if verificar_empate(tabuleiro):
#             exibir_tabuleiro()
            exibir_tabuleiro()
#             imprimir "Empate!"
            print("Empate!")
#             SAIR
            break

#         // Turno do computador (O)
#         imprimir "Computador está pensando..."
        print("Computador está pensando...")
#         melhor_posicao ← melhor_jogada(tabuleiro)
        melhor_posicao = melhor_jogada(tabuleiro)
#         tabuleiro[melhor_posicao] ← "O"
        tabuleiro[melhor_posicao] = "O"

#         SE verificar_vencedor(tabuleiro, "O")
        if(verificar_vencedor(tabuleiro, "O")):
#             exibir_tabuleiro()
            exibir_tabuleiro()
#             imprimir "O computador venceu!"
            print("O computador venceu!")
#             SAIR
            break
#         SE verificar_empate(tabuleiro)
        if(verificar_empate(tabuleiro)):
#             exibir_tabuleiro()
            exibir_tabuleiro()
#             imprimir "Empate!"
            print("Empate!")
#             SAIR
            break

def posicoes_tabuleiro():
#     imprimir linhas do tabuleiro no formato 3x3
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")

# // Execução inicial
# imprimir mensagens de boas-vindas
print("Boas vindas ao Jogo da Velha!")
# mostrar posições do tabuleiro numeradas
print("Posições do tabuleiro")
posicoes_tabuleiro()
# chamar jogar_jogo()
print("Iniciando o jogo...\n")
jogar_jogo()