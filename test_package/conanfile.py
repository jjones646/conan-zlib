import os

from conans.model.conan_file import ConanFile
from conans import CMake


class ZlibConanPackageTest(ConanFile):
    version = '0.0.0'
    settings = 'os', 'compiler', 'arch', 'build_type'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run('cd bin && .{!s}ZlibPackageTest'.format(os.sep))
        assert os.path.exists(os.path.join(self.deps_cpp_info['zlib'].rootpath, 'LICENSE'))
