import pybind11
import LowLevelStuff
import numpy as np


def sum_test_base(a, b, target_result):

    result = 0
    try:
        result = LowLevelStuff.sum(a, b)
        
    except Exception as err:
        result = str(err)

    assert result==target_result, (f"Error: Expected: {target_result} | Got: {result}")

def test_sum1():
    sum_test_base(1, 8, 9)
def test_sum2():
    sum_test_base("Hello, ", "World!", "Hello, World!")
def test_sum3():
    x = np.int64(9223372036854775807)  
    y = np.int64(1)
    sum_test_base(x, y, "Numeric overflow")



def test_sum_invoker():
    try:
        test_sum1()
    except Exception as err:
        print(err)
    
    try:
        test_sum2()
    except Exception as err:
        print(err)
    
    try:
        test_sum3()
    except Exception as err:
        print(err)
        
test_sum_invoker()



