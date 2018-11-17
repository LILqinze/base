
def keys_sorted_by_values(items, reverse=True):
    return sorted(items, key=items.get, reverse=reverse)

def file_format(filepath):
    return filepath.split('.')[-1]

def filename_without_format(filepath):
    return '.'.join(filepath.split('.')[:-2])

def filename_from_path(filepath):
    return filepath.split('/')[-1]

def file_parent_dir(filepath):
    return '/'.join(filepath.split('/')[:-1])
