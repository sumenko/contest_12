def is_power_four(num):
    p = 1
    if num == 1: return True
    current = 4
    while current < num:
        current = 4 ** p
        p +=1

    return num == current

if __name__ == '__main__':
    print(is_power_four(int(input())))
    assert is_power_four(15) == False
    assert is_power_four(16) == True
    assert is_power_four(256) == True
    assert is_power_four(4) == True
    assert is_power_four(0) == False
    assert is_power_four(-16) == False
    assert is_power_four(1) == True