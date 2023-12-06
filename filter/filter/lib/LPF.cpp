#include <filter/LPF.h>

LPF::LPF(double alpha, double estimated_value)
    : alpha_(alpha), estimated_value_(estimated_value)
{

}

double LPF::filter(double input) {
    estimated_value_ = (1 - alpha_) * input + alpha_ * estimated_value_;
    return estimated_value_;
}


