cmake_minimum_required (VERSION 3.8)

project ("LowLevelStuff")

find_package(Python REQUIRED COMPONENTS Development)
add_subdirectory(pybind11)

pybind11_add_module(LowLevelStuff "LowLevelStuff.cpp" "LowLevelStuff.h")

set_target_properties(LowLevelStuff PROPERTIES
    OUTPUT_NAME "LowLevelStuff"
    PREFIX ""
    SUFFIX ".pyd"
    CXX_STANDARD 20
    CXX_STANDARD_REQUIRED ON
)