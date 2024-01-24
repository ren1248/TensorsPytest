import numpy as np
import math

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    squared_errors = [(p - t) ** 2 for p, t in zip(pred, tar)]
    mean_squared_error = sum(squared_errors) / len(pred)
    rmse = math.sqrt(mean_squared_error)
    return rmse