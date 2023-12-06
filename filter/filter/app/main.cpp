#include <filter/LPF.h>
#include <iostream>

int main() {
    LPF lpf(0.5); // Set the alpha value for the LPF

    // Apply the LPF to some input values
    double input1 = 1.0;
    double output1 = lpf.filter(input1);
    std::cout << "Output 1: " << output1 << std::endl;


    return 0;
}
