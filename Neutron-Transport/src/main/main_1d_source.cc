#include <iostream>

#include "ellpack.h"

int main () {
    size_t npoints = 10;
    Ellpack A(npoints, npoints, 3);

    double length = 10.0;
    double h = length / (npoints - 1);
    double d = 1.0;
    double xs_a = 1.0;

    for(int i = 0; i < npoints; i++) {
        double a = -d / (h * h);
        double b = 2 * d / (h * h) + xs_a;
        A.add(i, i - 1, b);
        A.add(i, i, b);
        A.add(i, i + 1, a);
    }

    std::vector<double> source (npoints, 1.0);
    std::vector<double> phi (npoints, 0.0);

    A.solve_cg(phi, source);

    for(const double v : phi) {
        std::cout << v << ",";
    }
    std::cout  << std::endl;
    return 0;
}