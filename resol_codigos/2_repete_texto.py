# 2. **Repetindo Textos ✏️**
#    - Quer repetir uma string várias vezes? Basta nos dar uma string e um número inteiro, e nós cuidaremos do resto! A repetição nunca foi tão fácil.

def repetir_string(string, vezes):
    resultado = ""
    for _ in range(vezes):
        resultado += string
        print(resultado[len(resultado) - len(string):])
    return resultado