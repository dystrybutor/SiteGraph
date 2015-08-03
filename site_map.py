from bs4 import BeautifulSoup


class SiteMap(object):
    def __init__(self, sitemap_xml):
        self.parents = None

        with open(sitemap_xml) as site_map:
            soup = BeautifulSoup(site_map, "html.parser")
            self.parents = {x.contents[0]: set() for x in soup.find_all('loc')[1:]}

    def set_parent_nodes(self, key, value):
        self.parents[key] = value

    def iget_parents(self):
        for p in self.parents:
            yield p