from f2_test import test_data


def trainer(k, data):
    
    return 2


if __name__ == '__main__':
    for test in test_data.keys():
        print('Test {}'.format(test))
        assert trainer(test_data[test]['k'], test_data[test]['data']) == test_data[test]['answer']