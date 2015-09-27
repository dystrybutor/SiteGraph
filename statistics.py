import json
import networkx as nx
import operator
import matplotlib.pyplot as plt


def read_json(name):
    with open(name, 'r') as f:
        return json.loads(f.read())


site_map = read_json('map2.json')
g = nx.DiGraph()
p = nx.Graph()
g.add_nodes_from(site_map['nodes'])
g.add_edges_from(site_map['edges'])
p.add_nodes_from(site_map['nodes'])
p.add_edges_from(site_map['edges'])

xx = nx.connected_components(p)
_ = xx.next()
to_remove = xx.next()

print sorted(g.degree().items(), key=operator.itemgetter(1), reverse=True)
print sorted(g.in_degree().items(), key=operator.itemgetter(1), reverse=True)
print sorted(g.out_degree().items(), key=operator.itemgetter(1), reverse=True)

g.remove_nodes_from(to_remove)
p.remove_nodes_from(to_remove)


# print nx.shortest_path(g, p1, p2)


# nx.draw(g)  # networkx draw()
# plt.draw()  # pyplot draw()

# nx.draw_networkx_edges(p, pos=nx.spring_layout(p))
nx.draw_networkx(p)
plt.show()
pass