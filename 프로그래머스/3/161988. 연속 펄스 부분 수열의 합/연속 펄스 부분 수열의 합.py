import numpy as np

def solution(sequence):
    sequence = [value * (-1 if index % 2 else 1) for[index, value] in enumerate(sequence)]
    
    for i in range(len(sequence) - 1):
        sequence[i + 1] = sequence[i + 1] + sequence[i]
        
    return max(np.abs(np.max(sequence)), np.abs(np.min(sequence)), (np.max(sequence)) - (np.min(sequence))).tolist()