numbers = ['0','1','2','3','4','5','6','7','8','9','.',',']
operator = ['+','-','*','/']


class Calculator():
    def bracketChecker(self,x):
        n = 0
        for i in range(len(x)):
            if x[i] == '(':
                n += 1
            elif x[i] == ')':
                n -= 1
            if n < 0:
                break
        if n == 0:
            return True
        else:
            return False

    def prepareString(self, a):
        a = a.replace(' ', '')
        a = a.replace(',', '.')
        good_array = []
        buffer = ''
        is_good = True
        for i in range(len(a)):
            # print(a[i])
            if a[i] in numbers:
                buffer = buffer + a[i]
                # print(buffer)
            elif a[i] in operator or a[i] in '()':
                if buffer != '':
                    good_array.append(buffer)
                    buffer = ''
                good_array.append(a[i])
        if buffer != '':
            good_array.append(buffer)
        a = good_array
        a.append('|')
        return a

    def doMath(self, a, b, c):
        if c == '+':
            return a + b
        if c == '-':
            return a - b

        if c == '*':
            return a * b

        if c == '/' and b != 0:
            return a / b
        elif b == 0:
            return "ERROR: ZERO DIVISION"

    def getPrior(self,a):
        if a == '+' or a == '-':
            return 1
        elif a == '*' or a == '/':
            return 2
        elif a == '(' or a == ')':
            return 0

    def go_pop(self, p1, p2):
        if p1 > p2 or p1 == p2 and p2 != 0 and p1 != 0:
            return True
        else:
            return False

    def digestCheck(self, x):
        num = 0
        op = 0
        for i in range(len(x)):
            if x[i] in operator:
                op += 1
            elif x[i] not in operator and x[i] not in '()|':
                num += 1
        if (num - op) == 1:
            return True
        else:
            return False

    def convert_to_polish(self, ex):
        polish = []
        stack = []
        expr = self.prepareString(ex)
        if self.digestCheck(expr) == True and self.bracketChecker(expr) == True:
            for i in range(len(expr)):
                if expr[i] not in operator and expr[i] != '|' and expr[i] not in '()':
                    polish.append(expr[i])
                elif expr[i] == '|' and stack != []:
                    while stack != []:
                        polish.append(stack.pop())
                elif expr[i] in operator:
                    go = True
                    while go == True:
                        if stack != []:
                            p1 = self.getPrior(stack[len(stack) - 1])
                            p2 = self.getPrior(expr[i])
                            if self.go_pop(p1, p2):
                                polish.append(stack.pop())
                            else:
                                stack.append(expr[i])
                                go = False
                        else:
                            stack.append(expr[i])
                            go = False
                elif expr[i] in '()':
                    if expr[i] == '(':
                        stack.append(expr[i])
                    else:
                        go = True
                        while go == True:
                            if stack != []:
                                p1 = self.getPrior(stack[len(stack) - 1])
                                p2 = self.getPrior(expr[i])
                                if self.go_pop(p1, p2):
                                    polish.append(stack.pop())
                                else:
                                    go = False
                            else:
                                go = False
                        stack.pop()
        else:
            print("ERROR: INCORRECT EXPRESSION. PLEASE ENTER THE CORRECT DATA")
        return polish

    def polish_math(self, polish):
        result_stack = []
        for i in range(len(polish)):
            if polish[i] not in operator and polish[i] != '|' and polish[i] not in '()':
                result_stack.append(polish[i])
            elif polish[i] in operator:
                x = float(result_stack.pop())
                y = float(result_stack.pop())
                result_stack.append(self.doMath(y, x, polish[i]))
        result = result_stack.pop()
        return result

    def go_calc(self, ex):
        if self.convert_to_polish(ex) != []:
            result = self.polish_math(self.convert_to_polish(ex))
            return result