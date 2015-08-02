import requests
from page_content_parser import PageContentParser


class WebPageWrapper(object):
	def __init__(self, url):
		print url
		self.url = url
		self.content = self._download_page_content()
		self.children = set(self._set_children())
		self._save_content_to_file()

	def _save_content_to_file(self):
		file_name = self.url.replace('/', "")
		with open(file_name, 'w') as f:
			f.save()

	def _download_page_content(self):
		ret = requests.get(self.url)
		return ret.content

	def _set_children(self):
		pgp = PageContentParser(self.content, self.url)
		for url in pgp.get_urls_that_belong_to_domain_as_set():
			if self.url == url:
				continue
			wpw = WebPageWrapper(url)
			yield wpw

	def get_children(self):
		return self.children
