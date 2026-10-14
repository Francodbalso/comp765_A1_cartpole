import math
import numpy as np
import scipy.linalg

# Uncomment this line if you want to use our LQR starter/library code
from lqr_starter import k

class Controller:
    def __init__(self, swingup=False) -> None:
        # TODO: Fill in based on controller specifications.
        self.swingup = swingup
        pass

    def compute_control(self, x):
        goal = np.array([0, 0, 0, np.pi])
        error = goal - x
        control = k @ error

        if self.swingup:
            angle = (x[3] + np.pi) % (2 * np.pi) - np.pi
            if abs(angle) < 2.6:
                control = -15 * x[0]
                if abs(x[0]) < 0.1:
                    if abs(x[1]) < 0.1:
                        control = 20
                    else:
                        control = 4*x[1]
        
        return control