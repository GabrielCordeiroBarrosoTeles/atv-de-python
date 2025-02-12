## Gabriel Cordeiro
## 6. Função com retorno e uso de listas
##    Crie uma função chamada filtrar_pares que receba uma lista de números inteiros e retorne
##    uma nova lista contendo apenas os números pares.

def filtrar_pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

## Testando a função
if __name__ == "__main__":
    lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filtrar_pares(lista_teste))  # Deve imprimir a lista desse jeito -> [2, 4, 6, 8, 10] :)