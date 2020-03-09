from src.range_part import RangePart
import tests.test_range_part.utility as u
import pytest as pt


@pt.mark.add
def test_commutative():
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = u.get_rand_range_part()
        assert a + b == b + a


@pt.mark.add
def test_associative():
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = u.get_rand_range_part()
        c = u.get_rand_range_part()
        assert (a + b) + c == a + (b + c)


@pt.mark.add
def test_add_super_range():
    for _ in range(1000):
        parent = u.get_rand_range_part()
        x = u.get_rand_int_in_range(parent.a, parent.b - 1)
        y = u.get_rand_int_in_range(x, parent.b)
        child = RangePart(x, y)

        assert parent.a < child.a < child.b < parent.b
        assert child + parent == parent + child == parent


@pt.mark.add
def test_add_no_overlap():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_below_exclusive(part.a)
        x = u.get_rand_int_below_exclusive(y)
        other = RangePart(x, y)

        assert other.a < other.b < part.a < part.b
        assert other + part == part + other == RangePart(other.a, part.b)


@pt.mark.add
def test_add_overlap_exclusive():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.a)
        y = u.get_rand_int_in_range(part.a, part.b - 1)
        other = RangePart(x, y)

        assert other.a < part.a < other.b < part.b
        assert other + part == part + other == RangePart(other.a, part.b)


@pt.mark.add
def test_add_same_right_bound():
    for _ in range(1000):
        part = u.get_rand_range_part()
        x = u.get_rand_int_below_exclusive(part.b)
        other = RangePart(x, part.b)
        sum_a = min(part.a, other.a)
        assert other + part == part + other == RangePart(sum_a, part.b) == RangePart(sum_a, other.b)


@pt.mark.add
def test_add_same_left_bound():
    for _ in range(1000):
        part = u.get_rand_range_part()
        y = u.get_rand_int_above_exclusive(part.a)
        other = RangePart(part.a, y)
        sum_b = max(part.b, other.b)
        assert other + part == part + other == RangePart(part.a, sum_b) == RangePart(other.a, sum_b)
        

if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])
