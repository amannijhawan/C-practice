import time


class Value(object):

    def __init__(self, value):
        self.time = time.time()
        self._value = value

    @property
    def value(self):
        self.time = time.time()
        return self._value

    @value.setter
    def value(self, value):
        self.time = time.time()
        self._value = value


def cmp_values(item1, item2):
    return item1[1].time < item2[1].time


class LRUCache(object):

    def __init__(self, size=200, **kwargs):
        self.size = size
        self._dict = {}

    def __setitem__(self, key, value):
        val = Value(value)

        if key not in self._dict:
            if len(self._dict) > self.size:
                self.free_up_space()
        val = Value(value)
        self._dict[key] = val

    def __getitem__(self, key):
        val = self._dict[key]
        time = val.time
        value = value.value
        return value

    def free_up_space(self,):
        sorted_items = sorted(self._dict.iteritems(), cmp=cmp_values)
        key = sorted_items[0][0]
        del self._dict[key]

    def state(self):
        sorted_items = sorted(self._dict.iteritems(), cmp=cmp_values)
        print sorted_items

    def put(self, key, value):
        self[key] = value

    def get(self, key):
        return self[key]

    def clear(self,):
        del self._dict
        self._dict = {}

    def __delete__(self):
        del self._dict
        self.size = None

    def evict(self, key):
        self._dict.pop(key)

    def __iter__(self):
        return self._dict.keys()

    def len(self,):
        return len(self._dict)

if __name__ == "__main__":
    cache = LRUCache()
    for i in range(200):
        cache[i] = i + 200
    cache.evict(1)
    cache.state()
    for i in range(500, 600):
        cache[i] = i + 1000
    cache.state()
    cache.clear()
    for i in range(10):
        cache[i] = 213
    cache.state()
    del cache
