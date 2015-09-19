import urlparse
from bs4 import BeautifulSoup
from domainchecker import DomainChecker


class PageContentParser(object):
    def __init__(self, content, content_url):
        self.content = content
        self.base_url = self._get_base_url()
        self.content_url = content_url

    def iget_urls_that_belong_to_domain(self):
        soup = BeautifulSoup(self.content)
        urls = soup.findAll('a', href=True)
        for url in [x['href'] for x in urls]:
            url = self._do_links(url)
            if DomainChecker.belong_to_domain(url):
                yield url

    def get_urls_that_belong_to_domain_as_set(self):
            return set(self.iget_urls_that_belong_to_domain())

    def _get_base_url(self):
        soup = BeautifulSoup(self.content)
        return soup.findAll('base', href=True)[0]['href']

    def _do_links(self, url):
        if url.startswith("/"):
            return urlparse.urljoin(self.base_url, url)
        elif not url.startswith(("http", "www")):
            return urlparse.urljoin(self.content_url, url)
        else:
            return url