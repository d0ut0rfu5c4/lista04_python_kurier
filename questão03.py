# Desenvolva uma função que realize compressão de string usando contagem de caracteres consecutivos ("aaabb" → "a3b2").
 
def compress_string(text):
    if not text:
        return ""
    
    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    # Adiciona o último grupo de caracteres
    result += text[-1] + str(count)

    return result

# Testando
string = 'acccccccccwwwwwhh'
compress = compress_string(string)
print(compress)  # Saída esperada: 'a2b5c1'




