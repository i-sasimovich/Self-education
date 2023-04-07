import pandas as pd
import numpy as np


chat_id = 601128791 

def solution(x: np.array) -> float:
    t = 57
    a = 2x / 2t**2
    
    return a.mean()