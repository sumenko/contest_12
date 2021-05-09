import time

def min_divider(num):
    divider = 2
    limit = num
    while num  % divider != 0:
        if divider * divider > limit: return num
        divider += 1

    return divider

def factorize(num):
    if num == 1: return '1'
    
    dividers = ()
    result = num

    while result != 1:
        divider = min_divider(result)
        dividers += (str(divider),)
        result = result // divider
    return ' '.join(dividers)
    
if __name__ == '__main__':
    print(factorize(int(input())))
    assert factorize(1) == '1'
    assert factorize(8) == '2 2 2'
    assert factorize(13) == '13'
    assert factorize(100) == '2 2 5 5'

