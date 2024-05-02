def verificar_palindromo(palavra):
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Verifica se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False