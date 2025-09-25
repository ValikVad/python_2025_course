import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", nargs="+", help="Имя пользователя")
parser.add_argument("--age", nargs="+", type=int, help="Возраст")
args = parser.parse_args()

print(f"Имя: {args.name}, возраст: {args.age}")
