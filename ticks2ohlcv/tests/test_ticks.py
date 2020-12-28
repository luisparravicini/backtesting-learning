import ticks
import pytest
import io
from pathlib import Path


def build_path(dir, fname):
    return Path(__file__).parent.joinpath(dir, fname + '.csv')

def data_path(fname):
    return build_path('data', fname)

def data_expected_path(fname):
    return build_path('expected', fname)

def assert_result(data_fname, result):
    with open(data_expected_path(data_fname), 'r') as file:
        expected = file.read()

    output = result.to_csv(index=False, float_format='%.4f')
    assert expected.split("\n") == output.split("\n")

def assert_conversion(data_fname):
    result = ticks.to_ohlcv(data_path(data_fname))    
    assert_result(data_fname, result)

def test_1m_reset_seconds():
    assert_conversion('data_001')

def test_min():
    assert_conversion('data_002')

def test_rows_in_an_interval_are_collapsed():
    assert_conversion('data_003')
