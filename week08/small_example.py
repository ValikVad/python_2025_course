import json
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel

# a = "string"

# print("Тип переменной a:", type(a))


class Color(List[int]):
    RED = [255, 0, 0]


class ColorEnum(List[int], Enum):
    RED = [255, 0, 0]


class Address(BaseModel):
    city: str
    country: str


class Person(BaseModel):
    name: str
    addresses: List[Address]
    id: Union[str, int]
    friends: Optional[List["Person"]] = None


data = """{
    "name": "Jonh",
    "id": "1",
    "addresses": [{"city": "New York", "country": "USA", "kek": "kek"}]
}"""

data = json.loads(data)
print(data)

a = Person(**data)
print(a)

print(ColorEnum.RED, type(ColorEnum.RED))
print(Color.RED, type(Color.RED))
