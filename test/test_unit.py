from pypliers.dicttools import flatten_dict, walk_deep, assoc, assoc_in, get, get_in, dissoc, dissoc_in
from ward import test
from expycted import expect
from operator import methodcaller


@test('walk_deep() should apply a function to all values in a nested dict')
def _():
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
            },
        },
        'e': 4,
    }
    expect(walk_deep(lambda x: x * 2, d)).to.be_equal_to({
        'a': 2,
        'b': {
            'c': 4,
            'd': {
                'e': 6,
            },
        },
        'e': 8,
    })

@test('walk_deep() should apply a function to all keys in a nested dict if `walk_keys` param is `True`')
def _():
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
            },
        },
        'e': 4,
    }
    expect(walk_deep(methodcaller('upper'), d, True)).to.be_equal_to({
        'A': 1,
        'B': {
            'C': 2,
            'D': {
                'E': 3,
            },
        },
        'E': 4,
    })

@test('flatten_dict() should flatten a nested dict')
def _():
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
            },
        },
        'e': 4,
    }
    expect(list(flatten_dict(d))).to.be_equal_to([
        (['a'], 1),
        (['b', 'c'], 2),
        (['b', 'd', 'e'], 3),
        (['e'], 4),
    ])

@test('get() should get a value from a dict')
def _():
    d = {'a': 1}
    expect(get(d, 'a')).to.be_equal_to(1)
    expect(get(d, 'b')).to.be_equal_to(None)

@test('get_in() should get a value from a nested dict')
def _():
    d = {'a': {'b': {'c': 1}}}
    expect(get_in(d, ['a', 'b', 'c'])).to.be_equal_to(1)
    expect(get_in(d, ['a', 'b', 'd'])).to.be_equal_to(None)

@test('assoc() should associate a key with a value in a dict')
def _():
    d = {'a': 1}
    expect(assoc(d, 'b', 2)).to.be_equal_to({'a': 1, 'b': 2})

@test('assoc_in() should associate a key with a value in a nested dict')
def _():
    d = {'a': {'b': {'c': 1}}}
    expect(assoc_in(d, ['a', 'b', 'c'], 2)).to.be_equal_to({'a': {'b': {'c': 2}}})
    expect(assoc_in(d, ['a', 'b', 'd'], 8)).to.be_equal_to({'a': {'b': {'c': 1, 'd': 8}}})

@test('dissoc() should dissociate a key from a dict')
def _():
    d = {'a': 1, 'b': 2}
    expect(dissoc(d, 'a')).to.be_equal_to({'b': 2})

@test('dissoc_in() should dissociate a key from a nested dict')
def _():
    d = {'a': {'b': {'c': 1}}}
    expect(dissoc_in(d, ['a', 'b', 'c'])).to.be_equal_to({'a': {'b': {}}})
    expect(dissoc_in(d, ['a', 'b', 'd'])).to.be_equal_to({'a': {'b': {'c': 1}}})
    expect(dissoc_in(d, ['a'])).to.be_equal_to({})
