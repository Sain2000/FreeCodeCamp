import numpy as np

def calculate(l):
    if(len(l)<9):
        raise ValueError("List must contain nine numbers.")
    num_array=np.array([l[:3],l[3:6],l[6:9]])

    calc_mean=[np.mean(num_array, axis=0).tolist(), np.mean(num_array, axis=1).tolist(), np.mean(num_array).tolist()]

    calc_variance=[np.var(num_array, axis=0).tolist(), np.var(num_array, axis=1).tolist(), np.var(num_array).tolist()]

    calc_standard_dev=[np.std(num_array, axis=0).tolist(), np.std(num_array, axis=1).tolist(), np.std(num_array).tolist()]

    calc_max=[np.max(num_array, axis=0).tolist(), np.max(num_array, axis=1).tolist(), np.max(num_array).tolist()]

    calc_min=[np.min(num_array, axis=0).tolist(), np.min(num_array, axis=1).tolist(), np.min(num_array).tolist()]

    calc_sum=[np.sum(num_array, axis=0).tolist(), np.sum(num_array, axis=1).tolist(), np.sum(num_array).tolist()]

    calculations={'mean':calc_mean, 'variance':calc_variance, 'standard deviation':calc_standard_dev, 'max':calc_max, 'min':calc_min, 'sum':calc_sum }
    return calculations