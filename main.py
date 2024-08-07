import types


LIST_OF_LISTS_1 = [['a', 'b', 'c'], 
                   ['d', 'e', 'f', 'h', False], 
                   [1, 2, None]]
FLATTEN_LIST_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

LIST_OF_LISTS_2 = [[['a'], ['b', 'c']], 
                   ['d', 'e', [['f'], 'h'], False], 
                   [1, 2, None, [[[[['!']]]]], []]]
FLATTEN_LIST_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


class FlatIterator:
    '''Класс-итератор

    '''
    def __init__(self, list_of_lists=None):
        self.list_of_lists = list_of_lists

    def list_flatten(self, sequence):
        '''Функция разглаживания списка

        Для разглаживания простого списка со списками (без дополнительной вложенности) 
        можно использовать функцию sum():
            self.iter_list = iter(sum(self.list_of_lists, []))

        '''
        result = []
        for value in sequence:
            if isinstance(value, list):
                result.extend(self.list_flatten(value))
            else:
                result.append(value)
        return result

    def __iter__(self):
        self.iter_list = iter(self.list_flatten(self.list_of_lists))
        return self

    def __next__(self):
        try: 
            return next(self.iter_list)
        except IndexError:
            raise StopIteration


def flat_generator(list_of_lists):
    '''Функция-генератор
    '''
    yield from FlatIterator().list_flatten(list_of_lists)


def test_2():
    '''Тест функции-генератора
    '''
    for flat_iterator_item, check_item in zip(flat_generator(LIST_OF_LISTS_1), FLATTEN_LIST_1):
        assert flat_iterator_item == check_item
    assert list(flat_generator(LIST_OF_LISTS_1)) == FLATTEN_LIST_1
    assert isinstance(flat_generator(LIST_OF_LISTS_1), types.GeneratorType)

    print('Задание №2 выполнено')

def test_4():
    '''Тест функции-генератора
    '''
    for flat_iterator_item, check_item in zip(flat_generator(LIST_OF_LISTS_2), FLATTEN_LIST_2):
        assert flat_iterator_item == check_item
    assert list(flat_generator(LIST_OF_LISTS_2)) == FLATTEN_LIST_2
    assert isinstance(flat_generator(LIST_OF_LISTS_2), types.GeneratorType)

    print('Задание №4 выполнено')

def test_1():
    '''Тест класса-итератора
    '''
    for flat_iterator_item, check_item in zip(FlatIterator(LIST_OF_LISTS_1), FLATTEN_LIST_1):  
        assert flat_iterator_item == check_item
    assert list(FlatIterator(LIST_OF_LISTS_1)) == FLATTEN_LIST_1

    print('Задание №1 выполнено')

def test_3():
    '''Тест класса-итератора
    '''
    for flat_iterator_item, check_item in zip(FlatIterator(LIST_OF_LISTS_2), FLATTEN_LIST_2):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(LIST_OF_LISTS_2)) == FLATTEN_LIST_2

    print('Задание №3 выполнено')


if __name__ == '__main__':
    for test in test_1, test_2, test_3, test_4:
        test()