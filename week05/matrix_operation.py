# modular_matrix.py

import time
from typing import List

from modular_core import ModularNumber


class ModularMatrix(ModularNumber):
    def __init__(self, data: List[List[int]], mod: int):
        if not data or not data[0]:
            raise ValueError("Matrix must be non-empty")
        if mod <= 0:
            raise ValueError("Modulus must be positive")
        rows = len(data)
        cols = len(data[0])
        if any(len(row) != cols for row in data):
            raise ValueError("Matrix must be rectangular")
        self._mod = mod
        self._rows = rows
        self._cols = cols
        self._data = [[x % mod for x in row] for row in data]

    @property
    def mod(self) -> int:
        return self._mod

    @property
    def data(self) -> List[List[int]]:
        return self._data

    @property
    def shape(self) -> tuple:
        return (self._rows, self._cols)

    def __add__(self, other: "ModularMatrix") -> "ModularMatrix":
        if not isinstance(other, ModularMatrix):
            return NotImplemented
        if self.mod != other.mod or self.shape != other.shape:
            raise ValueError("Matrices must have same shape and modulus")
        new_data = [
            [(self.data[i][j] + other.data[i][j]) % self.mod for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return ModularMatrix(new_data, self.mod)

    def __mul__(self, other: "ModularMatrix") -> "ModularMatrix":
        if not isinstance(other, ModularMatrix):
            return NotImplemented
        if self.mod != other.mod or self._cols != other._rows:
            raise ValueError("Incompatible matrix dimensions or moduli")
        result = [[0] * other._cols for _ in range(self._rows)]
        for i in range(self._rows):
            for k in range(self._cols):
                for j in range(other._cols):
                    result[i][j] = (
                        result[i][j] + self.data[i][k] * other.data[k][j]
                    ) % self.mod
        return ModularMatrix(result, self.mod)

    def __pow__(self, n: int) -> "ModularMatrix":
        if n < 0:
            raise ValueError("Negative powers not supported")
        if self._rows != self._cols:
            raise ValueError("Matrix must be square for exponentiation")
        # Единичная матрица
        identity_data = [
            [1 if i == j else 0 for j in range(self._rows)] for i in range(self._rows)
        ]
        result = ModularMatrix(identity_data, self.mod)
        base = self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result

    def det(self):
        raise NotImplementedError

    def zero(self) -> "ModularMatrix":
        zero_data = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        return ModularMatrix(zero_data, self.mod)

    def one(self) -> "ModularMatrix":
        if self._rows != self._cols:
            raise ValueError("Only square matrices have a multiplicative identity")
        identity_data = [
            [1 if i == j else 0 for j in range(self._rows)] for i in range(self._rows)
        ]
        return ModularMatrix(identity_data, self.mod)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, ModularMatrix)
            and self.mod == other.mod
            and self.data == other.data
        )

    def __repr__(self) -> str:
        return f"ModularMatrix({self.data}, mod={self.mod})"
