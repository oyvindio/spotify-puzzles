# -*- coding: utf-8 -*-
import binary_reverse


def test_as_number():
    assert binary_reverse.as_number('3') == 3

def test_as_number_with_whitespace():
    assert binary_reverse.as_number('   3     ') == 3

def test_binary_reverse():
    assert binary_reverse.binary_reverse(47) == 61
    assert binary_reverse.binary_reverse(13) == 11
