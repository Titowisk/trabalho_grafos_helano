# Biblioteca de Grafos
# https://www.python-course.eu/networkx.php
# networkx doc: https://networkx.github.io/documentation/stable/

# Módulo de fora
import networkx as nx
import matplotlib.pyplot as plt 
import os
import pprint
from collections import deque
import math
import time

isWeighted = False
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
    7 - Criar grafo de um arquivo
    8 - Verificar Caminho de Euler
    9 - Exibição dos Graus
    10 - Testar Aresta
    11 - Vértices Adjacentes
    12 - Remover Vértices
    13 - Remover Arestas
    14 - Testar se Grafo é Conexo
    15 - Dijkstra
    16 - Caminhos de Bellman-Ford
    17 - Aplicar Algoritmo de Floyd
    ...
    0 - Sai do programa    
"""

def print_matrix(G):
    M=nx.to_numpy_matrix(G)
    print(M)
    get_user_input("Aperte enter para continuar...")

def add_edges_to_graph(G):
    global isWeighted
    """
    Adiciona arestas aos vértices de origem e destino indicados.
    
    !WARNING! adicionar uma aresta à um grafo sem vértices, faz com que ele crie os vértices automaticamente
    quando o usuário insere o vértice de origem e o vértice de destino
    """

    # TODO verificar se existe um grafo com vértices, para assim poder adicionar as arestas
    print("Insira a quantiade de arestas a serem inseridas")
    edges_quantity = get_user_input()
    count = 0
    while count  < edges_quantity:
        edges_message = """
--- Aresta {} ---
        """.format(count + 1) # TODO mostrar um a lista das arestas já existentes

        print("Insira o vértice de origem")
        edge_origin = get_user_input()
        print("Insira o vértice de destino")
        edge_destiny = get_user_input()
        if isWeighted:
            print("Insira o peso da aresta")
            edge_weight = get_user_input()
            G.add_edge( edge_origin, edge_destiny, weight=edge_weight )
        else:
            G.add_edge( edge_origin, edge_destiny )
        count += 1
    return G

def remove_edge():
    print("Insira o vértice de origem")
    edge_origin = get_user_input()
    print("Insira o vértice de destino")
    edge_destiny = get_user_input()
    try:
        G.remove_edge( edge_origin, edge_destiny )
        print("Aresta removida com sucesso.")
    except:
        print("A Operação falhou.")
        print("Não existe uma aresta entre {a} e {b}".format(a=edge_origin,b=edge_destiny))
    get_user_input("Pressione enter para continuar...")       

def add_nodes_to_graph(G):
    """
    Adiciona vértices ao grafo.
    Essa função sempre recebe um objeto nx.Graph()
    """
    nodes_list = []
    print("Insira a quantidade de vértices a serem inseridos")
    # TODO validar somente números como input do usuário
    nodes_quantity = get_user_input() #transformar a string de input() para int é diferente nas versoes do python 2 e 3
    count = 0
    while count  < nodes_quantity:
        nodes_message = """
Insira o vértice {nodes_quantity}:
        """.format(nodes_quantity = count+1) # TODO mostrar vértices existentes no grafo
        print(nodes_message)
        nodes_list.append(input())
        count += 1
    for x in nodes_list:
        G.add_node(x)
    return G

def remove_node():
    try:
        G.remove_node(get_user_input("Digite o vértice que deseja ser removido, os vertices existentes são :{a}\n".format(a=list(G.nodes))))
        print("A Operação finalizou com sucesso.")  
    except:
        print("A Operação falhou. O Vértice não existe no grafo.")
    finally:
        get_user_input("Aperte enter para continuar...")

def plot_graph():
    """
    Usa o Matplotlib para plotar o grafo.
    """

    nx.draw(G, with_labels=True)
    #plt.savefig("teste.png")  #este comando cria um arquivo png do grafo
    plt.show()


    input('Aperte enter para continuar...')

def get_user_input(default_message="--> "):
    """
    Processa a entrada do usuário.
    Recebe como parâmetro uma mensagem para o input
    """
    user_input = input(default_message)
    if (user_input.isdigit()):
        # se o usuário entrar com número, converte para inteiro
        return int(user_input)
    else:
        # se o usuário entrar com outra coisa, converte a string para mínuscula
        return user_input.lower()

def create_graph(G=False):
    # print("Debug G = {0}".format(G)) 
    """
    Cria um Grafo ou um Dígrafo, conforme escolha do usuário
    """
    introduction_message = """
        Deseja criar que tipo de Grafo?
            1 - Dirigido
            2 - Comum
            3 - Dirigido Ponderado
            4 - Ponderado
            5 - Criar grafo de um arquivo
            0 - Cancelar
    """
    if not G: # se não existir grafo criado
        print(introduction_message)
        graphType = get_user_input()
        global isWeighted

        if graphType == 1:
            G = nx.DiGraph()            
        elif graphType == 2:
            G = nx.Graph()
        elif graphType == 3:
            G = nx.DiGraph()
            isWeighted= True
        elif graphType == 4:
            G = nx.Graph()
            isWeighted = True
        elif graphType == 5:
            G = get_graph_from_file() # irá criar um grafo  
        else:
            print("Operação Abortada.")
    else:
        print("Já existe um grafo criado, deseja apaga-lo para criar outro? (s, sim, n, não)")
        yes_or_no = get_user_input()
        if (yes_or_no in ("s", "sim")): # caso sim
            G = create_graph()    
    
    return G # se G não existir, G = False

def exibir_graus(G):
    print("0 - Grau de um Vértice")
    print("1 - Graus mínimo, médio e máximo")
    # TODO validar somente números como input do usuário
    opcao = get_user_input() #transformar a string de input() para int é diferente nas versoes do python 2 e 3
    if opcao == 0:
        print("Deseja obter o grau de qual Vértice?")
        vertice= get_user_input()
        print("Grau do vértice:")
        print(G.degree(vertice)) # TODO juntar para um print so
        input('Aperte enter para continuar...')
    if opcao == 1:
        vertices_graus= G.degree()
        #valores_graus = dict(vertices_graus).values()
        valores_graus = [v for k, v in vertices_graus]
        media= 0
        qtd_vertices = 0
        grau_min= 100
        grau_max= 0
        for x in valores_graus:
            media+= x
            qtd_vertices+=1
            if grau_min > x:
                grau_min= x
            if grau_max < x:
                grau_max= x
        resultado= media/qtd_vertices
        print("Grau Médio:")
        print(resultado)
        print("Grau Mínimo:")
        print(grau_min)
        print("Grau Máximo:")
        print(grau_max)
        input('Aperte enter para continuar...')
    return

def testar_aresta(G):
    print("Insira a primeira aresta: ")
    aresta_a = get_user_input()
    print("Insira a segunda aresta: ")
    aresta_b = get_user_input()
    arestas= G.number_of_edges(aresta_a, aresta_b)
    if arestas == 0:
        print ("Não existe aresta entre esses vértices.")
        input('Aperte enter para continuar...')
    else:
        #TODO print("Existem {arestas} arestas entre os vértices." .format(arestas))
        print("Número de Arestas: ")
        print(arestas)
        input('Aperte enter para continuar...')
    return

def testar_adjacencia(G):
    print("Insira o vértice: ")
    v = get_user_input()
    vertices_adjacentes= [n for n in G.neighbors(v)]
    print(vertices_adjacentes) #TODO adicionar tratamento para vértice sem adjacêntes
    input('Aperte enter para continuar...')
    return
def get_graph_from_file(G=False):
    """
    Cria um grafo a partir das informações de um arquivo csv
    Estrutura do arquivo csv:
    Delimiter: "|"
    1ª linha: tipo do grafo (grafo, ponderado, dígrafo)
    2ª linha: cabeçalho: vértice|aresta
    3ª ou mais: dados do grafo

    Ex Grafo:
    a|a,b|
    b||
    c|b,c

    Ex Dígrafo:
    a|a,b|
    b||
    a|b,a|  # ordem importa!!
    c|b,c|

    Ex Ponderado:
    a|a,b|0.5
    b||
    c|b,c|1.5

    *Se for um dígrafo a ordem da segunda coluna importa!!
    """

    # caso já exista um grafo
    if G:
        print("Já existe um grafo criado, deseja apaga-lo para criar outro? (s, sim, n, não)")
        yes_or_no = get_user_input()
        if (yes_or_no not in ("s", "sim")):
            return G
    
    # ler a pasta root e ver quais arquivos csv existem
    list_of_files = os.listdir() # lista todos os arquivos dentro da pasta raiz: /trabalho_grafos_helano/
    list_of_csv_files = [file for file in list_of_files if file.endswith(".csv")] # cria uma nova lista apenas com arquivos.csv

    # perguntar qual arquivo csv quer utilizar
    print("Escolha um arquivo para criar o grafo:")
    for i, csv in enumerate(list_of_csv_files):
        print("{arquivo} ({numero})".format(arquivo=csv, numero=i))
    selected_option = get_user_input("Digite uma opção: ")
    selected_file = list_of_csv_files[selected_option]


    # ler o arquivo e criar um dicionário de informações
    graph_type, nodes, edges = parseCsvData(selected_file)

    # criar um grafo a partir do dicionário lido
    
    if (graph_type == "grafo"):
        #cria grafo normal
        G = nx.Graph()
        # G.add_nodes_from(nodes)
        # try:
        #     G.add_edges_from(edges)
        # except TypeError: # TypeError: 'float' object is not iterable -> ocorre quando a aresta é ponderada
        #     G.add_weighted_edges_from(edges)
        
    elif (graph_type in ("dígrafo", "digrafo")):
        # cria dígrafo
        G = nx.DiGraph()
    
    G.add_nodes_from(nodes)
    try:
        G.add_edges_from(edges)
    except TypeError: # TypeError: 'float' object is not iterable -> ocorre quando a aresta é ponderada
        G.add_weighted_edges_from(edges)


    # imprimir o dicionário criado para visualização do usuário
    print_graph_info(G)

    return G

def print_graph_info(G):

    try:
        print("\nGrafo criado ======================")
        print("Vértices: {v}".format(v=G.nodes))
        print("Arestas: {a}".format(a=nx.convert.to_edgelist(G)))
        #Verifica se é conexo ou não
        try:
            if nx.is_connected(G):
                print("Conexo: Sim")
            else:
                print("Conexo: Não")
        except:
            if nx.is_strongly_connected(G):
                print("Conexo: Sim")
            else:
                print("Conexo: Não")
        
    except:
        print("Não há grafo criado")
    

def parseCsvData(file):
    list_of_nodes = []
    list_of_edges = []
    with open(file, 'r', encoding='utf-8') as csv:
        for i, line in enumerate(csv):
            line = line.rstrip("\n")
            if (i == 0):
                graph_type = line.lower()
            elif (i > 1): # i == 1 é cabeçalho
                fields = line.split("|")
                list_of_nodes.append(fields[0]) # fields[0] = "a" node
                # fields[1] = "a,b"; fields[1].split(",") -> ["a", "b"] edge
                # fields[2] = weight
                if (fields[1] != "" and fields[2] != ""):
                    edge = tuple( fields[1].split(",") + [float(fields[2])] )
                    list_of_edges.append(edge)
                elif (fields[1] != ""):
                    edge = tuple( fields[1].split(",") )
                    list_of_edges.append(edge)

    return graph_type, list_of_nodes, list_of_edges

def verify_eulerian_path(G):
    """
    Verifica se existe um caminho de Euler no grafo
    """
    total = 0
    for node in G.nodes:
        if((G.degree(node) % 2) != 0): # se o grau for impar
            total += 1
            if (total > 2):
                break
    if (total > 2):
        print("Não existe um caminho de Euler!")
    else:
        print("Existe um caminho de Euler!")
    get_user_input("Aperte enter para continuar...")

def is_connected():
    try:
        if nx.is_connected(G):
            print("Conexo: Sim")
        else:
            print("Conexo: Não")
    except:
        if nx.is_strongly_connected(G):
            print("Conexo: Sim")
        else:
            print("Conexo: Não")
    get_user_input("Aperte enter para continuar...")

def floyds_algorithm(G):
    """
    Calcula o menor caminho para todos os pares de vértices do grafo.
    Fonte:
    https://www.youtube.com/watch?v=4OQeCuLYj-4
    """
    pp = pprint.PrettyPrinter(indent=4)
    # verifica se o grafo é digrafo e ponderado
    # https://networkx.github.io/documentation/stable/reference/functions.html
    if not ( nx.is_weighted(G)):
        print("O grafo precisa ser ponderado.")
        return  False
    

    # ajusta a matriz para colocar os valores de infinito
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
    M = nx.to_numpy_matrix(G)
    matrix = M.tolist()
    nodes_quantity = len(G)
    nodes_quantity_range = range(nodes_quantity)
    for i in nodes_quantity_range:
        for j in nodes_quantity_range:
            if (i != j and matrix[i][j] == 0):
                matrix[i][j] = float("inf")
    print("\n ============== Matriz com infinitos =============")
    pp.pprint(matrix)

    # algoritmo de floyd
    for k in nodes_quantity_range:
        for i in nodes_quantity_range:
            for j in nodes_quantity_range:
                if(matrix[i][j] > matrix[i][k] + matrix[k][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    print("\n ============== Matriz Floyd =============")    
    pp.pprint(matrix)
    
def bellman_ford_path():
    """
    Retorna o tamanho do menor caminho de um vértice para todos os outros
    """
    source = get_user_input("Escolha o vértice de origem: ")

    if G.is_multigraph():
        weight = lambda u, v, d: min(attr.get("weight", 1) for attr in d.values())
    weight = lambda u, v, data: data.get("weight", 1)

    pred=None
    paths=None
    dist=None
    target=None
    
    for s in source:
        if s not in G:
            raise nx.NodeNotFound("Source {} not in G".format(s))

    if pred is None:
        pred = {v: [] for v in source}

    if dist is None:
        dist = {v: 0 for v in source}

    G_succ = G.succ if G.is_directed() else G.adj
    inf = float('inf')
    n = len(G)

    count = {}
    q = deque(source)
    in_q = set(source)
    while q:
        u = q.popleft()
        in_q.remove(u)

        # Skip relaxations if any of the predecessors of u is in the queue.
        if all(pred_u not in in_q for pred_u in pred[u]):
            dist_u = dist[u]
            for v, e in G_succ[u].items():
                dist_v = dist_u + weight(v, u, e)

                if dist_v < dist.get(v, inf):
                    if v not in in_q:
                        q.append(v)
                        in_q.add(v)
                        count_v = count.get(v, 0) + 1
                        if count_v == n:
                            raise nx.NetworkXUnbounded(
                                "Negative cost cycle detected.")
                        count[v] = count_v
                    dist[v] = dist_v
                    pred[v] = [u]

                elif dist.get(v) is not None and dist_v == dist.get(v):
                    pred[v].append(u)

    if paths is not None:
        dsts = [target] if target is not None else pred
        for dst in dsts:

            path = [dst]
            cur = dst

            while pred[cur]:
                cur = pred[cur][0]
                path.append(cur)

            path.reverse()
            paths[dst] = path

    length = dict(dist)

    for node in G.nodes:
        print('{}: {}'.format(node, length[node]))
    get_user_input("Aperte enter para continuar...")

'https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm'
'Deve retornar menor caminho entre source e target, contando quantas interações ocorreram e quanto tempo levou para executar.'
'https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/shortest_paths/weighted.html baseado em _dijkstra_multisource'
def dijkstra(G): 
    inicio = input("Qual o vertice inicial?\n")   
    destino = input("Qual o vertice destino?\n")   
    Matrix = nx.to_numpy_matrix(G)
    Nodes = list(G)
    #IN
    Visto = list()
    Visto.append(Nodes[Nodes.index(inicio)])
    #d
    distancia = list()
    distancia = [math.inf] * (len(Nodes))
    #-1 para representar nulo
    distancia[Nodes.index(inicio)] = -1
    #s
    path = list()
    path = [None] * (len(Nodes))

    currentNode = Visto[0]
    #tempo inicial de execuçao
    StartTime = time.time()
    #Contador de iteracoes
    iteracoes = 0

    while destino not in Visto:
        menorDistVizinho = math.inf
        nextNode = None
        #preenche as distancias e escolhe o vizinho com menor distancia dos vizinhos 
        for vizinho in G.neighbors(currentNode):
            if vizinho in Visto:
                continue
                
            dist = Matrix[Nodes.index(currentNode),Nodes.index(vizinho)]

            dist = min(dist + int(distancia[Nodes.index(currentNode)]), distancia[Nodes.index(vizinho)])
            if dist < distancia[Nodes.index(vizinho)]:
                distancia[Nodes.index(vizinho)] = dist
                path[Nodes.index(vizinho)] = currentNode
            if(dist < menorDistVizinho):
                menorDistVizinho = dist
                nextNode = vizinho

        currentNode = nextNode
        Visto.append(currentNode)
        #Nova Iteração se destino ainda nao foi lido
        iteracoes = iteracoes + 1

    #tempo final de execucao
    EndTime = time.time()

    #Constroi o menor caminho
    shortestPath = list()
    nextNode = destino
    shortestPath.append(nextNode)
    print(nextNode)
    while inicio not in shortestPath:        
        shortestPath.append(path[Nodes.index(nextNode)])  
        nextNode = path[Nodes.index(nextNode)]

    shortestPath.reverse()
    print("O Caminho mais curto através do algoritmo de Dijkstra foi:\n")
    print(shortestPath)
    print("Tempo de Execução:" + str(EndTime-StartTime))
    print("Iterações:" + str(iteracoes))


def optionAction(option, G):
    """
    Gerencia as ações a serem tomadas conforme opção escolhida pelo usuário
    """
    option = get_user_input() # retorna inteiro se o usuário insere números

    if option == 1: # Imprime um grafo
        plot_graph()
        

    elif option == 2: # adiciona vértices
        # verifica se existe um grafo, para assim poder adicionar os vértices
        G = add_nodes_to_graph(G)
        
        
    elif option == 3: # adiciona arestas
        G = add_edges_to_graph(G)
        
        
    elif option == 4: # imprime matriz
        # verifica se existe um grafo e imprime uma matriz representativa
        print_matrix(G)
        
        
    elif option == 5: # imprime dicionário de grafos
        # verifica se exuste um grafo e imprime um dicionário representativo
        pass

    elif option == 6: # Cria um Novo Grafo
        G = create_graph(G)

    elif option == 7: # ler grafo de um arquivo
        G = get_graph_from_file(G)
        
    elif option == 8: # verifica se existe um caminho de euler
        verify_eulerian_path(G)

    elif option == 9: # Menu de Graus
        exibir_graus(G)
    
    elif option == 10:
        testar_aresta(G)

    elif option == 11:
        testar_adjacencia(G)
    
    elif option == 12:
        remove_node()
    
    elif option == 13:
        remove_edge()

    elif option == 14:
        is_connected()

    elif option == 15:
        dijkstra(G)

    elif option == 16:
        bellman_ford_path()
    # ...
    elif option == 17:
        floyds_algorithm(G)

    return option, G

# ==== MAIN ======

#Inicializa o primeiro Grafo
G = create_graph()

#Inicializa o Menu de Operações do Grafo
while option != 0:
    
    print(menu)
    option, G = optionAction(option, G) # if option == 0 irá sair do while loop
