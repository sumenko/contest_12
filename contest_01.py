# вычислить ax^2+bx+c
# input: a, x, b, c
text= input()
a, x, b, c = [int(o) for o in text.split()]
print(a * x**2 + b * x + c)
