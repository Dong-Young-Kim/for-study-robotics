# 위치로 속도를 추정하는 칼만필터 예시

# Initial Train velocity = 25m/s, acc = -0.5m/s^2
# Sense Train Position which have sensing noise (N(0,4))
# Kalman Filter compute current position and velocity

from Kalman import KalmanFilter

import numpy as np
import matplotlib.pyplot as plt

def getPosition(normal: float, sigma: float):
    global pos, vel

    return np.random.normal(normal, sigma, 1)

# Train status generator
class Train:
    def __init__(self, p, v, dt, mean: float, sigma: float):
        self.p = p  # initial true position
        self.v = v  # initial true velocity
        self.dt = dt    # time step
        self.mean = mean    # default mean of sensing noise
        self.sigma = sigma  # default standard deviation of sensing noise

    def Move(self, acc):
        self.p += self.v * self.dt  # Move
        self.v += acc * dt   # Next state velocity Update
    
    def SensePosition(self):
        # add Noise when sense
        return self.p + np.random.normal(self.mean, self.sigma, 1)
    
    def SenseVelocity(self):
        # add Noise when sense
        return self.v + np.random.normal(self.mean, self.sigma, 1)

#################################################

# 축정 오차
MEAN = 0
STDEV = 2

# 열차 초기값
VEL = 25
ACC = -0.5

dt = .1
t = np.arange(0, 20, dt)
trn = Train(0, VEL, dt, MEAN, STDEV)

measured_p = []
filtered_p = []
filtered_v = []
covar_p = []
covar_v = []
true_p = []
true_v = []


# 시스템 모델 변수 초기화
# x : 상태변수 (n*1), [위치, 속도]
# z : 측정값 (m*1), [위치]
A = np.array([[1, dt],
              [0, 1]]) # 시스템 행렬 (n*n)
H = np.array([[1, 0]]) # 출력 행렬 (m*n)
Q = np.array([[1, 0],
              [0, 2]]) # 시스템 오차의 공분산 행렬 (n*n)
R = np.array([[4]]) # 측정 오차의 공분산 행렬 (m*m)

# 초기 예측값
x = np.array([[0],
              [10]]) # 초기 추정값 (초기 위치 = 0, 초기 속도 = 10)
P = np.array([[5, 0],
              [0, 5]]) # 초기 추정값의 오차 공분산


kf = KalmanFilter(x, P, A, H, Q, R)

for i in t:

    trn.Move(ACC)
    z = trn.SensePosition()
    
    kf.Measure(z)

    true_p.append(trn.p)
    true_v.append(trn.v)
    measured_p.append(z)
    filtered_p.append(kf.x_[0])
    filtered_v.append(kf.x_[1])
    covar_p.append(kf.P_[0])
    covar_v.append(kf.P_[1])

    kf.Predict()

#################################################


fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.set_title(f'Position (Mean = ${MEAN}$, $\sigma^2 = {STDEV * STDEV}$)')
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Position (m)')
ax1.grid(True, axis='y')  # Add grid to the graph
ax1.scatter(t, measured_p, color='black', label='Measured', s=7)
ax1.plot(t, true_p, color='blue', label='True')
ax1.plot(t, filtered_p, color='firebrick', label='Kalman Filter')
ax1.legend()

ax2.set_title(f'Velocity (${VEL}m/s$, acc: ${ACC}m/s^2$)')
ax2.set_xlabel('Time (sec)')
ax2.set_ylabel('Velocity (m/s)')
ax2.plot(t, true_v, color='blue', label='True')
ax2.plot(t, filtered_v, color='firebrick', label='Kalman Filter')
ax2.legend()

fig.tight_layout()
plt.show()
