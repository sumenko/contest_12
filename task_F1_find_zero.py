import time

from gen_data import generate


def find_zeros(n, data):
    street = data.split()  # улица
    paths = []  # расстояния до нулей

    index = 0
    zero_left = street.index('0', 0)
    zero_right = zero_left

    while index < len(street):
        if index == zero_right:
            zero_left = zero_right
            try:
                zero_right = street.index('0', index + 1)
            except ValueError:
                pass

        right = abs(zero_right-index)
        left = abs(zero_left-index)

        paths.append(str(min(right, left)))
        index += 1

    return ' '.join(paths)


if __name__ == '__main__':
    assert find_zeros(5, '0 1 4 9 0') == '0 1 2 1 0'
    assert find_zeros(6, '0 7 9 4 8 20') == '0 1 2 3 4 5'
    assert find_zeros(9, '98 0 10 77 0 59 28 0 94') == '1 0 1 1 0 1 1 0 1'
    assert (find_zeros(12, '99 0 100 72 43 49 0 51 19 61 93 31') ==
            '1 0 1 2 2 1 0 1 2 3 4 5')

    n = 10**6
    print('Prepare data')
    data = generate(n, 10**9, 40)
    print('Start test')
    start = time.time()
    find_zeros(n, data)
    print("time: {:.2f}".format(time.time() - start))
    # print(find_zeros(int(input()), input()))
