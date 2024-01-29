#!/usr/bin/env python3
#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
_version_ = "0.1.1"

########################################################
#      ATENçÃO: MODIFIQUE ESSE CÓDIGO!                 #
#   Tente utilizar dicionários onde achar conveniente  #
########################################################

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": aula_ingles,
    "Música": aula_musica,
    "Dança": aula_danca,
}


# Listar alunos em cada atividade por sala

for nome_atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividades[nome_atividade])
    atividade_sala2 = set(sala2) & set(atividades[nome_atividade])

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
