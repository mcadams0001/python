class ExampleIterator:
    def __init__(self, data) -> None:
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()
        rslt = self.data[self.index]
        self.index += 1
        return rslt

    def __getitem__(self, idx):
        return self.data[idx]

class ExampleIterable:
    def __init__(self) -> None:
        self.data = [1,2,3]

    def __iter__(self):
        return ExampleIterator(self.data)
