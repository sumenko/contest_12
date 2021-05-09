import random

def generate(n, max_int, max_zeros):
    sample = random.sample(range(1, max_int), n)
    num_zeros = random.randint(1, max_zeros)
    
    for i in range(num_zeros):
        index = random.randint(0, len(sample)-1)
        sample[index] = 0

    return ' '.join([str(i) for i in sample])


if __name__ == '__main__':
    print(generate(10, 20, 5))
