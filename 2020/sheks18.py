import re
import operator
Forms, Lines = {
    '+': operator.add,
    '*': operator.mul,
}, [*open("inputs/18")]


def GetTokens(Ln):
    while Ln:
        for Ptn, Fn in [('\d+', int), ('[+*()]', str)]:
            if (V := re.match('(?:\s*)(' + Ptn + ')(?:\s*)', Ln)):
                yield Fn(V.group(1))
                Ln = Ln[V.end():]
# Part 1 Structure


class Silver(list):
    def Expr(Tokens):
        Value = Tokens.Factor()
        print('\n')
        print(Value)
        while Tokens and Tokens[0] in Forms:
            Value = Forms[Tokens.pop(0)](Value, Tokens.Factor())
            print(Value)
        return Value

    def Factor(Tokens):
        Value = Tokens.pop(0)
        if Value != "(":
            return Value
        Value = Tokens.Expr()
        Tokens.pop(0)
        return Value
# Part 2 Structure


class Gold(Silver):
    def Expr(Tokens):
        Value = Tokens.Term()
        while Tokens and Tokens[0] == "*":
            Value = Forms[Tokens.pop(0)](Value, Tokens.Term())
        return Value

    def Term(Tokens):
        Value = Tokens.Factor()
        while Tokens and Tokens[0] == "+":
            Value = Forms[Tokens.pop(0)](Value, Tokens.Factor())
        return Value

# Results


def Eval(Ty):
    # for X in Lines:
    # print(*GetTokens(X))
    return sum(Ty(GetTokens(X)).Expr() for X in Lines)


print("Silver:", Eval(Silver), "\nGold:", Eval(Gold))
