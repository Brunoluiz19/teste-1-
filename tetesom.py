#ola erick baiano
#ola bruno carioca

def corrige_tabuleiro(tabuleiro):
    num_linhas = len(tabuleiro)
    if num_linhas == 0:
        return tabuleiro
    num_colunas = len(tabuleiro[0])
    
    for coluna in range(num_colunas):
        nova_coluna = []
        
        for linha in range(num_linhas):
            if tabuleiro[linha][coluna] != 0:
                nova_coluna.append(tabuleiro[linha][coluna])
        
        while len(nova_coluna) < num_linhas:
            nova_coluna.append(0)
        
        for linha in range(num_linhas):
            tabuleiro[linha][coluna] = nova_coluna[linha]
    
    return tabuleiro