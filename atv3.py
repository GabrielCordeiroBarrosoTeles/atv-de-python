## Arthur Menezes
# ## 3. Utilizando módulos
## Crie um módulo chamado operacoes.py que contenha uma função subtrair(a, b). Depois,
## importe esse módulo em outro arquivo e use a função para calcular 10 - 4.

import operacoes
a=int(input("digite seu primeiro numero: "))
b=int(input("digite seu segundo numero: "))
print(f"o resultado da subtracao desses numeros e igual a: {operacoes.subtrair(a,b)}")
