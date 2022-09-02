class FlatIterator:

    def __init__(self, list_):

        self.list_iter = list_
        self.len = len(self.list_iter)

    def __iter__(self):

        self.count = 0
        self.iter_l = iter([])
        return self

    def __next__(self):

        try:
            item = next(self.iter_l)
        except StopIteration:
            if self.count >= self.len:
                raise StopIteration
            self.iter_l = iter(self.list_iter[self.count])
            item = next(self.iter_l)
            self.count += 1
        return item
