import pytest as pt
from src.range_part import RangePart
import tests.test_range_part.utility as u


@pt.mark.overlap
def test_left_overlap_out_of_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_in_range_exclusive(part.a, part.b)
        x = u.get_rand_int_below_exclusive(part.a)
        other = RangePart(x, y)
        assert other.a < part.a < other.b < part.b
        assert part.left_overlap_with(other) and other.right_overlap_with(part)


@pt.mark.overlap
def test_right_overlap_out_of_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_in_range(part.a, part.b)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        assert part.a < other.a < part.b < other.b
        assert part.right_overlap_with(other) and other.left_overlap_with(part)


@pt.mark.overlap
def test_left_overlap_in_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_in_range_exclusive(part.a, part.b)
        x = u.get_rand_int_in_range_exclusive(part.a, y)
        other = RangePart(x, y)
        assert part.a < other.a < other.b < part.b
        assert part.left_overlap_with(other) and not other.right_overlap_with(part)


@pt.mark.overlap
def test_right_overlap_in_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_in_range(part.a, part.b)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        assert part.a < other.a < part.b < other.b
        assert part.right_overlap_with(other) and other.left_overlap_with(part)


@pt.mark.overlap
def test_is_sub_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        assert part.is_sub_range(other)
        assert other.is_super_range(part)


@pt.mark.overlap
def test_is_super_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_in_range(part.a, part.b - 1)
        y = u.get_rand_int_in_range(x + 1, part.b)
        other = RangePart(x, y)
        assert part.is_super_range(other)
        assert other.is_sub_range(part)


@pt.mark.overlap
def test_super_range_self():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert part.is_super_range(part)


@pt.mark.overlap
def test_sub_range_self():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert part.is_sub_range(part)


if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])