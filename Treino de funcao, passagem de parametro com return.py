def add_numbers(n1, n2,):
    result = n1 + n2
    return result


def multiply_numbers(n1, n2):
    result2 = n1 * n2
    return result2


number1 = input("choose the first number ")
number2 = input("choose the second number")
number1 = int(number1)
number2 = int(number2)

result = add_numbers(number1, number2)
result2 = multiply_numbers(number1, number2)

print('The sum between', [number1], 'and', [number2], 'is', [result])
print('The multiplication between', [number1], 'and', [number2], 'is', [result2])
