import os
from urlparse import urlparse
import requests
from page_content_parser import PageContentParser


class WebPageWrapper(object):
    def __init__(self, url):
        # print url
        self.url = url
        self.robot_exclusion = ["local/", "ecrire", "extensions/", "lib/", "plugins/", "prive/",
                                   "squelettes-dist/", "squelettes/", "Files/", "IMG/", "/libraries", "menu-footer/",
                                   "menu-cache/"]

        self.url_path = self._get_url_path_if_exists_or_raise_name_error()
        self.content = self._download_page_content()
        self._save_content_to_file()

    def create_not_existing_direcotries(self, filename):
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

    def _save_content_to_file(self):
        filename = os.path.join("htmls", self.url_path)
        self.create_not_existing_direcotries(filename)
        with open(filename + ".html", 'w') as f:
            f.write(self.content)

    def _download_page_content(self):
        ret = requests.get(self.url)
        return ret.content

    def get_children(self, commons):
        pgp = PageContentParser(self.content, self.url)
        for url in pgp.get_urls_that_belong_to_domain_as_set():
            if self.url == url:
                continue
            elif url in commons:
                yield url
            try:
                yield WebPageWrapper(url)
            except NameError as e:
                # print e
                pass

    def _get_url_path_if_exists_or_raise_name_error(self):
        path = urlparse(self.url).path
        if path.startswith("/"):
            path = path[1:]
        if path.endswith("/"):
            path = path[:-1]
        if path in ["", "/", "\\"]:
            raise NameError("URL has no path!!!")
        elif "php?action" in self.url:
            raise NameError("This triggers php event!!!")
        elif "mailto:" in self.url:
            raise NameError("This is an email!!!")
        elif filter(path.__contains__, self.robot_exclusion):
            raise NameError("This page is excluded")
        else:
            return path
