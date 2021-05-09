def reg_sum(r_one, r_two, shift):
    sums = {
        ('0', '0', False): ('0', False),
        ('0', '1', False): ('1', False),
        ('1', '0', False): ('1', False),
        ('1', '1', False): ('0', True),
        ('0', '0', True): ('1', False),
        ('0', '1', True): ('0', True),
        ('1', '0', True): ('0', True),
        ('1', '1', True): ('1', True),
        }
    return sums[(r_one, r_two, shift)]

def sum_binary(one, two):
    length = max(len(one), len(two))
    one = one.rjust(length, '0')[::-1]
    two = two.rjust(length, '0')[::-1]

    result = ''
    shift = 0
    index = 0
    while index < length:
        digit, shift = reg_sum(one[index], two[index], shift)
        result += digit
        index += 1
    
    if shift: result += '1'
    
    result = result[::-1].lstrip('0')
    if result == '': result = '0'

    return result

if __name__ == '__main__':
    # one = input()
    # two = input()
    # print(sum_binary(one, two))
    assert sum_binary('1010', '1011') == '10101' 
    assert sum_binary('0', '0') == '0' 
    assert sum_binary('0', '0') == '0' 
    assert sum_binary('0', '1') == '1' 
    assert sum_binary('1', '0') == '1' 
    # assert sum_binary('', '') == '0' 
    assert sum_binary('1100', '00101101') == '111001' 
