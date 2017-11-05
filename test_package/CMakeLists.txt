project( ZlibConanPackageTest )
cmake_minimum_required( VERSION  3.0 )
include( "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake" )
conan_basic_setup( TARGETS )

add_executable( ZlibPackageTest
    enough.c
)
target_link_libraries( ZlibPackageTest
    PRIVATE  CONAN_PKG::zlib
)
