from collections import namedtuple

d = namedtuple("okay", ["a", "b"])
f = d(10, 20)

print(f)
