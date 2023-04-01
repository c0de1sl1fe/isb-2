# from cmath import sqrt
import math


def frequency_bitwise_test(sequence: list) -> float:
    return math.erfc((abs(sum(sequence))/math.sqrt(128))/math.sqrt(2))