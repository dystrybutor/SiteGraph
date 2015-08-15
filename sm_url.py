from web_page_wrapper import WebPageWrapper


class SiteMapURL(object):
    def __init__(self, url):
        self.page = WebPageWrapper(url)
        self.url = url
        self.nodes = set()

    def add_nodes(self, nodes):
        self.nodes.add(nodes)

    def get_new_nodes(self, nodes):
        return self.nodes.intersection(nodes)

    def children(self, commons):
        return self.page.get_children(commons)