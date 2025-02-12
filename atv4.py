## Gabreil Cordeiro
## 4. Parâmetro opcional
## Crie uma função chamada cumprimentar que receba um nome e um parâmetro opcional
## saudacao (padrão: "Olá"). A função deve exibir a saudação seguida do nome.
## Exemplo de uso:
## cumprimentar("Ana") # Saída: Olá, Ana
## cumprimentar("Carlos", "Bom dia") # Saída: Bom dia, Carlos

def cumprimentar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}")

cumprimentar("Ana")               
cumprimentar("Carlos", "Bom dia")  
