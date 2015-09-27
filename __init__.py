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
        for child in [c for c in smu.children(sm.commons) if not isinstance(c, unicode)]:
            for c in child.get_children(sm.commons):
                if isinstance(c, unicode):
                    edge_set.add((child.url, c))
                else:
                    node_set.add(c.url)
                    sm.add_parent_node(smu.url, c.url)
                    edge_set.add((child.url, c.url))
        parent_worker.q.put({'nodes': node_set, 'edges': edge_set})
    except IndexError as e:
        print e
    except Exception as e:
        print e


def parent_worker_init(q):
    parent_worker.q = q


def to_file(sm_map):
    json_map = json.dumps({"nodes": list(sm_map['nodes']), "edges": list(sm_map['edges'])})
    with open('map2.json', 'w') as f:
        f.write(json_map)


sm = SiteMap("sitemap.xml")

if __name__ == "__main__":
    parents = sm.iget_parents()
    q = Queue()
    pool = Pool(8, parent_worker_init, [q])
    result = pool.map_async(parent_worker, parents)
    while time.clock() < 600:
        if not q.empty():
            partial_map = q.get()
            sm.map["nodes"].update(partial_map["nodes"])
            sm.map["edges"].update(partial_map["edges"])
    to_file(sm.map)