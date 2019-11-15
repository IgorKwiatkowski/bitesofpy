

# def my_queue(n=5):
#     return deque(maxlen=n)

def my_queue(n=5):
    return MyQueue(max_size=n)


class MyQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.contents = []

    def append(self, val):
        self.contents.append(val)
        if len(self.contents) > self.max_size:
            del self.contents[0]

    def __repr__(self):
        return self.contents

    def __iter__(self):
        return iter(self.contents)

if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """
