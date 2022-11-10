cmake_minimum_required(VERSION 3.10.2)
project(audio-tests CXX)

find_package(audio REQUIRED)

add_executable(audio-tests src/audio_test.cpp)

target_link_libraries(audio-tests
    PRIVATE
        audio::audio
)
target_include_directories(audio-tests PRIVATE include)

enable_testing()
add_test(NAME audio-tests
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
         COMMAND audio-tests)
