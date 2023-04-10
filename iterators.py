import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.inputList = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.nestedCursor = -1
        self.nestedList = self.inputList[self.cursor]
        return self

    def __next__(self):
        if self.cursor == len(self.inputList) - 1 and self.nestedCursor == len(self.nestedList) - 1:
            raise StopIteration
        
        if self.nestedCursor == len(self.nestedList) - 1:
            self.cursor += 1
            self.nestedCursor = 0
            self.nestedList = self.inputList[self.cursor]
        else:
            self.nestedCursor += 1

        item = self.nestedList[self.nestedCursor]
        return item
    """
class nestedFlatIterator:

    def __init__(self, list_of_list):
        self.inputList = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.deepCursor = 0
        self.count = 0
        if type(self.inputList[self.cursor]) is list:
                self.deepList = self.inputList[self.cursor]
        return self
    
    def __next__(self):
        if self.cursor == len(self.inputList) - 1 and self.nestedCursor == len(self.nestedList) - 1:
            raise StopIteration
        
        while type(self.deepList[self.deepCursor]) is list:
            self.deepList = self.deepList[self.deepCursor]

        if self.deepCursor != 0 or self.count > 0:
                self.deepCursor += 1
        
        if self.deepCursor == len(self.deepList):
            self.cursor += 1
            self.deepCursor = 0
            self.count = 0
            if type(self.inputList[self.cursor]) is list:
                self.deepList = self.inputList[self.cursor]

        self.count += 1
        item = self.deepList[self.deepCursor]
        return item
    """

def flat_generator(list_of_lists):
    for cursor in range(0, len(list_of_lists)):
        nestedList = list_of_lists[cursor]
        for nestedCursor in range(0, len(nestedList)):
            item = nestedList[nestedCursor]
            yield item

def nested_flat_generator(list_of_lists):
    for cursor in range(0, len(list_of_lists)):
        if type(list_of_lists[cursor]) is list:
            for item in nested_flat_generator(list_of_lists[cursor]):
                yield item
        else:
            yield list_of_lists[cursor]

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
    print('test_1 - finish')

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print('test_2 - finish')
    """
def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            nestedFlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(nestedFlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    """

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            nested_flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(nested_flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(nested_flat_generator(list_of_lists_2), types.GeneratorType)
    print('test_4 - finish')