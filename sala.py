#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
_version_ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [aula_ingles ,aula_muica , aula_danca]

atividades_1 = []
atividades_2 = []

for atividade in atividades:
    for aluno in atividade:
        if aluno in sala1:
            atividades_1.append(aluno)
        elif aluno in sala2:
            atividades_2.append(aluno)

print("alunos que fazem atividades na sala 1"atividades_1)
print("alunos que fazem atividades na sala 2"atividades_2)
            
