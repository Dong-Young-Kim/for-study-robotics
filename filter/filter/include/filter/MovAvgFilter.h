#ifndef MOVAVG_FILTER_H
#define MOVAVG_FILTER_H

#include <queue>

class MovAvgFilter {
private:
    int window_size_;
    double average_value_;
    std::queue<double> data_queue_;

public:

    MovAvgFilter(int window_size = 0, double average_value = 0.0);
    double GetEstimatedValue() const;
    double Update(double input);


};

#endif // MOVAVG_FILTER_H