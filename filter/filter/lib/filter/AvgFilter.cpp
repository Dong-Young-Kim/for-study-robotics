#include <filter/AvgFilter.h>

AvgFilter::AvgFilter(long long data_size, double average_value)
    : data_size_(data_size), average_value_(average_value) {}

double AvgFilter::GetEstimatedValue() const {
    if (data_size_ == 0) {
        return 0;
    }
    return average_value_;
}

double AvgFilter::Update(double input) {
    average_value_ = (data_size_ * average_value_ + input) / (data_size_ + 1);
    data_size_++;
    return average_value_;
}
