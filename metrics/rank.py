import random as rand

import scipy.stats as stats

from utils import keys_sorted_by_values
from pylog import *


def random_rank_complement(rank, complementary_rank):
    sum_rank = set(rank + complementary_rank)
    complement = list((sum_rank - set(rank)))
    rand.shuffle(complement)
    return complement


@try_catch_log('Comparing %0 to %1', print_result=True)
def compare_network_ranks(first_rank, second_rank,
                          compare_method=stats.kendalltau):
    first_rank.extend(random_rank_complement(first_rank, second_rank))
    second_rank.extend(random_rank_complement(second_rank, first_rank))
    return compare_method(first_rank, second_rank)


@try_catch_log('Calculating rank with %1 for all nodes: %2', print_result=True, prog=False)
def calc_rank(net, metric_func, metric_func_for_all_nodes=False):
    if metric_func_for_all_nodes:
        return keys_sorted_by_values(metric_func(net))
    else:
        rank = {}
        for node in net.available_nodes():
            rank[node] = metric_func(net, node)
        return keys_sorted_by_values(rank)
