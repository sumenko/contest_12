def extra_char(s, t):
    one = sorted(s)
    two = sorted(t)
    

    for i in range(len(one)):
        if one[i] != two[i]:
            return two[i]
    return two[-1]

if __name__ == '__main__':
    s = input()
    t = input()
    print(extra_char(s, t))
    assert extra_char('abcd', 'abcde') == 'e'
    assert extra_char('go', 'ogg') == 'g'
    assert extra_char('aaa', 'aab')