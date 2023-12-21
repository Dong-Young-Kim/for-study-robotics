#include <vector>

namespace l3dod{
class Mat {
private:
    std::vector<std::vector<int>> mat;

public:
    Mat(const std::vector<std::vector<int>>& matrix) : mat(matrix) {}

    // 복사 생성자
    Mat(const Mat& other) : mat(other.mat) {}

    // 대입 연산자 오버로딩
    Mat& operator=(const Mat& other) {
        mat = other.mat;
        return *this;
    }

    // 덧셈 연산자
    Mat operator+(const Mat& other) const {
        int n = mat.size();
        std::vector<std::vector<int>> result(n, std::vector<int>(n, 0));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                result[i][j] = mat[i][j] + other.mat[i][j];
            }
        }

        return Mat(result);
    }

    // 뺄셈 연산자
    Mat operator-(const Mat& other) const {
        int n = mat.size();
        std::vector<std::vector<int>> result(n, std::vector<int>(n, 0));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                result[i][j] = mat[i][j] - other.mat[i][j];
            }
        }

        return Mat(result);
    }

    // // Strassen의 행렬 곱셈 알고리즘
    // Mat operator*(const Mat& other) const {
    //     int n = mat.size();

    //     if (n == 1) {
    //         std::vector<std::vector<int>> result(1, std::vector<int>(1, 0));
    //         result[0][0] = mat[0][0] * other.mat[0][0];
    //         return Mat(result);
    //     }

    //     int newSize = n / 2;

    //     std::vector<std::vector<int>> A11(newSize, std::vector<int>(newSize));
    //     // ... 나머지 행렬 분할 코드는 이전 코드와 동일합니다.

    //     // 나머지 Strassen 알고리즘 코드는 이전과 같습니다.
    //     // ...

    //     return Mat(result);
    // }

    // // 행렬 출력 함수
    // void print() const {
    //     for (const auto& row : mat) {
    //         for (int element : row) {
    //             std::cout << element << " ";
    //         }
    //         std::cout << std::endl;
    //     }
    // }

    // 역행렬 반환 함수
    Mat inv() const {
    }


};
}; // namespace l3dod