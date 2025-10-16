
#CPYTHON

#Пошаговый гайд по сборке с помощью CMake. 

## 📋 Предварительные требования

- **Python 3.8+** с установленными development headers
- **Visual Studio 2022** с компонентами C++ и CMake
- **CMake 3.15+**

-1. Готовимся страдать

0. Качаем Python последней версии 

1. Качаем pybind 
```
pip install pybind11
```

2. Открываем Visual Studio -> Создание проекта -> Проект CMake -> Называем LowLevelStuff

3. Скачиваем https://github.com/pybind/pybind11/releases/tag/v3.0.1

4. Разархивируем в репу проекта CMake папку pybind11-3.0.1, в тоже место где лежит CMakeLists.txt

5. Открываем в VS CMakeLists.txt текст ниже и сохраняем
```
cmake_minimum_required (VERSION 3.8)

project ("LowLevelStuff")

find_package(Python REQUIRED COMPONENTS Development)
add_subdirectory(pybind11)

pybind11_add_module(LowLevelStuff "LowLevelStuff.cpp" "LowLevelStuff.h")


set_target_properties(LowLevelStuff PROPERTIES
    OUTPUT_NAME "LowLevelStuff"
    PREFIX ""
    SUFFIX ".pyd"
    CXX_STANDARD 20
    CXX_STANDARD_REQUIRED ON
)
```

6. Если возникли некие ошибки, то проверяем, что все сделали правильно

Итоговый вид проекта
```
LowLevelStuff/
├── CMakeLists.txt
├── LowLevelStuff.cpp
├── LowLevelStuff.h
├── pybind11/          
└── out/               # создается при сборке
    └── build/
        └── x64-release/
            └── LowLevelStuff.pyd
```

7. Открываем LowLevelStuff.h, пишем туда код ниже
```
//pybuild
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

int dif(int a, int b, int c) {
	return a - b + a - c;
}

PYBIND11_MODULE(LowLevelStuff, m) {
	
	m.doc() = "Your C++ module";

	m.def("dif", &dif, "Dif three integers");

}
```

8. Собираем

9. В папке LowLevelStuff\out\build\x64-release лежит LowLevelStuff.pyd

10. Создаем файл Python, вставляем туда
```
import pybind11
import LowLevelStuff

ans = LowLevelStuff.dif(1, 2, 3)

print(ans)
```

11. Кидаем LowLevelStuff.pyd в папку с Python скриптом, запускам

12. Если не работает, проверяем прошлые шаги. Если все равно не работает, он поможет, наверное =) https://www.deepseek.com/
