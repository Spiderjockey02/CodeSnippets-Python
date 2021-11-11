def calculate(Entry):
    equation = Entry.split(" ")
    #Basic arithmetic
    if '/' in equation:
        divide = equation.index('/')
        answer = int(equation[divide-1])/int(equation[divide+1])
    elif '*' in equation:
        mulitply = equation.index('*')
        answer = int(equation[mulitply-1])*int(equation[mulitply+1])
    elif '+' in equation:
        add = equation.index('+')
        answer = int(equation[add-1])+int(equation[add+1])
    elif '-' in equation:
        minus = equation.index('*')
        answer = int(equation[minus-1])*int(equation[minus+1])
    else:
        print("You need help!")
    print(answer)

while True:
    calculate(input("Enter equation: "))
