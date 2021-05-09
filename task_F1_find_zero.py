from gen_data import generate
import time

def find_zeros(n, data):
    times = []
    start = time.time()
    street = [1 if i!='0' else 0 for i in data.split()]
    times.append(time.time())
    zero_paths = [n for _ in range(n)]
    times.append(time.time())
    

    index = 0
    while index < n:
        try:
            index = street.index(0, index)
        except ValueError:
            break
        for i in range(n):
            length = abs(index - i)
            if length < zero_paths[i]:
                zero_paths[i] = length
        index += 1

    times.append(time.time())
    print('\n'.join(map(lambda f: '{:.2f}'.format(f-start), times)))
    return ' '.join([str(i) for i in zero_paths])

if __name__ == '__main__':
    # assert find_zeros(5, '0 1 4 9 0') == '0 1 2 1 0'
    # exit(0)
    # assert find_zeros(6, '0 7 9 4 8 20') == '0 1 2 3 4 5'
    
    n = 10**6
    print('Prepare data')
    data = generate(n, 10**9, 40)
    print('Start test')
    start = time.time()
    find_zeros(n, data)
    print("time: {:.2f}".format(time.time() - start))
    # print(find_zeros(int(input()), input()))


    