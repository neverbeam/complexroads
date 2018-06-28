import networkx as nx
import matplotlib.pyplot as plt
names = [
    "africa",
    "australia",
    "europa",
    "newzealand",
    "northamerica",
    "UK",
    "road"
]

paths = ['./Graph_GPickles/' + x + '_FinalResult.gpickle' for x in names]

for name, path in zip(names, paths):
    G = nx.read_gpickle(path)
    flows = dict(nx.get_edge_attributes(G, 'flow')).values()
    plt.hist(list(flows), bins = 24, range=(0,6))
    plt.title(name)
    plt.show()