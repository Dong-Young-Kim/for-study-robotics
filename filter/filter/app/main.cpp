#include <filter/LPF.h>
#include <filter/AvgFilter.h>

#include <iostream>
#include <random>

// class FilterTester {
// public:
//     FilterTester() {}

//     double filter(double input) {
//         return lpf_.Update(input);
//     }
// };

class MakeInput {

private:
    std::default_random_engine generator_;
    std::normal_distribution<double> distribution_;

public:
    MakeInput(double mean, double stddev)
        : generator_(std::random_device()()), distribution_(mean, stddev) 
    {}

    double makeInput() {
        return distribution_(generator_);
    }
};


int main() {
    // LPF lpf(0.5); // Set the alpha value for the LPF

    // // Apply the LPF to some input values
    // double input1 = 1.0;
    // double output1 = lpf.filter(input1);
    // std::cout << "Output 1: " << output1 << std::endl;

    for (int i = 0; i < 100; i++) {
        MakeInput makeInput(0.0, 1.0);
        double input = makeInput.makeInput();
        std::cout << "Input: " << input << std::endl;
    }
    return 0;
}
