import matplotlib.pyplot as plt
import networkx as nx

class Graphorizor:
    def __init__(self):
        G = nx.Graph()  # create graph object
        # define list of nodes (node IDs)
        nodes = [1, 2, 3, 4, 5]
        # define list of edges
        # list of tuples, each tuple represents an edge
        # tuple (id_1, id_2) means that id_1 and id_2 nodes are connected with an edge
        edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]
        # add information to the graph object
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        # draw a graph and show the plot
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.title('hercules with middle finger circa 69x')
        plt.show()