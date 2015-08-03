class DomainChecker(object):
    @staticmethod
    def belong_to_domain(url):
        if "paris-sorbonne.fr" in url:
            return True
        elif not str(url).startswith(("http", "www")):
            return True

