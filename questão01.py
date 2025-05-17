# Crie uma função que encontre a menor substring de uma string que contenha todos os caracteres de outra.

from collections import Counter

def menor_substring_com_todos_caracteres(s: str, t: str) -> str:
    # Verifica se é possível encontrar a substring (t não pode ser maior que s)
    if not s or not t or len(t) > len(s):
        return ""

    # Conta os caracteres necessários com suas respectivas quantidades
    mapa_necessario = Counter(t)

    # Número total de caracteres distintos que precisamos encontrar
    caracteres_faltando = len(mapa_necessario)

    # Ponteiros para o início e fim da janela
    inicio = 0
    fim = 0

    # Contador de caracteres da janela atual
    janela = {}

    # Variáveis para armazenar a menor janela encontrada
    menor_inicio = 0
    menor_tamanho = float('inf')

    # Número de caracteres que já atendem os requisitos de t
    formados = 0

    while fim < len(s):
        # Adiciona o caractere atual da direita à janela
        caractere = s[fim]
        janela[caractere] = janela.get(caractere, 0) + 1

        # Se o caractere está no mapa_necessario e a quantidade é suficiente
        if caractere in mapa_necessario and janela[caractere] == mapa_necessario[caractere]:
            formados += 1

        # Quando todos os caracteres necessários estiverem na janela
        while inicio <= fim and formados == caracteres_faltando:
            # Atualiza o menor intervalo se for o menor encontrado até agora
            if (fim - inicio + 1) < menor_tamanho:
                menor_tamanho = fim - inicio + 1
                menor_inicio = inicio

            # Remove o caractere da esquerda da janela
            caractere_esquerda = s[inicio]
            janela[caractere_esquerda] -= 1

            # Se a quantidade ficou menor que o necessário, atualiza `formados`
            if caractere_esquerda in mapa_necessario and janela[caractere_esquerda] < mapa_necessario[caractere_esquerda]:
                formados -= 1

            # Move o ponteiro da esquerda
            inicio += 1

        # Move o ponteiro da direita
        fim += 1

    # Retorna a menor substring encontrada ou "" se não houver
    return s[menor_inicio:menor_inicio + menor_tamanho] if menor_tamanho != float('inf') else ""
