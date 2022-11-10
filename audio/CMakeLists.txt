cmake_minimum_required(VERSION 3.10.2)
project(audio CXX)

find_package(drwav REQUIRED)

set(SOURCES
    src/audio.cpp
)

add_library(audio ${SOURCES})
target_include_directories(audio PRIVATE include)
target_link_libraries(audio
    PRIVATE 
        drwav::drwav
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING 
        PATTERN "*.hpp"
)
install(TARGETS audio
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
