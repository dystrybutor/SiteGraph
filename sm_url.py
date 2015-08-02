from web_page_wrapper import WebPageWrapper


class SiteMapURL(object):
	def __init__(self, url):
		p = WebPageWrapper(url)
		self._children = p.get_children()
		self.nodes = set()

	def add_nodes(self, nodes):
		self.nodes.add(nodes)

	def get_new_nodes(self, nodes):
		return self.nodes.intersection(nodes)

	def children(self):
		return self._children