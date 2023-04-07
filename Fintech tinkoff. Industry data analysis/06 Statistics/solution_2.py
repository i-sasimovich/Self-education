import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 601128791 

def exact_solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2
    n = len(x)
    alpha = 1 - p    
    x_new = np.array([el**2 for el in x])
    x2_mean =  x_new.mean()

    chi2_2n =  chi2(df = 2*n)
    chi2_left = chi2_2n.ppf(1 - alpha/2) 
    chi2_right = chi2_2n.ppf(alpha/2)
    left =np.sqrt(n * x2_mean/(14*chi2_left))
    right = np.sqrt(n * x2_mean/(14*chi2_right))
    return (left, right)

