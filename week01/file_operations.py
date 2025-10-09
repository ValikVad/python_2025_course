#!/usr/bin/env python3
"""
Примеры работы с файлами в Python
"""

import csv
import glob
import json
import os
import zipfile
from pathlib import Path

# ========================
# 1. Чтение файла (Read)
# ========================


def read_file_basic(filename: str) -> None:
    """Чтение файла построчно"""
    print("=== Чтение файла построчно ===")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(f"Строка: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")


def read_file_all(filename: str) -> None:
    """Чтение всего файла сразу"""
    print("\n=== Чтение всего файла ===")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"Содержимое файла:\n{content}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")


def read_file_lines(filename: str) -> None:
    """Чтение файла в список строк"""
    print("\n=== Чтение файла в список строк ===")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(f"Строк в файле: {len(lines)}")
            for i, line in enumerate(lines[:3]):  # Показываем первые 3 строки
                print(f"{i+1}: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")


# ========================
# 2. Запись в файл (Write)
# ========================


def write_file_basic(filename: str, content: str) -> None:
    """Запись в файл (перезапись)"""
    print("\n=== Запись в файл (перезапись) ===")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Данные записаны в {filename}")
    except Exception as e:
        print(f"Ошибка записи: {e}")


def append_to_file(filename: str, content: str) -> None:
    """Добавление в конец файла"""
    print("\n=== Добавление в конец файла ===")
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        print(f"Данные добавлены в {filename}")
    except Exception as e:
        print(f"Ошибка добавления: {e}")


def write_multiple_lines(filename: str, lines_list: str) -> None:
    """Запись нескольких строк"""
    print("\n=== Запись нескольких строк ===")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines_list:
                file.write(line + "\n")
        print(f"Записано {len(lines_list)} строк в {filename}")
    except Exception as e:
        print(f"Ошибка записи: {e}")


# ========================
# 3. Работа с JSON
# ========================


def json_example() -> None:
    """Пример работы с JSON"""
    print("\n=== Работа с JSON ===")

    # Создаем данные
    data = {
        "name": "Алексей",
        "age": 25,
        "hobbies": ["чтение", "программирование", "путешествия"],
        "address": {"city": "Москва", "street": "Ленина 10"},
    }

    # Сохраняем в файл
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("JSON данные сохранены в data.json")

    # Читаем обратно
    with open("data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        print("Загруженные данные:")
        print(json.dumps(loaded_data, ensure_ascii=False, indent=2))


# ========================
# 4. Парсинг CSV файлов
# ========================


def csv_example() -> None:
    """Пример работы с CSV"""
    print("\n=== Работа с CSV ===")

    # Создаем пример CSV файла
    csv_data = [
        ["Имя", "Возраст", "Город"],
        ["Анна", "28", "СПб"],
        ["Петр", "32", "Москва"],
        ["Мария", "24", "Новосибирск"],
    ]

    with open("people.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print("CSV файл создан: people.csv")

    # Читаем CSV
    with open("people.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Читаем заголовок
        print(f"Заголовок: {header}")

        print("Данные:")
        for row in reader:
            print(f"  {row}")


# ========================
# 5. Работа с папками и файлами
# ========================


def folder_operations() -> None:
    """Примеры работы с папками"""
    print("\n=== Работа с папками ===")

    # Создаем тестовую структуру
    os.makedirs("test_folder/subfolder", exist_ok=True)

    # Создаем тестовые файлы
    with open("test_folder/file1.txt", "w") as f:
        f.write("Содержимое первого файла")

    with open("test_folder/subfolder/file2.txt", "w") as f:
        f.write("Содержимое второго файла")

    # Показываем содержимое папки
    print("Содержимое test_folder:")
    for root, dirs, files in os.walk("test_folder"):
        level = root.replace("test_folder", "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

    # Поиск файлов
    print("\nПоиск всех .txt файлов:")
    txt_files = glob.glob("test_folder/**/*.txt", recursive=True)
    for file in txt_files:
        print(f"  {file}")


def file_info(filename: str) -> None:
    """Получение информации о файле"""
    print(f"\n=== Информация о файле: {filename} ===")
    try:
        stat = os.stat(filename)
        print(f"Размер: {stat.st_size} байт")
        print(f"Дата создания: {stat.st_ctime}")
        print(f"Дата модификации: {stat.st_mtime}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")


# ========================
# 6. Работа с путями
# ========================


def path_operations() -> None:
    """Примеры работы с путями"""
    print("\n=== Работа с путями ===")

    # Создаем путь
    current_path = Path(".")
    print(f"Текущая директория: {current_path.absolute()}")

    # Путь к файлу
    file_path = Path("test_folder/file1.txt")
    print(f"Путь к файлу: {file_path}")
    print(f"Расширение: {file_path.suffix}")
    print(f"Имя файла: {file_path.name}")
    print(f"Родительская папка: {file_path.parent}")

    # Создание нового пути
    new_path = Path("new_folder") / "data.txt"
    print(f"Новый путь: {new_path}")


# ========================
# 7. Работа с архивами
# ========================


def archive_example() -> None:
    """Пример работы с архивами"""
    print("\n=== Работа с архивами ===")

    # Создаем zip архив
    with zipfile.ZipFile("test_archive.zip", "w") as zipf:
        zipf.write("test_folder/file1.txt", "file1.txt")
        zipf.write("test_folder/subfolder/file2.txt", "subfolder/file2.txt")

    print("Создан архив test_archive.zip")

    # Распаковка
    with zipfile.ZipFile("test_archive.zip", "r") as zipf:
        zipf.extractall("extracted")

    print("Архив распакован в extracted/")


# ========================
# 8. Работа с ошибками
# ========================


def safe_file_operations() -> None:
    """Безопасная работа с файлами"""
    print("\n=== Безопасная работа с файлами ===")

    # Проверка существования файла
    filename = "test_file.txt"

    if os.path.exists(filename):
        print(f"Файл {filename} существует")
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(f"Содержимое файла: {content[:50]}...")
        except PermissionError:
            print("Нет прав на чтение файла")
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
    else:
        print(f"Файл {filename} не существует")
        # Создаем его
        with open(filename, "w") as f:
            f.write("Это тестовый файл\nСоздан в процессе обучения")
        print("Файл создан")


# ========================
# Основная функция
# ========================


def main() -> None:
    """Основная функция для демонстрации"""
    print("🎓 Примеры работы с файлами в Python")
    print("=" * 50)

    # Создаем тестовый файл для чтения
    test_content = """Это первая строка
Это вторая строка
Это третья строка
Это четвертая строка"""

    write_file_basic("test_read.txt", test_content)

    # Выполняем примеры
    read_file_basic("test_read.txt")
    read_file_all("test_read.txt")
    read_file_lines("test_read.txt")

    # Запись файлов
    write_file_basic("output.txt", "Первая строка\nВторая строка")
    append_to_file("output.txt", "Третья строка")

    # JSON пример
    json_example()

    # CSV пример
    csv_example()

    # Папки и файлы
    folder_operations()
    file_info("test_read.txt")

    # Пути
    path_operations()

    # Архивы
    archive_example()

    # Безопасные операции
    safe_file_operations()

    # Очистка
    print("\n=== Очистка ===")
    try:
        os.remove("test_read.txt")
        os.remove("output.txt")
        os.remove("data.json")
        os.remove("people.csv")
        os.remove("test_archive.zip")
        os.removedirs("extracted")
        os.removedirs("test_folder/subfolder")
        os.rmdir("test_folder")
        os.rmdir("new_folder")
        print("Все временные файлы удалены")
    except Exception:
        print("Не удалось удалить все временные файлы")


if __name__ == "__main__":
    main()
