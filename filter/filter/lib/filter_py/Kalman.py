import numpy as np

class KalmanFilter:
    def __init__(self, 
            x: np.ndarray, 
            P: np.ndarray, 
            A: np.ndarray, 
            H: np.ndarray, 
            Q: np.ndarray, 
            R: np.ndarray):
        self.x_ = x
        self.xpred_ = x
        self.P_ = P
        self.Ppred_ = P
        self.A_ = A
        self.H_ = H
        self.Q_ = Q
        self.R_ = R
        self.K_ = np.zeros_like(x)
        
    def Predict(self):
        self.xpred_ = self.A_ @ self.x_
        self.Ppred_ = self.A_ @ self.P_ @ self.A_.T + self.Q_
        
    def Measure(self, z :np.ndarray):
        self.K_ = self.Ppred_ @ self.H_.T @ np.linalg.inv(self.H_ @ self.Ppred_ @ self.H_.T + self.R_)

        self.x_ = self.xpred_ + self.K_ @ (z - self.H_ @ self.xpred_)
        self.P_ = self.Ppred_ - self.K_ @ self.H_ @ self.Ppred_
