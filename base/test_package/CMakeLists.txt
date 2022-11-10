cmake_minimum_required(VERSION 3.10.2)
project(base-tests CXX)

find_package(base REQUIRED)

add_executable(base-tests src/base_test.cpp)

target_link_libraries(base-tests
    PRIVATE
        base::base
)
target_include_directories(base-tests PRIVATE include)

enable_testing()
add_test(NAME base-tests
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
         COMMAND base-tests)
