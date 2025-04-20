# FUNÇÃO mostrar_tabuleiro(tabuleiro)
def mostrar_tabuleiro(tabuleiro):
    # PARA cada linha no tabuleiro:
    for linha in tabuleiro: 
        # IMPRIMIR a linha formatada com os Pipes -> | 
        print('| ' + ' | '.join(linha) + ' |')

# FUNÇÃO proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade)
def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    # Inicializa melhor_profundidade como infinito
    melhor_profundidade = float('inf')
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    # PARA cada direção em [direita, esquerda, cima, baixo]:
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for linha, coluna in direcoes:
        # Calcula nova_linha e nova_coluna com base na direção
        nova_linha = linha_atual + linha
        nova_coluna = coluna_atual + coluna

        # SE o movimento for válido:
        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            # SE nova posição for o destino:
            if (nova_linha, nova_coluna) == (0, 3):
                return nova_linha, nova_coluna, profundidade + 1

            # Marca a nova posição no tabuleiro como visitada ('*')
            tabuleiro[nova_linha][nova_coluna] = '*'
            # Chama recursivamente proximo_movimento com nova posição e profundidade + 1
            res = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
            
            # Desmarca a posição (restaura para espaço em branco)
            tabuleiro[nova_linha][nova_coluna] = ' '
            
            # SE a profundidade do resultado for melhor que a atual:
            if res is not None and res[2] < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = res

    # RETORNA (melhor_linha, melhor_coluna, melhor_profundidade)
    if melhor_profundidade != float('inf'):
        return melhor_linha, melhor_coluna, melhor_profundidade
    return None

# FUNÇÃO movimento_valido(tabuleiro, linha, coluna)
def movimento_valido(tabuleiro, linha, coluna):
    # RETORNA verdadeiro se linha e coluna estão dentro dos limites e a posição estiver livre
    if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) and tabuleiro[linha][coluna] == ' ':
        return True
    return False

# FUNÇÃO chegou_destino(linha, coluna)
def chegou_destino(linha, coluna):
    # RETORNA verdadeiro se linha == 0 e coluna == 3
    return linha == 0 and coluna == 3

# FUNÇÃO main()
def main():
    # Define o tabuleiro com posições livres (' ') e bloqueadas ('X') -> Matriz criada
    tabuleiro = [
        ['X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', 'X', 'X', ' '],
        ['*', ' ', 'X', 'X']
    ]
    # Mostra o tabuleiro inicial
    mostrar_tabuleiro(tabuleiro)
    print("\n")

    # ENQUANTO usuário continuar e não tiver chegado ao destino:
    linha_atual, coluna_atual = 3, 0
    resultado = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

    # SE não for possível encontrar caminho (resultado é None):
    if resultado is None:
        print("Não é possível encontrar um caminho.")
    else:
        # Atualiza a posição atual com o melhor movimento encontrado
        melhor_linha, melhor_coluna, _ = resultado
        # Marca a nova posição no tabuleiro
        tabuleiro[melhor_linha][melhor_coluna] = '*'
        # Mostra o tabuleiro atualizado
        mostrar_tabuleiro(tabuleiro)

# INÍCIO
if __name__ == "__main__":
    # Executa main()
    main()
