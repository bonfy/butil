# coding: utf-8


class MemoryCache:
    """ MemoryCache use dict

    >>> m = MemoryCache()
    >>> m.add('a', 1)
    >>> m.keys
    dict_keys(['a'])

    >>> m['b'] = 2
    >>> m.size
    2

    >>> m.pop('a')
    1
    >>> m.delete('b')

    >>> m.add('abc', 'abc')
    >>> m.add('adc', 'adc')
    >>> m.add('bcd', 'bcd')
    >>> m.clear('a')
    >>> m.keys
    dict_keys(['bcd'])
    """

    def __init__(self):
        self._m = {}

    @property
    def keys(self):
        return self._m.keys()

    @property
    def size(self):
        return len(self.keys)

    def is_empty(self):
        return len(self.keys) == 0

    def __setitem__(self, key, val):
        self.add(key, val)

    def add(self, key, val):
        self._m[key] = val
    
    def delete(self, key):
        if key in self.keys:
            del self._m[key]

    def pop(self, key):
        return self._m.pop(key)

    def get(self, key, default=None):
        return self._m.get(key, default)

    def display(self):
        print(self._m)

    def clear(self, key_start_with=None):
        if key_start_with is None:
            self._m.clear()

        keys_to_clear = filter(lambda i: i.startswith(key_start_with), self.keys)
        for k in list(keys_to_clear):
            self.delete(k)

    



