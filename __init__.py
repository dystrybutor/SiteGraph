from site_map import SiteMap
from sm_url import SiteMapURL

if __name__ == "__main__":
    sm = SiteMap("sitemap.xml")
    parents = sm.iget_parents()

    for parent in parents:
        smu = SiteMapURL(parent)
        for child in smu.children(sm.commons):
            for c in child.get_children(sm.commons):
                sm.add_parent_node(smu.url, c.url)
    pass