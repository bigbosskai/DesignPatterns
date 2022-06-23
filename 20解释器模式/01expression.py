from abc import ABCMeta, abstractmethod

"""
解释器模式
解释器模式（Interpreter Pattern）提供了评估语言的语法或表达式的方式，
它属于行为型模式。这种模式实现了一个表达式接口，该接口解释一个特定的上下文。
这种模式被用在 SQL 解析、符号处理引擎等。

介绍
意图：给定一个语言，定义它的文法表示，并定义一个解释器，这个解释器使用该标识来解释语言中的句子。

主要解决：对于一些固定文法构建一个解释句子的解释器。
"""


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, s):
        pass


class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, s):
        return self.data in s


class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, s):
        return self.expr1.interpret(s) or self.expr2.interpret(s)


class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, s):
        return self.expr1.interpret(s) and self.expr2.interpret(s)


# 规则：Robert和John是男性
def getMaleExpression():
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    return OrExpression(robert, john)


# 规则：Julie是一个已婚的女性
def getMarriedWomanExpression():
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    return AndExpression(julie, married)


if __name__ == '__main__':
    isMale = getMaleExpression()
    isMarriedWoman = getMarriedWomanExpression()
    print("John is male? " + str(isMale.interpret("John")))
    print("Julie is a married women? " + str(isMarriedWoman.interpret("Married Julie")))
