import unittest1


class TestSum(unittest1.TestCase):

    def test_sum(self):
        self.assertEqual(sum([5, 10, 15]), 30, "Should be 30")

    def test_sum_tuple(self):
        self.assertEqual(sum((5, 10, 15)), 30, "Should be 30")

if __name__ == '__main__':
    unittest1.main()