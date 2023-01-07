import pytest

from integers.exceptions import WrongNumber
from integers.utils import read_file, get_values, make_pairs, write_to_file


def test_read_file():
    with pytest.raises(Exception) as e:
        read_file("nonexistent_file.txt")
    assert e.type == FileNotFoundError


def test_get_values_not_number_value(not_number_value):
    with pytest.raises(Exception) as e:
        get_values(not_number_value)
    assert e.type == ValueError


@pytest.fixture
def too_big_number():
    return '8;3;13;4'


def test_get_values_too_big_number(too_big_number):
    with pytest.raises(Exception) as e:
        get_values(too_big_number)
    assert e.type == WrongNumber


@pytest.fixture
def not_number_value():
    return '5;6;3s;12'


def test_get_values_not_number_value(not_number_value):
    with pytest.raises(Exception) as e:
        get_values(not_number_value)
    assert e.type == ValueError


@pytest.fixture
def not_natural_number():
    return '8;3;-1;4'


def test_get_values_not_natural_number(not_natural_number):
    with pytest.raises(Exception) as e:
        get_values(not_natural_number)
    assert e.type == WrongNumber


@pytest.fixture
def good_values():
    return '4;8;9;0;12;1;4;2;12;12;4;4;8;11;12;0'


def test_get_values_good_values(good_values):
    values = get_values(good_values)

    assert values == [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]


@pytest.fixture
def input_values():
    return [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]


def test_make_pairs(input_values):
    pairs = make_pairs(input_values)

    assert pairs == [[4, 8], [0, 12], [1, 11], [4, 8], [0, 12]]


def test_make_pairs_equal_12(input_values):
    pairs = make_pairs(input_values)

    for i in range(len(pairs)):
        assert int(pairs[i][0]) + int(pairs[i][1]) == 12


def test_make_pairs_first_not_larger(input_values):
    pairs = make_pairs(input_values)

    for i in range(len(pairs)):
        assert int(pairs[i][0]) <= int(pairs[i][1])


@pytest.fixture
def input_pairs():
    return [[4, 8], [0, 12], [1, 11], [4, 8], [0, 12]]


@pytest.fixture
def output_file_name():
    return '../output.txt'


def test_write_to_file(output_file_name, input_pairs):
    write_to_file(output_file_name, input_pairs)
    file = open(output_file_name, "r")
    assert file.read() == "[4, 8]\n[0, 12]\n[1, 11]\n[4, 8]\n[0, 12]\n"
