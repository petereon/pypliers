from ward import test
from pypliers.fntools import if_fn, interpret
from expycted import expect

@test('if_fn() should execute a specific expression along with the arguments to pass to it depending on a condition')
def _():
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    expect(if_fn(True, (add, 1, 2), (sub, 1, 2))).to.be(3)
    expect(if_fn(False, (add, 1, 2), (sub, 1, 2))).to.be(-1)


@test('interpret() should interpret a tuple as a function and its arguments')
def _():
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    expect(interpret((add, (sub, 3, 2), (mul, 2, 3)))).to.be(7)
