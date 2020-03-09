from src.whole_range import WholeRange
from src.range_part import Number, RangePart
from typing import List, Optional


class RangeNode:

    def __init__(self, range_part: RangePart) -> None:
        self.range_part: RangePart = range_part
        self.left: Optional[RangeNode] = None
        self.right: Optional[RangeNode] = None
        self.items: List[Number] = []

    def __len__(self) -> int:
        return len(self.items)

    def insert(self, num: Number) -> None:
        err_msg = f'value {num} is outside the range of this RangeTree'
        if num in self.range_part:
            self.items.append(num)
        elif num < self.range_part.a:
            if self.left:
                self.left.insert(num)
            else:
                raise ValueError(err_msg)
        else:  # num > self.range_part.b
            if self.right:
                self.right.insert(num)
            else:
                raise ValueError(f'value {num} is outside the range of this RangeTree')

    def __str__(self) -> str:
        return f'Range of {self.range_part.a}, {self.range_part.b} with items {", ".join(map(str, self.items))}'

    def __repr__(self):
        return type(self).__name__ + ':' + str(self)


class RangeTree:

    def __init__(self, whole_range: WholeRange) -> None:
        self.whole_range = whole_range
        self.root = self.setup_tree()

    def setup_tree(self) -> RangeNode:
        pass

    def add(self, num: Number) -> None:
        if num not in self.whole_range:
            raise ValueError(f'value {num} is not in the range of [{self.whole_range.start}, {self.whole_range.end}]')
        self.root.insert(num)
