# PAths in a NxN grid

_paths_dict = {}
def enum_paths(i,j):
    if _paths_dict.get((i,j)):
        return _paths_dict[(i,j)]
    if i == 1 or j ==1:
        return 1
    else:
        _paths = enum_paths(i, j-1) + enum_paths(i-1, j)
    _paths_dict[(i,j)] = _paths
    return _paths

_paths = {}
def print_paths(i,j):
    print (i,j),
    if i == 1 or j ==1 :
        print
    else:
        print_paths(i-1,j)
        print_paths(i, j-1)

print_paths(5,5)