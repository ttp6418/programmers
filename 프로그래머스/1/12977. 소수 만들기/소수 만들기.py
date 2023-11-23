import itertools
import numpy as np
import math

def solution(nums):
    answer = 0
    per = list(itertools.combinations(nums, 3))
    for pers in per:
        if print_decimal(np.sum(pers)) == True:
            answer += 1
    return answer

def print_decimal(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True