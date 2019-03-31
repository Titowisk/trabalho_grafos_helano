# Biblioteca de Grafos
# https://www.python-course.eu/networkx.php

# Módulo nativo
import argparse

# Módulo de fora
import networkx as nx

option = -1
menu = """
    Trabalho de Grafos da equipe: Lucas, Lucas, Rafael e Vitor

    Escolha uma das opções a seguir:

    1 - Criar um Grafo
    2 - Adicionar vértices
    3 - Adicionar arestas:
    4 - Imprimir Matriz
    5 - Imprimir Dicionário de Grafos
    ...
    0 - Sai do programa    
"""

def optionAction(option):
    """
    Gerencia as ações a serem tomadas conforme opção escolhida pelo usuário
    """
    option = int(option) # converte a string recebida no input para inteiro

    if option == 1: # Cria um grafo vazio
        
        G=nx.Graph()

        print("Grafo criado:")
        print( "Vértices: {0}".format( G.nodes() ) )
        print( "Arestas: {0}".format(G.edges()))
        input('Aperte enter para continuar...')

    elif option == 2: # adiciona vértices
        # verifica se existe um grafo, para assim poder adicionar os vértices
        pass
    elif option == 3: # adiciona arestas
        # verifica se existe um grafo com vértices, para assim poder adicionar as arestas
        pass
    elif option == 4: # imprime matriz
        # verifica se existe um grafo e imprime uma matriz representativa
        pass
    elif option == 5: # imprime dicionário de grafos
        # verifica se exuste um grafo e imprime um dicionário representativo
        pass
    # ...

    return option


while option != 0:
    print(menu)
    option = input('--> ')

    option = optionAction(option) # if option == 0 irá sair do while loop
