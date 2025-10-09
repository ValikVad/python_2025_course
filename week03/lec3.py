from typing import Any


class Animal:
    sound: str = "mu"
    _protect_val: str = "protect"
    __private_args: str = "privat"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_name_and_age(self) -> None:
        print(f"Dog's name is {self.name} age: {self.age} '{self.sound}'")


class Dog(Animal):
    def __init__(self, name: str, age: int, sound: str):
        super().__init__(name, age)
        self.sound = sound

    def __str__(self) -> str:
        return f"Dog's name is {self.name} age: {self.age}"

    def __int__(self) -> int:
        return 1

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


my_dog = Dog("Lord", 7, "gaf")

# my_dog.sound = "mu"
# my_dog.print_name_and_age()
# print(my_dog._protect_val)
# print(my_dog.sound)
print(str(my_dog), int(my_dog))

# print(my_dog())


# class Empty:
#     value = 9
#     def __call__(self, *args, **kwds):
#         return str(self.value)


# class A:
#     value = 1

#     def __add__(self, other: str):
#         return f"{self.value}{other}"

#     def __call__(self, *args, **kwds):
#         return str(self.value)
# class B:
#     value = 1

#     def __radd__(self, other: str):
#         return f"{other}{self.value}"

#     def __call__(self, *args, **kwds):
#         return str(self.value)

# empty = Empty()
# print(A() + empty())
# # print(B() + empty())
# print(empty() + A())


int("10")
