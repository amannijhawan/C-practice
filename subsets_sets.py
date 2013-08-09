_subsets =[] 
def subsets_set(s):
    s = set(s)
    news = set(s)
    for item in news:
        _subsets.append(set([item]))
        s.remove(item)
        _subsets.append(set([item]).add(subsets_set(s)))

subsets_set([3,2,1])
print _subsets
        
