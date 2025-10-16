
#CPYTHON

##Зачем?
--	Интеграция C++ в Python или наоборот.
--	Возможность тестить C++ код через Python
--	Написание высокопроизводительных модулей для Python.
--	Использование Python как обертку вокруг ядра C++.

##Установка

###Python:
```
pip install pybind
```
###C++:
```
cmake_minimum_required(VERSION 3.15)
project(LowLevelStuff)

find_package(Python REQUIRED COMPONENTS Development)
find_package(pybind11 REQUIRED)

pybind11_add_module(LowLevelStuff example.cpp)
target_compile_features(LowLevelStuff PRIVATE cxx_std_20)
```

##Проблемки
--	1) Сложность переключения между высокоуровневым Python и C++
--	2) Cmake
--	3) Выделенная память в C++ должна быть освобождена
--	4) Необходимы хотя бы небольшие знания C++
