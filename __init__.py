from site_map import SiteMap
from sm_url import SiteMapURL
from multiprocessing import Pool, Queue

def parent_worker(parent):
    smu = SiteMapURL(parent)
    try:
        node_list = []
        edge_list = []
        for child in smu.children(sm.commons):
            node_list.append(child.url)
            print child
            for c in child.get_children(sm.commons):
                sm.add_parent_node(smu.url, c.url)
                edge_list.append({'source':child.url, 'target':c.url})
        parent_worker.q.put({'nodes':node_list, 'edges':edge_list})
    except IndexError:
        pass

def parent_worker_init(q):
    parent_worker.q = q

sm = SiteMap("sitemap.xml")

if __name__ == "__main__":
    parents = sm.iget_parents()
    q = Queue()
    pool = Pool(8, parent_worker_init, [q])
    pool.map_async(parent_worker, parents)
    print 10
    while True:
        sm.map.update(q.get())


