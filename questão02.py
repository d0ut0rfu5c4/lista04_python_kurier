# Implemente uma função que verifique se duas strings são anagramas, ignorando espaços e diferenças de caixa.

def verifying_anagrams():
    # Solicitando as palavras ao usuário
    word = input("\n\tInsert the first word: ").replace(" ", "").lower()
    word_2 = input("\n\tInsert the second word: ").replace(" ", "").lower()

    # Imprime o que o usuário digitou
    print(f"\nYou entered:\n\tWord 1: {word}\n\tWord 2: {word_2}")

    # Verifica se são anagramas
    if sorted(word) == sorted(word_2):
        print("\n The words are anagrams!")
    else:
        print("\n The're NOT anagrams.")

# Chamada da função
verifying_anagrams()

