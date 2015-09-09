import time
from site_map import SiteMap
from sm_url import SiteMapURL
from multiprocessing import Pool, Queue
import json


def parent_worker(parent):
    smu = SiteMapURL(parent)
    try:
        node_set = set()
        edge_set = set()
        for child in smu.children(sm.commons):
            for c in child.get_children(sm.commons):
                node_set.add(c.url)
                sm.add_parent_node(smu.url, c.url)
                edge_set.add((child.url, c.url))
        parent_worker.q.put({'nodes': node_set, 'edges': edge_set})
    except IndexError:
        pass


def parent_worker_init(q):
    parent_worker.q = q


def to_file(sm_map):
    json_map = json.dumps({"nodes": list(sm_map['nodes']), "edges": list(sm_map['edges'])})
    with open('map.json', 'w') as f:
        f.write(json_map)


sm = SiteMap("sitemap.xml")

if __name__ == "__main__":
    parents = sm.iget_parents()
    q = Queue()
    pool = Pool(8, parent_worker_init, [q])
    pool.map_async(parent_worker, parents)
    while time.clock() < 600:
        if not q.empty():
            partial_map = q.get()
            sm.map["nodes"].update(partial_map["nodes"])
            sm.map["edges"].update(partial_map["edges"])
    to_file(sm.map)