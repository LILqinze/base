def keys_sorted_by_values(items, reverse=True):
    return sorted(items, key=items.get, reverse=reverse)
