import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Line starts from {self.start} and ends {self.end}'

    def deep_copy(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    l1 = Line((1, 2), (3, 4))
    l2 = Line.deep_copy(l1)
    print(l1, '\n', l2)
    l2.start = (2, 2)
    print('Changed')
    print(l1, '\n', l2)
