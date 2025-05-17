# Dado uma string com parênteses, determine se ela está corretamente balanceada e quais índices devem ser removidos para balancear, se necessário.

'''

passo a passo de como resolver:

O primeiro passo - ler uma string qualquer do usuário, para isso
fiz uma função chamada balance_string, na qual ele vai receber uma 
string do usuário

segundo passo - criar uma variável chamada list_str [], para cada
string que o usuário inserir, vai adicionar na lista

terceiro passo - percorrer a list_str caractere por caractere.

quarto passo - fazer as respecitivas verificações:

se na lista, a posição 0 do array lista é um (, {, ou um [.

se encontrar um símbolo de fechamento, verifique novammente a posição 0 do array,
 caso seja, a strinnngg estará balanceada

caso não, não está balanceada

'''
# definindo a lista de strings
list_str = []  # começará vazia

# função para verificar se a string está balanceada
def balance_string():
    count = 0  # conta quantos caracteres precisarão ser removidos para balancear
    while True:
        entry = input("\n\t Digite uma string: (ou pare) ").lower()  # entrada do usuário
        if entry == "pare":
            print("\n\t Fim da execução do código...")
            break
        else:
            list_str.append(entry)  # se a entrada não for 'pare', adiciona à lista

        # Pilha para checagem de balanceamento
        stack = []

        # Dicionário de pares de fechamento
        pair = {')': '(', ']': '[', '}': '{'}

        balanced = True  # assume que está balanceada até achar erro

        for char in entry:  # varre caractere por caractere da string
            if char in "({[":  # se for caractere de abertura, empilha
                stack.append(char)
            elif char in ")}]":  # se for de fechamento, verifica se fecha o topo da pilha
                if stack and stack[-1] == pair[char]:  # se o topo da pilha é correspondente
                    stack.pop()
                else:
                    balanced = False
                    count += 1  # precisa de remoção para balancear

        if balanced and not stack:
            print(f"\n\t A string '{entry}' está balanceada!\n\n")  # mensagem quando estiver balanceada
        else:
            print(f"\n\t A string '{entry}' NÃO está balanceada.\n\n")
            # soma o que restou na pilha como caracteres que precisam ser removidos
            count += len(stack)
            print(f"\n\t Para balancear a string inserida, será necessário fazer a remoção de {count} caractere(s)!\n")

        # zera o contador para próxima string
        count = 0

balance_string()
