#include "base.hpp"

#include <iostream>

void base::test() {
    std::cout << "IN base::test()" << std::endl;
    std::cout << "CALLING audio::test()" << std::endl;
    _a.test();
}
