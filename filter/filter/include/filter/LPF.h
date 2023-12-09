#ifndef LPF_H
#define LPF_H

class LPF {
private:
    double alpha_;
    double estimated_value_;

public:
    LPF(double alpha, double estimated_value = 0.0);
    double GetEstimatedValue() const;
    double Update(double input);
};

#endif // LPF_H
