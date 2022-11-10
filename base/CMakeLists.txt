cmake_minimum_required(VERSION 3.10.2)
project(base CXX)

find_package(audio REQUIRED)

set(SOURCES
    src/base.cpp
)

add_library(base ${SOURCES})
target_include_directories(base PUBLIC include)

target_link_libraries(base
    PRIVATE 
        audio::audio
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING
        PATTERN "*.hpp"
)
install(TARGETS base
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
