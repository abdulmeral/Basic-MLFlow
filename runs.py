import numpy as np
import os

alphas = np.linspace(0.1, 1.0, 5)
l1Ratios = np.linspace(0.1, 1.0, 5)

for alpha in alphas:
    for l1Ratio in l1Ratios:
        os.system(f"python example2.py -a {alpha} -l1 {l1Ratio}")