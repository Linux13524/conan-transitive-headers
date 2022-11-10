from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout

required_conan_version = ">=1.52.0"


class AudioConan(ConanFile):
    name = "audio"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "src/*", "include/*", "CMakeLists.txt"

    def validate(self):
        check_min_cppstd(self, "17")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def requirements(self):
        self.requires("drwav/0.13.7", transitive_headers=True)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["audio"]
        self.cpp_info.set_property("cmake_file_name", "audio")
        self.cpp_info.set_property("cmake_target_name", "audio::audio")
