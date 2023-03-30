from typing import Iterable, Sequence, List, Tuple
"""unction’s parameters and return values with the appropriate types"""


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
