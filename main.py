from flat_iterator import FlatIterator
from flat_generator import flat_generator


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


if __name__ == "__main__":
    iter_ = FlatIterator(nested_list)
    for it in iter_:
        print(it)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
