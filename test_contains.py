import pytest as pt
import tests.test_range_part.utility as u


@pt.mark.contains
def test_from_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        item = u.get_rand_int_in_range(part.a, part.b)
        assert item in part


@pt.mark.contains
def test_above_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        item = u.get_rand_int_above_exclusive(part.b)
        assert item not in part


@pt.mark.contains
def test_below_range():
    for _ in range(1000):
        part = u.get_rand_range_part()
        item = u.get_rand_int_below_exclusive(part.a)
        assert item not in part


@pt.mark.contains
def test_left_bound():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert part.a in part


@pt.mark.contains
def test_right_bound():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert part.b in part


if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])
