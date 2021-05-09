def list_form(length, num_one_str, num_two):
    digits = [int(i) for i in num_one_str.split()]
    digits.reverse()
    base = 1
    num_one = 0
    for d in digits:
        num_one += d * base
        base *= 10
    result = num_one + num_two
    answer = ' '.join([a for a in str(result)])
    return answer

if __name__ == '__main__':
    n = int(input())
    num_one_str = input()
    num_two = int(input())
    print(list_form(n, num_one_str, num_two))

    assert(list_form(4, '1 2 0 0', 34)) == '1 2 3 4'
    assert(list_form(2, '9 5', 17)) == '1 1 2'
    assert(list_form(6, '0 0 1 2 0 0', 34)) == '1 2 3 4'