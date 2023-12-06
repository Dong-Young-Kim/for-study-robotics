cmake_minimum_required(VERSION 3.15)

project(
    filter
    VERSION 0.1
    DESCRIPTION "filter 알고리즘"
    LANGUAGES CXX
)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

add_subdirectory(app)
add_subdirectory(lib)
