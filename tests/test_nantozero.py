#!/usr/bin/env python

'''
`apply_if_or_else` tests for `opyttional` package.
'''

import math

from nanto import nantozero

value_battery_without_nan = [
    0,
    1,
    0.0,
    1.0,
    float('inf'),
    None,
    False,
    True,
    '',
    'None',
    'hello',
    [],
    [None],
    ['greetings'],
    [[]],
]

value_battery_with_nan = value_battery_without_nan + [float('nan')]


def test_with_value():
    for value in value_battery_without_nan:
        res = nantozero(
            value,
        )
        assert res == value


def test_with_nan():
    res = nantozero(
        float('nan'),
    )
    assert res == 0.0
