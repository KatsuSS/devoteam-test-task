import sys

from typing import Dict, List
from collections import defaultdict


def get_graph_communication(communications: List) -> Dict:
    graph_info = defaultdict(list)
    general_res = defaultdict(lambda: defaultdict(int))
    min_coms, max_coms, total = sys.maxsize, 0, 0

    for com in communications:
        graph_info[com['initiator_user']].append({'user': com['acceptor_user'], 'total': com['total']})
        general_res[com['initiator_user']]['total'] += com['total']
    for val in general_res.values():
        temp_total = val['total']
        total += temp_total
        max_coms = max(max_coms, temp_total)
        min_coms = min(min_coms, temp_total)

    graph_info.update({
        'min_coms': min_coms,
        'max_coms': max_coms,
        'avg_coms': total // len(general_res),
    })
    return graph_info
