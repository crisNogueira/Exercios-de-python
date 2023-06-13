e = str(input('Digite uma expressão matemática: ')).strip().upper()
a = y = 0
for c in range(0, len(e)):
    if e[c] == '(':
        a += 1
    if e[c] == ')':
        if c == 0:
            y += 1
        a -= 1
if y == 1:
    print('Essa expressão matemática não é válida.')
if a != 0:
    print('Essa expressão matemática não é válida.')
if a == 0 and y == 0:
    print('Essa expressão matemática é válida.')

