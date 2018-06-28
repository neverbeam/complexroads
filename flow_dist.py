import networkx as nx
import matplotlib.pyplot as plt
from numpy import var
names = [
    "africa",
    "australia",
    "europa",
    "newzealand",
    "northamerica",
    "UK",
    "road",
    "smallworld",
    "erdos",
    "scalefree"
]

paths = ['./Graph_GPickles/' + x + '_FinalResult.gpickle' for x in names]

for name, path in zip(names, paths):
    G = nx.read_gpickle(path)
    flows = list(dict(nx.get_edge_attributes(G, 'flow')).values())
    print(name, var(flows))
    plt.hist(flows, bins = 24, range=(0,6))
    plt.title(name)
    plt.xlabel('Capacity')
    plt.ylabel('Number of roads')
    plt.show()