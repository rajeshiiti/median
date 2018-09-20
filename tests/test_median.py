from unittest import TestCase

import nkrajesh

class TestMedian(TestCase):
    def test_is_float(self):
        f = nkrajesh.median([1,2,3,4,5,2,3,4])
        self.assertTrue(isinstance(f, float))

