# Biblioteca de Grafos
# https://www.python-course.eu/networkx.php

# Módulo nativo
import argparse

# Módulo de fora
import networkx as nx
import matplotlib.pyplot as plt 

G=nx.Graph() #grafo

option = -1
menu = """
    Trabalho de Grafos da equipe: Lucas, Lucas, Rafael e Vitor

    Escolha uma das opções a seguir:

    1 - Exibir Grafo
    2 - Adicionar vértices
    3 - Adicionar arestas
    4 - Imprimir Matriz
    5 - Imprimir Dicionário de Grafos
    6 - Criar um Novo Grafo
    ...
    0 - Sai do programa    
"""

def optionAction(option):
    """
    Gerencia as ações a serem tomadas conforme opção escolhida pelo usuário
    """
    option = int(option) # converte a string recebida no input para inteiro
    global G

    if option == 1: # Cria um grafo vazio
                
        nx.draw(G, with_labels=True)
        #plt.savefig("teste.png")  #este comando cria um arquivo png do grafo
        plt.show()

        #G=nx.Graph() #grafo6
        #print("Grafo criado:")
        #print( "Vértices: {0}".format( G.nodes() ) )
        #print( "Arestas: {0}".format(G.edges()))

        input('Aperte enter para continuar...')

    elif option == 2: # adiciona vértices
        # verifica se existe um grafo, para assim poder adicionar os vértices
        vertices= []
        print("Insira a quantidade de vértices a serem inseridos")
        i= int(input()) #transformar a string de input() para int é diferente nas versoes do python 2 e 3
        cont= 0
        while cont < i:
            print("Insira o vértice %d" % (cont+1)) #a funcao print() pode ser diferente a depender da versao do python no PC
            vertices.append(input())
            cont+=1
        for x in vertices:
            G.add_node(x)
        pass
    elif option == 3: # adiciona arestas
        # verifica se existe um grafo com vértices, para assim poder adicionar as arestas
        print("Insira a quantiade de arestas a serem inseridas")
        i= int(input())
        cont= 0
        while cont < i:
            print("--- Aresta %d ---" % (cont+1))
            print("Insira o vértice de origem")
            x= input()
            print("Insira o vértice de destino")
            y= input()
            G.add_edge(x, y)
            cont+=1
        pass
    elif option == 4: # imprime matriz
        # verifica se existe um grafo e imprime uma matriz representativa
        M=nx.to_numpy_matrix(G)
        print(M)
        input('Aperte enter para continuar...')
        pass
    elif option == 5: # imprime dicionário de grafos
        # verifica se exuste um grafo e imprime um dicionário representativo
        pass

    elif option == 6: # Cria um Novo Grafo
        print("""Deseja criar que tipo de Grafo?
        1 - Ponderado
        2 - Não Ponderado""")
        graphType = int(input('--> '))
        if graphType == 1:
            G = nx.DiGraph()
            pass
        elif graphType == 2:
            G = nx.Graph()
            pass
        else:
            print("Operação Abortada.")
            pass
        pass
    # ...

    return option

#Inicializa o primeiro Grafo
print("""Escolha o tipo de Grafo que deseja Trabalhar:
    1 - Ponderado
    2 - Não Ponderado""")
graphType = int(input('--> '))
if graphType == 1:
    G = nx.DiGraph()
    pass
elif graphType == 2:
    G = nx.Graph()
    pass
pass

#Inicializa o Menu de Operações do Grafo
while option != 0:
    
    print(menu)
    option = input('--> ')

    option = optionAction(option) # if option == 0 irá sair do while loop
