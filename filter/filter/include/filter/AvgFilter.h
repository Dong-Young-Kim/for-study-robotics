#ifndef AVG_FILTER_H
#define AVG_FILTER_H

class AvgFilter {
private:
    long long data_size_;
    double average_value_;

public:
    AvgFilter(long long data_size = 0, double average_value = 0.0);
    double GetEstimatedValue() const;
    double Update(double input);
};

#endif // AVG_FILTER_H
