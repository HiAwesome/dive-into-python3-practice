class Fib:
    """ 生成斐波拉切数列的迭代器"""

    def __init__(self, ele):
        self.ele = ele

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.ele:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
