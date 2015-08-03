from site_map import SiteMap
from sm_url import SiteMapURL

if __name__ == "__main__":
    sm = SiteMap("sitemap.xml")
    parents = sm.iget_parents()

    smu = SiteMapURL(parents.next())

    for child in smu.children():
        for c in child.get_children():
            pass