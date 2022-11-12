
import pytest
import random


def test_case():

    if random.randint(0, 1):
        assert 1
    else:
        assert 0