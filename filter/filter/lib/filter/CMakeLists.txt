# add all source files in this directory to the executable
file(GLOB_RECURSE SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp
)

add_library(${PROJECT_NAME} STATIC ${SOURCES})

# add include directories
target_include_directories(${PROJECT_NAME} PUBLIC 
    ${CMAKE_SOURCE_DIR}/include
)

# compile options
target_compile_options(${PROJECT_NAME} PRIVATE -Wall)

# compile features
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)

# add dependencies
# target_link_libraries(${PROJECT_NAME} PUBLIC
#     ${OpenCV_LIBS}
#     ${Boost_LIBRARIES}
#     ${CMAKE_THREAD_LIBS_INIT}
#     ${CMAKE_DL_LIBS}
#     ${CMAKE_CURRENT_SOURCE_DIR}/../lib/libdarknet.so
# )

# external libraries