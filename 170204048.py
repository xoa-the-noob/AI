neighbourlist = [
    ('d', 'a', 7),
    ('a', 'c', 2),
    ('c', 'b', 3),
    ('b', 'e', 1),
    ('e', 'h', 3),
    ('h', 'g', 6),
    ('g', 'f', 27),

]


def path_length(initial, final, length):
    if initial == final:
        print('Path Length:', length)
        return length
    for temp in neighbourlist:
        if temp[0] == initial:
            path_length(temp[1], final, length + temp[2])
            return length


def find_length():
    initial = input('Enter the source node:')
    final = input('Enter the destination node:')
    path_length(initial, final, 0)
    path_length(final, initial , 0)

find_length()
