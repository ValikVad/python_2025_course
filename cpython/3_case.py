import unittest
import pybind11
import LowLevelStuff
import random
import time
import collections

random.seed(time.time())

def base():
        

    cpp_counter = collections.Counter()
    py_counter = collections.Counter()

    cpp_wins = 0
    py_wins = 0
    draws = 0
    
    max_rounds = 1000
    mod = 1000
    win_threshold = 2

    for round_num in range(max_rounds):
        
        cpp_num = LowLevelStuff.rand() % mod  
        py_num = random.randint(0, mod-1)        
        
        
        cpp_counter[cpp_num] += 1
        py_counter[py_num] += 1
        
        
        cpp_win = cpp_counter[cpp_num] >= win_threshold
        py_win = py_counter[py_num] >= win_threshold
        
        if cpp_win and py_win:
            draws += 1
            
        elif cpp_win:
            cpp_wins += 1
            
        elif py_win:
            py_wins += 1
            
        
        
        if abs(cpp_wins - py_wins) > 50:
            break
    print("\n" + "=" * 50)
    print("🏁 ИТОГИ БИТВЫ:")
    print(f"🔧 C++ побед: {cpp_wins}")
    print(f"🐍 Python побед: {py_wins}") 
    print(f"⚡ Ничьих: {draws}")
    print(f"📊 Всего раундов: {round_num + 1}")
    
    if cpp_wins > py_wins:
        print("🎉 ПОБЕДИТЕЛЬ: C++ ГЕНЕРАТОР!")
        return "C++"
    elif py_wins > cpp_wins:
        print("🎉 ПОБЕДИТЕЛЬ: PYTHON ГЕНЕРАТОР!")
        return "Python"
    else:
        print("🤝 НИЧЬЯ!")
        return "Draw"

class TestMult(unittest.TestCase):

    None

base()
    
