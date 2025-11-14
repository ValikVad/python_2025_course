

#pragma once

//pybuild
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

//stl

#include <string>
#include <concepts>
#include <type_traits>
#include <thread>
#include <atomic>
#include <time.h>
#include <vector>




//Для гайда
int dif(int a, int b, int c) {
	return a - b + a - c;
}


//1 кейс
template<typename T>
concept Addable = requires(T a, T b) {
    { a + b }->std::same_as<T>;
};

template<Addable T>
T sum(T a, T b) {
    if constexpr (std::integral<T>) {
        if ((b > 0 and a > std::numeric_limits<T>::max() - b) ||
            (b < 0 and a < std::numeric_limits<T>::min() - b)) {
            throw std::overflow_error("Numeric overflow");
        }
    }
    return a + b;
}


//2 кейс
template<typename T, typename V>
concept Multiplyable = requires(T a, V b) {
	{ a* b }->std::same_as<T>;
} or (std::is_same_v<T, std::string> and std::is_integral_v<V> and std::is_unsigned_v<V>);

template<typename T, typename V = T> requires Multiplyable<T, V>
void multi(pybind11::list list, V&& mult) {
    for (size_t i = 0; i < list.size(); ++i) {
        list[i] = list[i].cast<T>() * mult;
    }
}
template<>
void multi<std::string, size_t>(pybind11::list list, size_t&& count) {
    for (size_t i = 0; i < list.size(); ++i) {
        std::string value = std::move(list[i].cast<std::string>());
        std::string temp=value;
        
        value.reserve(value.size() * count);

		size_t power = 1;
		while (power * 2  <= count) {
			value += value;
			power *= 2;
		}
		while (power < count) {
			value += temp;
			++power;
		}
        list[i] = std::move(value);
    }
}

//3 кейс
//https://github.com/CheatsPriest/RaceRandom - более правильная версия нижнего кода
class TrueRandomGenerator {
private:

	size_t victim;
	const int thread_nums;
	const size_t increase_max;

	std::atomic<bool> ready;
	size_t ans;



	void increase() {

		for (int i = 1; i < increase_max; ++i) {
			victim += rand() % (10000);
		}

	}
	void launch() {

		ready = false;


		std::vector<std::thread> pool;
		for (int i = 0; i < thread_nums; ++i) {
			pool.emplace_back([this]() {increase(); });
		}


		for (int i = 0; i < pool.size(); ++i) {
			pool[i].join();
		}

		ans = victim;

		ready = true;
	}

public:

	TrueRandomGenerator() : victim(0), thread_nums(4), increase_max(20000), ans(0) {
		srand(time(0));
	}

	size_t generate() {
		
		launch();
		
		return ans;
	}

};

size_t generator() {
	TrueRandomGenerator gen;
	size_t ans = gen.generate();
	return ans;
}


PYBIND11_MODULE(LowLevelStuff, m) {
	m.doc() = "Bugged C++ module";

	m.def("dif", &dif, "Dif three integers");

	m.def("sum", &sum<long long>, "Add two integers");
	m.def("sum", &sum<long double>, "Add two integers");
	m.def("sum", &sum<std::string>, "Add two strings");


    m.def("mult", &multi<long long>, "Mult integer list by x");
    m.def("mult", &multi<size_t>, "Mult unsigned list by x");
    m.def("mult", &multi<long double>, "Mult float list by x");
    m.def("mult_strings", &multi<std::string, size_t>, "Mult string list by x");

    m.def("rand", &generator, "Generate random num");
}	