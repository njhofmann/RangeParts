from __future__ import annotations
from typing import Union, Any, List, Optional

Number = Union[float, int]


class RangePart:

    def __init__(self, a: Number, b: Number) -> None:
        if a >= b:
            raise ValueError(f'a {a} must be < b {b}')
        self.a = a
        self.b = b

    def __contains__(self, item: Number) -> bool:
        return self.a <= item <= self.b

    def __hash__(self) -> int:
        return hash(frozenset([self.a, self.b]))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, RangePart):
            return other.a == self.a and other.b == self.b
        return False

    def __copy__(self) -> RangePart:
        return RangePart(self.a, self.b)

    def __str__(self) -> str:
        return f'({self.a}, {self.b})'

    def __repr__(self) -> str:
        return type(self).__name__ + ':' + str(self)

    def left_overlap_with(self, other: RangePart) -> bool:
        """
        Returns if the give RangePart overlaps on the left side (inclusive) of this RangePart.
        :param other: RangePart to compare
        :return: if given RangePart overlaps on the left side of this RangePart
        """
        return other.b in self

    def right_overlap_with(self, other: RangePart) -> bool:
        """
        Returns if the give RangePart overlaps on the right side (inclusive) of this RangePart.
        :param other: RangePart to compare
        :return: if given RangePart overlaps on the right side of this RangePart
        """
        return other.a in self

    def is_super_range(self, other: RangePart) -> bool:
        """
        Returns if this RangePart is a super range fo the given RangePart (is its range within this RangePart's range).
        :param other: RangePart to compare against
        :return: if this RangePart is a super range of the given RangePart
        """
        return self.left_overlap_with(other) and self.right_overlap_with(other)

    def is_sub_range(self, other: RangePart) -> bool:
        """
        Returns if this RangePart is a sub range fo the given RangePart (is this RangePart's range is within the given
        RangePart's range).
        :param other: RangePart to compare against
        :return: if this RangePart is a sub range of the given RangePart
        """
        return other.is_super_range(self)

    def __add__(self, other: RangePart):
        if self == other:
            return self
        elif self.is_super_range(other):
            return self
        elif other.is_super_range(self):
            return other
        elif self.left_overlap_with(other):
            return RangePart(other.a, self.b)
        elif self.right_overlap_with(other):
            return RangePart(self.a, other.b)
        elif other.left_overlap_with(self):
            return RangePart(self.a, other.b)
        elif other.right_overlap_with(self):
            return RangePart(other.a, self.b)
        elif other.b < self.a:
            return RangePart(other.a, self.b)
        return RangePart(self.a, other.b)

    def __sub__(self, other: RangePart) -> Optional[List[RangePart]]:
        if self == other:
            return None

        elif self.is_super_range(other):

            if self.b == other.b:
                return [RangePart(self.a, other.a)]
            elif self.a == other.a:
                return [RangePart(other.b, self.b)]
            return [RangePart(self.a, other.a), RangePart(other.b, self.b)]

        elif self.is_sub_range(other):
            return other - self

        elif self.left_overlap_with(other):

            if self.a == other.b:
                return [other, self]
            return [RangePart(other.a, self.a), RangePart(other.b, self.b)]

        elif self.right_overlap_with(other):

            if self.b == other.a:
                return [self, other]
            return [RangePart(self.a, other.a), RangePart(self.b, other.b)]

        # no overlap
        return [self, other] if self < other else [other, self]

    def __le__(self, other: RangePart) -> bool:  # x <= y
        return True if self == other else self < other

    def __lt__(self, other: RangePart) -> bool:  # x < y
        if self.b > other.b:
            return False
        elif self.b < other.b:
            return True
        elif self.a < other.a:  # self.b == other.b then
            return True
        return False

    def __gt__(self, other: RangePart) -> bool:   # x > y
        return not (self <= other)

    def __ge__(self, other: RangePart) -> bool:  # x >= y
        return True if self == other else self > other
