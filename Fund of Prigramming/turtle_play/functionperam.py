
def multiply(x, y):
    return (x * y)

def add(x, y):
    return (x + y)

def evaluate(f, x, y):
    return f(x,y)

print(multiply(2, 3))
print(add(2, 3))
#print(multiply("2", "3"))
print(evaluate(multiply,2, 3))