## Gabrielly
# ## 2. Função com múltiplos parâmetros
## Crie uma função chamada media que receba três números como parâmetros e retorne a
## média aritmética deles.

def media_aritmetica (a,b,c):
    media= (a+b+c)/3
    return media

a=int(input("Digite um número:"))
b=int(input("Digite um número:"))
c=int(input("Digite um número:"))
print(media_aritmetica(a,b,c))