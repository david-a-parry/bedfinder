#!/usr/bin/env python3
import os
from nose.tools import *
try:
    from bedfinder.bedfinder  import *
except ImportError:
    from bedfinder  import *

dir_path = os.path.dirname(os.path.realpath(__file__))
test_data_path = os.path.join(dir_path, "test_data")

_regions_to_lines = { #keys are queries, values are expected search results
        '20:8388366-8388685': [["20", 8388365, 8388885, "L1MC3", "3105", "+"]],
        '21_gl000210_random:27468-27682': [["21_gl000210_random", 27468,
                                            27682, "HAL1-2a_MD", "370", "+"]],
        '22:51244457-51244541': [["22", 51244456, 51244541, "LTR60", "253",
                                  "+"]],
        '21:47870810-47874852':[["21", 47870810, 47871086, "ERVL-E-int", "842", 
                                 "+"],
                                ["21", 47871086, 47871373, "AluSc8", "2134",
                                 "+"],
                                ["21", 47871373, 47871534, "ERVL-E-int", "842", 
                                 "+"],
                                ["21", 47871667, 47873656, "ERV3-16A3_I-int",
                                 "6991", "-"],
                                ["21", 47873656, 47873948, "AluSx3", "2226",
                                 "-"],
                                ["21", 47873948, 47874690, "ERV3-16A3_I-int",
                                 "6991", "-"],
                                ["21", 47874690, 47874853, "FRAM", "900", "-"]
                               ]}


def test_exception_on_no_file():
    assert_raises(TypeError, BedFinder)


def test_not_enough_fields_error():
    assert_raises(BedFormatError,
                  BedFinder,
                  os.path.join(test_data_path, "not_enough_fields.bed"))


def test_search_by_region():
    bedfinder = BedFinder(os.path.join(test_data_path, "test_bed.gz"))
    for query, answer in _regions_to_lines.items():
        assert_equal(bedfinder.fetch_region(query), answer)


if __name__ == '__main__':
    import nose
    nose.run(defaultTest=__name__)
