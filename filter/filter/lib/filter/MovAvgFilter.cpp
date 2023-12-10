#include <filter/MovAvgFilter.h>

MovAvgFilter::MovAvgFilter(int window_size, double average_value)
    : window_size_(window_size), average_value_(average_value)
{
    for (int i = 0; i < window_size_; i++) {
        data_queue_.push(average_value_);
    }
}

double MovAvgFilter::GetEstimatedValue() const
{
    return average_value_;
}

double MovAvgFilter::Update(double input)
{
    data_queue_.push(input);
    average_value_ += (input - data_queue_.front()) / window_size_;
    data_queue_.pop();
    return average_value_;
}
