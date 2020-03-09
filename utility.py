from src.range_part import RangePart
import sys
import random as r

MIN_RANGE_PART_SPACING = 10


def get_rand_int_below_exclusive(x):
    """
    Returns a int in the range of [-sys.maxsize, x - 1]
    :param x: upper bound (exclusive) of range from which random int is drawn from
    :return: random int in [-sys.maxsize, x - 1]
    """
    return get_rand_int_in_range_exclusive(-sys.maxsize, x)


def get_rand_int_above_exclusive(x):
    """
    Returns a int in the range of [x + 1, sys.maxsize]
    :param x: lower bound (exclusive) of range from which random int is drawn from
    :return: random int in [x + 1, sys.maxsize]
    """
    return get_rand_int_in_range_exclusive(x, sys.maxsize)


def get_rand_int_in_range(x, y):
    return r.randint(x, y)


def get_rand_int():
    return r.randint(-sys.maxsize, sys.maxsize)


def get_rand_int_in_range_exclusive(x, y):
    # return num in (x, y)
    num = get_rand_int_in_range(x, y)
    while num in (x, y):
        num = get_rand_int_in_range(x, y)
    return num


def get_rand_int_in_range_inclusive(x, y):
    # return num in [x, y]
    return get_rand_int_in_range(x, y)


def get_rand_pair():
    x = get_rand_int()
    y = get_rand_int()
    while (y - x) < MIN_RANGE_PART_SPACING:
        y = get_rand_int()
    return x, y


def get_rand_range_part():
    return RangePart(*get_rand_pair())
