from modular_core import ModularNumber


class ModularInt(ModularNumber):
    def __init__(self, value: int, mod: int):
        if mod <= 0:
            raise ValueError("Modulus must be positive")
        self._mod = mod
        self._value = value % mod

    @property
    def mod(self) -> int:
        return self._mod

    @property
    def value(self) -> int:
        return self._value

    def __add__(self, other: "ModularInt") -> "ModularInt":
        if not isinstance(other, ModularInt):
            return NotImplemented
        if self.mod != other.mod:
            raise ValueError("Moduli must match")
        return ModularInt(self.value + other.value, self.mod)

    def __mul__(self, other: "ModularInt") -> "ModularInt":
        if not isinstance(other, ModularInt):
            return NotImplemented
        if self.mod != other.mod:
            raise ValueError("Moduli must match")
        return ModularInt(self.value * other.value, self.mod)

    def __pow__(self, exponent: int) -> "ModularInt":
        if exponent < 0:
            raise ValueError("Negative exponents not supported")
        return ModularInt(pow(self.value, exponent, self.mod), self.mod)

    def zero(self) -> "ModularInt":
        return ModularInt(0, self.mod)

    def one(self) -> "ModularInt":
        return ModularInt(1, self.mod)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, ModularInt)
            and self.value == other.value
            and self.mod == other.mod
        )

    def __repr__(self) -> str:
        return f"ModularInt({self.value}, mod={self.mod})"
