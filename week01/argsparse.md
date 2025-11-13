# Доклад на Argparse


Argparse - модуль в стандартной библиотеке питона. Модуль argparse позволяет разбирать аргументы, передаваемые скрипту при его запуске из командной строки, и даёт возможность пользоваться этими аргументами в скрипте. Этот модуль позволяет предоставлять скрипту некие данные в момент его запуска, а этими данными скрипт сможет воспользоваться во время выполнения его кода.

Чтобы понять это, посмотрим на обычный пример:

Обычно запускаем Python-скрипт как:
> python myscript.py

Но можно запускать с дополнительными параметрами, например:
> python myscript.py --name Inar 

Рассмотрим пример:

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help = "write your name!")
args = parser.parse_args()
print("Привет,", args.name)
```
>Запустим код: python myscript.py Inar

>Результат: Привет, Inar

Рассмотрим еще один пример:

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",type=int, help = "display a square of a given number") #метод используемый для указания параметров команд строк, которая прога готова принять
args = parser.parse_args() #метод возвращает некоторые данные из указанных параметров(парсим аргументы)
print(args.square**2) 

```
>Запустим код: python myscript.py 4

>Результат: 16 

Если же мы не будем указывать "type = int", то это не прокатит, так как argparse по умолчанию обрабатывает параметры как строки


В примерах выше я использовал,так называемые, **"позиционные аргументы"**. Про них важно запомнить следующее:
1. Указывается без имени.

2. Порядок имеет значение (нужно писать именно в том порядке, как объявлено в коде).

3. Обычно такие аргументы обязательные.

Далее расмотрим **Именованные аргументы**

Рассмотрим пример:

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Имя пользователя")
parser.add_argument("--age", type=int, help="Возраст")
args = parser.parse_args()

print(f"Имя: {args.name}, возраст: {args.age}")

```
>Запустим код: python myscript.py --age 21 --name Inar

>Результат: Имя: Inar, возраст: 21

Следует запомнить основное про **именованные аргументы**:

1. Указывается с именем через -- или -.

2. Порядок НЕ имеет значения (можно писать в любом порядке).

3. Обычно такие аргументы необязательные, можно задать значения по умолчанию.


**Аргументы по умолчанию** 

Легче сразу понять на примере:

```
import argparse 

parser = argparse.ArgumentParser(description="Пример argparse")
parser.add_argument("--city", default= "Уфа", help = 'Укажите город')
args = parser.parse_args()
print(f"Город: {args.city}")

```

>Запустим код: python myscript.py --city NiNo

>Результат: Город: NiNo


**Флаги**
```
import argparse 

parser = argparse.ArgumentParser(description="Пример argparse")
parser.add_argument("--debug", action = "store_true", help = "Checker")
args = parser.parse_args()
if args.debug:
    print("Debug on")
else:
    print("Debug off")

```
>Запустим код: python myscript.py --debug

>Результат код: Debug on

>Запустим код_2: python myscript.py

>Результат код_2: Debug off


***Скомбинируем Позиционный и Именованный аргумент***

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)

```
>Запустим код_1: python myscript.py 4

>Результат: 16

>Запустим код_2: python myscript.py 4 --v

>Результат: the square of 4 equals 16

>Запустим код_3: python myscript.py --verbose 4 

>Результат: the square of 4 equals 16



Для любого скрипта можно вызвать:

>python myscript.py --help

и получить автоматическую инструкцию
