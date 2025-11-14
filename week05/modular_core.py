from abc import ABC, abstractmethod
from typing import Self


class ModularNumber(ABC):
    """
    Абстрактный базовый класс для объектов в кольце вычетов по модулю.
    Любой наследник должен поддерживать сложение, умножение и возведение в степень.
    """

    @property
    @abstractmethod
    def mod(self) -> int:
        """Модуль, по которому производятся вычисления."""
        pass

    @abstractmethod
    def __add__(self, other: Self) -> Self:
        """Сложение по модулю."""
        pass

    @abstractmethod
    def __mul__(self, other: Self) -> Self:
        """Умножение по модулю."""
        pass

    @abstractmethod
    def __pow__(self, exponent: int) -> Self:
        """Возведение в неотрицательную целую степень по модулю."""
        pass

    @abstractmethod
    def zero(self) -> Self:
        """Возвращает нейтральный элемент по сложению (нуль)."""
        pass

    @abstractmethod
    def one(self) -> Self:
        """Возвращает нейтральный элемент по умножению (единицу)."""
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        """Сравнение на равенство."""
        pass

    def __radd__(self, other):
        # Поддержка sum([...])
        if other == 0:
            return self
        return NotImplemented

    def __rmul__(self, other):
        if other == 1:
            return self
        return NotImplemented
