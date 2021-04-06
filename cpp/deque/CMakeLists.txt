cmake_minimum_required(VERSION 3.0)

project(deque)

add_executable(deque deque.cpp)

install(TARGETS deque RUNTIME DESTINATION bin)
