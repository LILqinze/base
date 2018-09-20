#!/usr/bin/env python3
try:
    from pylog import *
except:
    print("Please, checkout pylog library from git submodule")
    exit(-1)

try:
    inf("Checking networkx", True)
    import networkx

    ok()
except:
    err("There's no networkx")
