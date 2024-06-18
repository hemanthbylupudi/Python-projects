def calculator(n):
    equation = n.replace(" ","")
    stack=[]
    current_num=0
    current_op= '+'
    for i in equation:
        if i.isdigit():
            current_num = current_num*10 +int(i)
        elif i in ['+','-','*','/','%']:
            if current_op == '+':
                stack.append(current_num)
            elif current_op == '-':
                stack.append(-current_num)
            elif current_op == '*':
                stack.append(stack.pop()*current_num)
            elif current_op == '/':
                stack.append(stack.pop()/current_num)
            elif current_op =='%':
                stack.append(stack.pop()%current_num)
            current_num =0
            current_op = i

    if current_op =='+':
        stack.append(current_num)
    elif current_op =='-':
        stack.append(-current_num)
    elif current_op =='*':
        stack.append(stack.pop()*current_num)
    elif current_op == '/':
        stack.append(stack.pop()/current_num)
    elif current_op == "%":
        stack.append(stack.pop()%current_num)

    result = sum(stack)
    return result


n=input("Enter the equation:")
result = calculator(n)
print("Result:",result)
