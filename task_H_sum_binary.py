def reg_sum(r_one, r_two, shift):
    sums = {
        ('0', '0', 0): ('0', 0),
        ('0', '1', 0): ('1', 0),
        ('1', '0', 0): ('1', 0),
        ('1', '1', 0): ('0', 1),
        ('0', '0', 1): ('1', 0),
        ('0', '1', 1): ('0', 1),
        ('1', '0', 1): ('0', 1),
        ('1', '1', 1): ('0', 2),
        }
    return sums[(r_one, r_two, shift)]

def sum_binary(one, two):
    one = one[::-1]
    two = two[::-1]
    result = ''
    shift = False
    index = 0
    while index < len(one) and index < len(two):
        if one[index] == 0 and two[index] ==0:
            result == '0'
        elif one[index] == '1' and two[index] == '1':
            shift = False
            result += '0'
        else:
            result += '1'
        
    return '0'

assert sum_binary('1010', '1011') == '10101' 
assert sum_binary('0', '0') == '0' 
assert sum_binary('0', '0') == '0' 
assert sum_binary('0', '1') == '1' 
assert sum_binary('1', '0') == '1' 
assert sum_binary('', '') == '0' 