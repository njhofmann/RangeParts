from src.range_part import RangePart
import copy
import pytest as pt
import tests.test_range_part.utility as u


@pt.mark.base
def test_copy():
    for _ in range(1000):
        part = u.get_rand_range_part()
        assert part == copy.copy(part)


@pt.mark.base
def test_equality():
    for _ in range(1000):
        x, y = u.get_rand_pair()
        a = RangePart(x, y)
        b = RangePart(x, y)

        # same object and same hashcode
        assert a == b
        assert hash(a) == hash(b)


@pt.mark.base
def test_invalid_constructor():
    for _ in range(1000):
        x, y = u.get_rand_pair()

        with pt.raises(ValueError):
            RangePart(y, x)


@pt.mark.base
def test_invalid_constructor_equal():
    for _ in range(1000):
        x = u.get_rand_int()

        with pt.raises(ValueError):
            RangePart(x, x)


@pt.mark.base
def test_inequality():  # TODO fix me
    for _ in range(1000):
        a = u.get_rand_range_part()
        b = RangePart(*u.get_rand_pair())
        assert a != b
        assert hash(a) != hash(b)


if __name__ == '__main__':
    pt.main(['-v', f'{__file__}'])
