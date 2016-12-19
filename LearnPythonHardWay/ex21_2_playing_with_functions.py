def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

one = subtract(2, 1)
two = add(1, 1)
three = divide(6, 2)
four = multiply(2, 2)
five = add(multiply(two, one), three)
six = multiply(two, three)
seven = subtract(multiply(five, two), divide(six, two))

print one, two, three, four, five, six, seven