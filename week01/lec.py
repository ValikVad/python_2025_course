import ast
import dis
import io
import tokenize
from typing import Any

# 1) этап 1 - токенизация кода на языке пайтон
code = "x = 5 + 3"
tokens = tokenize.generate_tokens(io.StringIO(code).readline)
for tok in tokens:
    print(tok)


# 2) этап 2 - построение абстрактного синтаксического дерева (AST)
tree = ast.parse(code)
print(*ast.dump(tree, indent=2))


# 3) этап 3 - компиляция в байт код


def greet() -> None:
    print("Hello!")


dis.dis(greet)

# 4) этап 4 - запуск на PVM
# запускается бинарник из шага 3 (бинарники можно найти в __pycache__ папке)


# вопрос на подумать как добавляются сторонние модули на питоне?
# print("0")
# a = "3" / 2
# print("1") x // SyntaxError: invalid syntax
# 1/0  # ZeroDivisionError: division by zero
# print("3")


# >>> x = 25
# >>> id(x)
# 4331936160
# >>> hex(id(x))
# '0x1023419a0'
# >>> x = 12
# >>> hex(id(x))
# '0x102341800'
# >>>


x: str = "global"


def foo() -> None:
    x = "local_1"

    def foo_inner() -> None:
        # nonlocal x
        # x = "local_2"
        # print(x)
        global x
        print(x)
        x = "local_2"
        print(x)

    foo_inner()
    print(x)


foo()
print(x)


x1: list[str] = ["Artem"]
x2: list[Any] = x1 + ["Danya"]
print(x1 is x2)


# >>> x = 5
# >>> y = 3
# >>> c = x+y
# >>> print(c)
# 8
# >>> x = 25
# >>> id(x)
# 4331936160
# >>> hex(id(x))
# '0x1023419a0'
# >>> x = 12
# >>> hex(id(x))
# '0x102341800'
# >>> type(x)
# <class 'int'>
# >>> x = "Alex"
# >>> type(x)
# <class 'str'>
# >>> hex(id(x))
# '0x101add920'
# >>> x =
#   File "<stdin>", line 1
#     x =
#         ^
# SyntaxError: invalid syntax
# >>> x
# 'Alex'
# >>> y = x
# >>> y
# 'Alex'
# >>> print(id(x) == id(y))
# True
# >>> y = y * 3
# >>> y
# 'AlexAlexAlex'
# >>> x
# 'Alex'
# >>> a = 3
# >>> b = a
# >>> id(a) == id(b)
# True
# >>> b = b * 3
# >>> id(a) == id(b)
# False
# >>> a
# 3
# >>> b
# 9
# >>> list = [1, 2 , 3]
# >>> list2 = list
# >>> list2.append(4)
# >>> list
# [1, 2, 3, 4]
# >>> list2
# [1, 2, 3, 4]
# >>> id(list) == id(list2)
# True
# >>> id("alex")
# 4323142192
# >>> a = "alex"
# >>> b = a.upper()
# >>> print(f"{id(a) \n{id(b)}")
#   File "<stdin>", line 1
#     print(f"{id(a) \n{id(b)}")
#                     ^
# SyntaxError: unexpected character after line continuation character
# >>> print(f"{id(a)  {id(b)}")
#   File "<stdin>", line 1
#     print(f"{id(a)  {id(b)}")
#                            ^
# SyntaxError: f-string: expecting '}'
# >>> print(f"{id(a)} \n  {id(b)}")
# 4323138448
#   4323145744
# >>> a is b
# False
# >>> a == b
# False
# >>> a.upper() == b
# True
# >>> a.upper() is  b
# False
# >>> a = a.upper()
# >>> a is b
# False
# >>> a == b
# True
# >>> a
# 'ALEX'
# >>> b
# 'ALEX'
# >>>
# >>>
# >>> x = 42
# >>> del x
# >>> x
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined
# >>> x = 42
# >>>
# >>>
# >>>
# >>> x = 35
# >>>
# >>>
# >>> import sys
# >>>
# >>> sys.getrefcount(x)
# 4294967295
# >>> sys.getrefcount(1)
# 4294967295
# >>> print(sys.getrefcount(1))
# 4294967295
# >>> x = 1
# >>> print(sys.getrefcount(1))
# 4294967295
# >>> print(sys.getrefcount("Alex"))
# 3
# >>> y = "Alex"
# >>> print(sys.getrefcount("Alex"))
# 3
# >>> z = "Alex"
# >>> print(sys.getrefcount("Alex"))
# 4
# >>> o = "Alex"
# >>> print(sys.getrefcount("Alex"))
# 5
# >>> i = 1
# >>> print(sys.getrefcount(1))
# 4294967295
# >>> erereiyrpeyre = 1
# >>> print(sys.getrefcount(1))
# 4294967295
# >>>
# >>>
# >>>
# >>> a = []
# >>> b = []
# >>> a.append(b)
# >>> b.append(a)
# >>>
# >>> # a -> b -> a -> ....
# >>>
# >>> import gc
# >>> gc.collect()
# 0
# >>>
# >>>
# >>>
# >>>
# >>> xx = (["Artem"])
# >>> type(xx)
# <class 'list'>
# >>> xx = (["Artem"], ["ab"])
# >>> type(xx)
# <class 'tuple'>
# >>> x is x[0].append("Danya")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not subscriptable
# >>> xx is xx[0].append("Danya")
# False
