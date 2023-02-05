from ward import test
from expycted import expect
from pypliers.itertools import flatmap, flatten
from operator import mul
from functools import partial


@test('flatten() should flatten a nested iterable')
def _():
    lst = [1, [2, [3, 4], 5], 6]
    expect(list(flatten(lst))).to.be_equal_to([1, 2, 3, 4, 5, 6])


@test('flatmap() should map elements and then flatten a nested iterable')
def _():
    lst = [1, [2, 2], 3]
    expect(list(flatmap(partial(mul, 2), lst))).to.be_equal_to([2, 2, 2, 2, 2, 6])
