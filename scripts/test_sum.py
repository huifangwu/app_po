import os, yaml
import pytest

from Base.get_data import GetData


def sum_data():
    sum_list = list()
    data = GetData.get_yame_data('sum.yml')
    for i in data.values():
        sum_list.append((i.get('a'), i.get('b'), i.get('c')))
        # [(1, 2, 3), (3, 4, 5), (4, 5, 9)]
    return sum_list


class TestSum:

    @pytest.mark.parametrize('a, b, c', sum_data())
    def test_sum(self, a, b, c):
        print('\n{} + {} = {}'.format(a, b, c))
        assert a + b == c
