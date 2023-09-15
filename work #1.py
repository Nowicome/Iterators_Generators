class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.length = len(list_of_list)
        self.exist = True

    def __iter__(self):
        self.results = iter([])
        return self

    def __next__(self):
        while self.length or self.exist:
            try:
                item = next(self.results)
                if item == self.list_of_lists[-1][-1]:
                    self.exist = False
            except StopIteration:
                self.results = iter(self.list_of_lists[len(self.list_of_lists) - self.length])
                self.length -= 1
                item = next(self.results)
            return item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
