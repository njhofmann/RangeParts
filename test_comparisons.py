import pytest as pt
import tests.test_range_part.utility as u
from src.range_part import RangePart


def test_transitivity():
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = u.get_rand_range_part()
        c = u.get_rand_range_part()

        if a < b and b < c:
            assert a < c
        elif b < c and c < a:
            assert b < c
        elif c < b and b < a:
            assert c < a
        elif a < c and c < b:
            assert a < b
        elif c < a and a < b:
            assert c < b
        elif b < a and a < c:
            assert b < c
        else:
            assert False, (a < b, a < c, b < c, c < b, c < a, b < a)


def test_addition():
    pass


def test_reversal():
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = u.get_rand_range_part()

        if a < b:
            assert b > a
        elif b < a:
            assert a > b
        else:
            assert a == b


def test_same_right_bound_left_bound_in_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_in_range_exclusive(part.a, part.b)
        other = RangePart(x, part.b)
        assert other > part and part < other and part != other


def test_same_right_bound_left_bound_out_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        other = RangePart(x, part.b)
        assert part > other and other < part and other != part


def test_same_left_bound_right_bound_in_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_in_range_exclusive(part.a, part.b)
        other = RangePart(part.a, y)
        assert part > other and other < part and part != other


def test_same_left_bound_right_bound_out_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(part.a, y)
        assert other > part and part < other and other != part


def test_super_sub_range_exclusive():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        assert other.is_super_range(part) and part.is_sub_range(other)
        assert other > part and part < other and part != other


def test_no_overlap():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_above_exclusive(part.b)
        y = u.get_rand_int_above_exclusive(x)
        other = RangePart(x, y)
        assert not other.right_overlap_with(part) and not other.left_overlap_with(part)
        assert other > part and part < other and part != other


if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])
