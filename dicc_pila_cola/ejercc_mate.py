expression = "3 4 2 * +"
stack = []

for token in expression.split():
    if token.isdigit():
        stack.append(int(token))
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if token == '+':
            stack.append(operand1 + operand2)
        elif token == '*':
            stack.append(operand1 * operand2)

result = stack.pop()  # El resultado final estará en la parte superior de la pila
print(result)