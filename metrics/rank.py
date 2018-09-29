import random as rand
import scipy.stats as stats


def random_rank_comp(rank, comp_rank):
    sum_rank = set(rank + comp_rank)
    comp_result = list((sum_rank - set(rank)))
    rand.shuffle(comp_result)
    return comp_result


def compare_network_ranks(first_rank, second_rank):
    first_rank.extend(random_rank_comp(first_rank, second_rank))
    second_rank.extend(random_rank_comp(second_rank, first_rank))
    return stats.kendalltau(first_rank, second_rank)


def keys_sorted_by_values(items, reverse=True):
    return sorted(items, key=items.get, reverse=reverse)


class Rank(object):

    def __init__(self, net):
        self._net = net

    def calc_rank(self, func_data):
        func, total_func = func_data
        if total_func:
            return keys_sorted_by_values(func(self._net))
        else:
            rank = {}
            for node in self._net.available_nodes():
                rank[node] = func(self._net, node)
            return keys_sorted_by_values(rank)
