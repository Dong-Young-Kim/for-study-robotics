# add all source files in this directory to the executable
file(GLOB_RECURSE SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp
)

# add the executable
add_executable(filter_run ${SOURCES})

# link the executable to the library
target_link_libraries(filter_run PUBLIC ${PROJECT_NAME})