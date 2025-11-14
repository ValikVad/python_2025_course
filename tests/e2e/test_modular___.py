from unittest.mock import Mock

import pytest
from matrix_operation import ModularMatrix
from modular_number import ModularInt


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (ModularInt(1, 5), ModularInt(2, 5), ModularInt(3, 5)),
        (ModularInt(-5, 5), ModularInt(2, 5), ModularInt(2, 5)),
    ],
    ids=["test1", "test2"],
)
def test_dummy(a, b, expected_result):
    assert a + b == expected_result


def e_matrix_22(request):
    return ModularMatrix([[1, 0], [0, 1]], mod=request.param)


@pytest.mark.parametrize(
    "a, b, expected_error",
    [
        (1, ModularInt(2, 5), TypeError),
        (ModularInt(-5, 6), ModularInt(2, 5), ValueError),
    ],
    ids=["test1", "test2"],
)
def test_incorect_type_add(a, b, expected_error):

    with pytest.raises(expected_error):
        b + a


def det():
    raise NotImplementedError


def test_matrix_add():
    a = ModularMatrix([[1, 1], [5, 2]], mod=4)
    b = ModularMatrix([[3, 3], [5, 2]], mod=4)
    det = Mock(return_value=ModularInt(2, 4))
    assert det() == ModularInt(2, 4)
    assert a + b == ModularMatrix([[0, 0], [2, 0]], mod=4)


# @pytest.mark.parametrize("mod", [5, 4])
# def test_matrix_mul(e_matrix_22, mod):
#     b =
#     a = ModularMatrix([[1, 1], [5, 2]], mod = mod)
#     assert a * e_matrix_22 == a
