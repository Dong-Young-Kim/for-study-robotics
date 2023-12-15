from Kalman import KalmanFilter

import numpy as np
import matplotlib.pyplot as plt

def getConstPlusNoise(mean: float, sigma: float):
    return np.random.normal(mean, sigma, 1)

#################################################

# 입력 난수
MEAN = 0
STDEV = 5

dt = 0.2
t = np.arange(0, 30, 0.2)
measured_z = []
covar_p = []
filtered_x = []
kalmanGain_k = []

# 시스템 모델 변수 초기화
# x : 상태변수 (n*1)
# z : 측정값 (m*1)
A = np.array([[1]]) # 시스템 행렬 (n*n)
H = np.array([[1]]) # 출력 행렬 (m*n)
Q = np.array([[0]]) # 시스템 오차의 공분산 행렬 (n*n)
R = np.array([[25]]) # 측정 오차의 공분산 행렬 (m*m)

# 초기 예측값
x = np.array([[14]]) # 초기 추정값
P = np.array([[6]]) # 초기 추정값의 오차 공분산

#################################################

kf = KalmanFilter(x, P, A, H, Q, R)

for i in t:
    z = getConstPlusNoise(MEAN, STDEV)
    
    kf.Measure(z)

    measured_z.append(z[0])
    filtered_x.append(kf.x_[0])
    covar_p.append(kf.P_[0])
    kalmanGain_k.append(kf.K_[0])

    kf.Predict()

#################################################


fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.set_title(f'Data (Mean = ${MEAN}$, $\sigma^2 = {STDEV * STDEV}$)')
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Value')
ax1.grid(True, axis='y')  # Add grid to the graph
ax1.scatter(t, measured_z, color='black', label='Measured', s=7)
upper_bound = filtered_x + np.sqrt(covar_p)
lower_bound = filtered_x - np.sqrt(covar_p)
ax1.fill_between(t, upper_bound.flatten(), lower_bound.flatten(), alpha=0.5, color='peachpuff', label='Covariance')
ax1.plot(t, filtered_x, color='firebrick', label='Kalman Filter', marker='o', markersize=3)
ax1.legend()

ax2.set_title('Kalman Gain')
ax2.set_xlabel('Time (sec)')
ax2.set_ylabel('Value')
ax2.plot(t, kalmanGain_k, color='blue', label='Kalman Gain')
ax2.legend()

fig.tight_layout()
plt.show()

