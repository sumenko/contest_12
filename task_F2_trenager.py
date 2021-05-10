from f2_test import test_data


def trainer(k, data):
    join_data = ''.join(data)

    score = 0
    keys = set(''.join(join_data.split('.')))
    for key in keys:
        count = join_data.count(key)
        if count <= 2 * k:
            score += 1

    return score


if __name__ == '__main__':
    for test in test_data.keys():
        assert (trainer(test_data[test]['k'], test_data[test]['data']) ==
                test_data[test]['answer'])

    k = int(input())
    data = []
    for i in range(4):
        data += input()
    print(trainer(k, data))
