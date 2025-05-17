# Escreva uma função que substitua cada letra de uma string pela próxima letra do alfabeto.

# Dicionário com as letras do alfabeto
alfabeto = {
    'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
    'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
    'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
    'z': 'a'
}

def substituir_por_proxima_letra(texto):
    resultado = ""
    for letra in texto:
        if letra.lower() in alfabeto:
            proxima = alfabeto[letra.lower()]
            # Mantém a capitalização original
            if letra.isupper():
                resultado += proxima.upper()
            else:
                resultado += proxima
        else:
            resultado += letra  # Mantém espaços, números ou símbolos
    return resultado

# Entrada do usuário
entrada = input("Digite uma frase: ")
saida = substituir_por_proxima_letra(entrada)
print("Resultado:", saida)
