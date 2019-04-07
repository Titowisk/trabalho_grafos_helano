# Biblioteca de Grafos
# https://www.python-course.eu/networkx.php
# networkx doc: https://networkx.github.io/documentation/stable/

# Módulo de fora
import networkx as nx
import matplotlib.pyplot as plt 

option = -1
menu = """
    Trabalho de Grafos da equipe: André, Lucas, Lucas, Rafael

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

def get_user_input():
    """
    Processa a entrada do usuário
    """
    user_input = input('--> ')
    if (user_input.isdigit()):
        # se o usuário entrar com número, converte para inteiro
        return int(user_input)
    else:
        # se o usuário entrar com outra coisa, converte a string para mínuscula
        return user_input.lower()

def create_graph(G=False):
    """
    Cria um Grafo ou um Dígrafo, conforme escolha do usuário
    """
    introduction_message = """
        Deseja criar que tipo de Grafo?
            1 - Dirigido
            2 - Comum
            0 - Cancelar
    """
    if not G: # se não existir grafo criado
        print(introduction_message)
        graphType = get_user_input()
        if graphType == 1:
            G = nx.DiGraph()
            
        elif graphType == 2:
            G = nx.Graph()
            
        else:
            print("Operação Abortada.")
    else:
        print("Já existe um grafo criado, deseja apaga-lo para criar outro ?")
        yes_or_no = get_user_input()
        if (yes_or_no in ("s", "sim")): # caso sim
            G = create_graph()    
    
    return G # se G não existir, G = False

def optionAction(option):
    """
    Gerencia as ações a serem tomadas conforme opção escolhida pelo usuário
    """
    option = get_user_input() # retorna inteiro se o usuário insere números

    if option == 1: # Imprime um grafo
        nx.draw(G, with_labels=True)
        #plt.savefig("teste.png")  #este comando cria um arquivo png do grafo
        plt.show()


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
        G = create_graph(G)
            
        
    # ...

    return option

# ==== MAIN ======

#Inicializa o primeiro Grafo
G = create_graph()

#Inicializa o Menu de Operações do Grafo
while option != 0:
    
    print(menu)
    option = optionAction(option) # if option == 0 irá sair do while loop
