class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.i = len(list_of_list)
        self.j = 0
        self.exist = True
        self.empty = []

    def __iter__(self):
        self.list = []
        return self

    def __next__(self):
        if self.i or self.exist:
            if self.list:
                item = self.take_item()
            else:
                self.list = self.list_of_lists[len(self.list_of_lists) - self.i]
                item = self.take_item()

            return item
        else:
            raise StopIteration

    def take_item(self):
        if self.list[self.j] != self.empty:
            item = self.list.pop(self.j)
        else:
            self.j += 1
            if not len(self.list) - self.j:
                self.j = 0
                self.i -= 1
            return self.__next__()

        if type(item) is list:
            some_list = []
            for z in item:
                some_list.insert(0, z)
            for z in some_list:
                self.list.insert(self.j, z)
            return self.__next__()

        else:
            self.list.insert(self.j, item)
            self.j += 1
            if not len(self.list) - self.j:
                self.j = 0
                self.i -= 1
                self.list = self.list_of_lists[len(self.list_of_lists) - self.i]
                if self.list == self.list_of_lists[-1]:
                    self.exist = False
            return item


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
