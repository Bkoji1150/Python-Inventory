

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


b = any([4==3, 23>4])

x = all([4==4, 23>4])
format(14, '#b'), format(14, 'b')


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
s = Shape()
print(dir(s))



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=1)))

list(enumerate(seasons, start=1))

# Equivalent to

def enumerate(sequense, start=0):
    n = start
    for element in sequense:
        yield n, element
        n += 1


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

b = enumerate(seasons)
# print(list(b))

# convert to Dict

b = dict(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
# print(b)


spam = __import__('spam', globals(), locals(), [], 0)

