import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(individual):
    edges = []
    for index in range(0, len(individual.chromossomes) - 1):
        edges.append((individual.chromossomes[index].name, individual.chromossomes[index + 1].name))
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    pos = {}
    for chromossome in individual.chromossomes:
        pos[chromossome.name] = (chromossome.x, chromossome.y) 
    nx.draw_networkx(graph, pos=pos)
    return graph

def show_graph(graph):
    plt.show()

def build_graph(individual):
    graph = create_graph(individual)
    show_graph(graph)
