import unittest2

from my_sum import sum


class TestSum(unittest2.TestCase):
    def test_list_int(self):
        """"""
        Test_that_it_can_sum_a_list_of_integers
        """"""
        data = [4, 8, 12]
        result = sum(data)
        self.assertEqual(result, 24)

if _name_ == '__main__':
    unittest2.main()
