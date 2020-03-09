from typing import List, Iterable, Union, Dict, Optional
from range_part import Number, RangePart


class WholeRange:

    def __init__(self, start: Number, end: Number, step: Number, round_err: Optional[int] = None) -> None:
        if step == 0:
            raise ValueError(f'step {step} must be non-zero')
        elif start == end:
            raise ValueError(f'start {start} can not equal end {end}')
        if start > end and step > 0:
            raise ValueError(f'if start {start} is > than end {end}, then step {step} must be negative')
        elif start < end and step < 0:
            raise ValueError(f'if start {start} is < than end {end}, then step {step} must be positive')

        self.start = start
        self.end = end
        self.step = step
        self.range_parts = self.get_range_parts()
        self.rnd = round_err

    def get_range_parts(self) -> List[RangePart]:
        float_range = []
        prev_start = self.start
        next_start = prev_start + self.step
        while self.in_range(next_start):
            range_part = RangePart(prev_start, next_start) \
                if prev_start < next_start \
                else RangePart(next_start, prev_start)
            float_range.append(range_part)
            prev_start = next_start
            next_start += self.step

        if prev_start < self.end:
            end_part = float_range.pop()
            float_range.append(RangePart(end_part.b, self.end))

        return float_range

    def create_range_counts(self, nums: Iterable[Union[float, int]]) -> Dict[RangePart, int]:
        parts_to_counts = {part: 0 for part in self.range_parts}
        for num in nums:

            if not self.in_range(num):
                num = self.end if num > self.end else self.start

            for part, count in parts_to_counts.items():
                if num in part:
                    parts_to_counts[part] = count + 1

        return parts_to_counts

    def __str__(self) -> str:
        return ', '.join([str(part) for part in self.range_parts])

    def __repr__(self) -> str:
        return type(self).__name__ + ': ' + str(self)

    def in_range(self, num: Number) -> bool:
        start, end = (self.start, self.end) \
            if self.start < self.end \
            else (self.end, self.start)
        return start <= num <= end

    def as_list(self) -> List[Number]:
        return [self.range_parts[0].a] + [part.b for part in self.range_parts]

