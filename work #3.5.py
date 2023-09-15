class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.count = 1

    def __iter__(self):
        self.list = iter([])
        return self

    def __next__(self):
        while self.count:
            try:
                item = next(self.list)
                self.count -= 1
            except StopIteration:
                self.list = list(self.flat_generator(self.list_of_lists))
                self.count = len(self.list) - 1
                self.list = iter(self.list)
                item = next(self.list)
            return item
        else:
            raise StopIteration

    def flat_generator(self, list_of_lists):
        for i in list_of_lists:
            if type(i) is list:
                for j in self.flat_generator(i):
                    yield j
            else:
                yield i


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
