def solve_list(equation, print_result=True):
    while '*' in equation or '/' in equation:
        mul_pos = equation.index('*') if '*' in equation else float('inf')
        div_pos = equation.index('/') if '/' in equation else float('inf')
        k = min(mul_pos, div_pos)
        nb = float(equation[k - 1])
        na = float(equation[k + 1])
        if equation[k] == '/':
            result = str(nb / na)
        else:
            result = str(nb * na)
        equation.pop(k + 1)
        equation.pop(k)
        equation[k - 1] = result

    while '+' in equation or '-' in equation:
        add_pos = equation.index('+') if '+' in equation else float('inf')
        sub_pos = equation.index('-') if '-' in equation else float('inf')
        k = min(add_pos, sub_pos)
        nb = float(equation[k - 1])
        na = float(equation[k + 1])
        if equation[k] == '-':
            result = str(nb - na)
        else:
            result = str(nb + na)
        equation.pop(k + 1)
        equation.pop(k)
        equation[k - 1] = result

    if print_result:
        result = float(equation[0])
        if result == int(result):
            print(int(result))
        else:
            print(result)


def brackets(equation):
    while '(' in equation:
        k = len(equation) - 1 - equation[::-1].index('(')
        if ')' in equation[k:]:
            l = equation.index(')', k)
            r = equation[(k + 1):(l)]
            solve_list(r, print_result=False)
            equation[k:l + 1] = [r[0]]
        else:
            equation.pop(k)
    while ')' in equation:
        equation.remove(')')


while True:
    user = input("Enter the sum:")
    if not user:
        continue
    ops = '+-*/()'
    equation = []
    temp = ''

    for i in user:
        try:
            if i in ops:
                if temp != "":
                    equation.append(temp)

                equation.append(i)
                temp = ""

            else:
                temp += i
        except ValueError:
            print("invalid input!")

    if temp != "":
        equation.append(temp)

    brackets(equation)
    solve_list(equation)