"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC9
"""


x = int(input())
y = x*2

print(y, "minutos")

"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 2 - AC9
"""

def Fatorial(n):
    if(F[n] == -1):
        F[n] = Fatorial(n - 1) * n
    return F[n]


F = [-1 for _ in range(14)]
F[0] = 1

N = int(input())

print(Fatorial(N))

"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 3 - AC9
"""

N = int(input())

for _ in range(N):
    M = int(input())

    precos = {}

    for _ in range(M):
        fruta, preco = input().strip().split(' ')

        precos[fruta] = float(preco)

    P = int(input())

    resposta = 0.0
    for _ in range(P):
        fruta, quantidade = input().strip().split(' ')

        resposta += int(quantidade) * precos[fruta]

    print(f'R$ {resposta:.2f}')

"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 4 - AC9
"""



"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 5 - AC9
"""



"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 6 - AC9
"""




"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 7 - AC9
"""




"""
Programação Estruturada
2024.1
06/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 8 - AC9
"""