from bs4 import BeautifulSoup


class SiteMap(object):
    def __init__(self, sitemap_xml):
        self.parents = None
        self.map = {"nodes": set(), "edges": set()}

        with open(sitemap_xml) as site_map:
            soup = BeautifulSoup(site_map, "html.parser")
            self.parents = {x.contents[0]: set() for x in soup.find_all('loc')[1:]}

        self.commons = self.parents.keys()

    def add_parent_nodes(self, key, nodes):
        self.parents[key].update(nodes)

    def add_parent_node(self, key, node):
        self.parents[key].add(node)

    def iget_parents(self):
        for p in self.parents:
            yield p