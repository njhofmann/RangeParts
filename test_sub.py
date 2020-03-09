from src.range_part import RangePart
import tests.test_range_part.utility as u
import pytest as pt


@pt.mark.sub
def test_sub_self():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert not part - part


@pt.mark.sub
def test_commutative():
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = u.get_rand_range_part()
        assert a - b == b - a


@pt.mark.sub
def test_no_overlap():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_above_exclusive(part.b)
        y = u.get_rand_int_above_exclusive(x)
        other = RangePart(x, y)
        diff = [part, other] if part < other else [other, part]
        assert part - other == other - part == diff


@pt.mark.sub
def test_left_overlap_on_bounds():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        other = RangePart(x, part.a)
        assert part.left_overlap_with(other)
        assert other.a < part.a == other.b < part.b
        assert part - other == other - part == [other, part]


@pt.mark.sub
def test_left_overlap_in_bounds():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        y = u.get_rand_int_in_range_exclusive(part.a, part.b)
        other = RangePart(x, y)
        assert part.left_overlap_with(other)
        assert other.a < part.a < other.b < part.b
        assert part - other == other - part == [RangePart(other.a, part.a), RangePart(other.b, part.b)]


@pt.mark.sub
def test_right_overlap_on_bounds():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(part.b, y)
        diff = [part, other]
        assert part.right_overlap_with(other)
        assert part.a < other.a == part.b < other.b
        assert part - other == other - part == diff


@pt.mark.sub
def test_right_overlap_in_bounds():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_in_range_exclusive(part.a, part.b)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        diff = [RangePart(part.a, other.a), RangePart(part.b, other.b)]
        assert part.right_overlap_with(other)
        assert part.a < other.a < part.b < other.b
        assert part - other == other - part == diff


@pt.mark.sub
def test_super_sub_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        y = u.get_rand_int_above_exclusive(part.b)
        other = RangePart(x, y)
        diff = [RangePart(other.a, part.a), RangePart(part.b, other.b)]
        assert other.a < part.a < part.b < other.b
        assert other.is_super_range(part)
        assert part.is_sub_range(other)
        assert part - other == other - part == diff


if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])
