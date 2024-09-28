from math import ceil, floor
def evalRPN(self, tokens: list[str]) -> int:
    stack = []
    stack = []
    for i in tokens:
        if i in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack.append(a+b)
            elif i == "-":
                stack.append(a-b)
            elif i == "*":
                stack.append(a*b)
            else:
                if a/b < 0:
                    stack.append(ceil(a/b))
                else:
                    stack.append(floor(a/b))
        else:
            stack.append(int(i))
    return stack[0]
    
def main():
    print(f"this is the result: {evalRPN(["2","1","+","3","*"])}")
                                   
if __name__ == "__main__":
    main()