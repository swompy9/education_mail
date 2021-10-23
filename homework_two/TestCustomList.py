import unittest
from custom_list import CustomList

class TestCustomList(unittest.TestCase):
    def test_add(self):
        self.assertEqual(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), [6, 3, 10, 7])
        self.assertEqual(CustomList([1, 2]) + CustomList([9, 8, 7, 6, 5]), [10, 10, 7, 6, 5])
        self.assertEqual(CustomList([5, 1, 3, 7]) + [1, 2, 7], [6, 3, 10, 7])
        self.assertEqual(CustomList([1, 2]) + [9, 8, 7, 6, 5], [10, 10, 7, 6, 5])
        self.assertEqual([5, 1, 3, 7] + CustomList([1, 2, 7]), [6, 3, 10, 7])
        self.assertEqual([1, 2] + CustomList([9, 8, 7, 6, 5]), [10, 10, 7, 6, 5])

    def test_sub(self):
        self.assertEqual(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), [4, -1, -4, 7])
        self.assertEqual(CustomList([5, 1]) - CustomList([1, 2, 7]), [4, -1, 7])
        self.assertEqual(CustomList([5, 1, 3, 7]) - [1, 2, 7], [4, -1, -4, 7])
        self.assertEqual(CustomList([5, 1]) - [1, 2, 7], [4, -1, 7])
        self.assertEqual([5, 1, 3, 7] - CustomList([1, 2, 7]), [4, -1, -4, 7])
        self.assertEqual([5, 1] - CustomList([1, 2, 7, 9, 1, 2]), [4, -1, -7, -9, -1, -2])

    def test_gt(self):
        self.assertEqual(CustomList([5, 5, 5, 5]) > CustomList([1, 2, 7]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) > CustomList([14]), False)
        self.assertEqual(CustomList([20]) > CustomList([5, 5, 5, 4]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) > [1, 2, 7], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) > [14], False)
        self.assertEqual(CustomList([20]) > [5, 5, 5, 4], True)
        self.assertEqual([5, 5, 5, 5] > CustomList([1, 2, 7]), True)
        self.assertEqual([5, 5, 2, 1] > CustomList([14]), False)
        self.assertEqual([20] > CustomList([5, 5, 5, 4]), True)


    def test_ge(self):
        self.assertEqual(CustomList([5, 5, 5, 5]) >= CustomList([1, 2, 7, 9, 1]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) >= CustomList([13]), True)
        self.assertEqual(CustomList([20]) >= CustomList([5, 5, 5, 4, 1]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) >= [1, 2, 7, 9, 1], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) >= [13], True)
        self.assertEqual(CustomList([20]) >= [5, 5, 5, 4, 1], True)
        self.assertEqual([5, 5, 5, 5] >= CustomList([1, 2, 7, 9, 1]), True)
        self.assertEqual([5, 5, 2, 1] >= CustomList([13]), True)
        self.assertEqual([20] >= CustomList([5, 5, 5, 4, 1]), True)

    def test_lt(self):
        self.assertEqual(CustomList([5, 5, 5, 5]) < CustomList([1, 2, 7, 4, 6, 1]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) < CustomList([14]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) < CustomList([13]), False)
        self.assertEqual(CustomList([20]) < CustomList([5, 5, 5, 4, 2]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) < [1, 2, 7, 4, 6, 1], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) < [14], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) < [13], False)
        self.assertEqual(CustomList([20]) < [5, 5, 5, 4, 2], True)
        self.assertEqual([5, 5, 5, 5] < CustomList([1, 2, 7, 4, 6, 1]), True)
        self.assertEqual([5, 5, 2, 1] < CustomList([14]), True)
        self.assertEqual([5, 5, 2, 1] < CustomList([13]), False)
        self.assertEqual([20] < CustomList([5, 5, 5, 4, 2]), True)

    def test_le(self):
        self.assertEqual(CustomList([5, 5, 5, 5]) <= CustomList([1, 2, 7, 9, 1]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) <= CustomList([13]), True)
        self.assertEqual(CustomList([20]) <= CustomList([5, 5, 5, 4, 1]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) <= [1, 2, 7, 9, 1], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) <= [13], True)
        self.assertEqual(CustomList([20]) <= [5, 5, 5, 4, 1], True)
        self.assertEqual([5, 5, 5, 5] <= CustomList([1, 2, 7, 9, 1]), True)
        self.assertEqual([5, 5, 2, 1] <= CustomList([13]), True)
        self.assertEqual([20] <= CustomList([5, 5, 5, 4, 1]), True)

    def __eq__(self, other):
        self.assertEqual(CustomList([5, 5, 5, 5]) == CustomList([1, 9, 9, 1]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) == CustomList([10, 10]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) == CustomList([14]), False)
        self.assertEqual(CustomList([5, 5, 2, 1]) == CustomList([13]), True)
        self.assertEqual(CustomList([20]) == CustomList([5, 5, 5, 4, 1]), True)
        self.assertEqual(CustomList([5, 5, 5, 5]) == [1, 9, 9, 1], True)
        self.assertEqual(CustomList([5, 5, 5, 5]) == [10, 10], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) == [14], False)
        self.assertEqual(CustomList([5, 5, 2, 1]) == [13], True)
        self.assertEqual(CustomList([20]) == [5, 5, 5, 4, 1], True)
        self.assertEqual([5, 5, 5, 5] == CustomList([1, 9, 9, 1]), True)
        self.assertEqual([5, 5, 5, 5] == CustomList([10, 10]), True)
        self.assertEqual([5, 5, 2, 1] == CustomList([14]), False)
        self.assertEqual([5, 5, 2, 1] == CustomList([13]), True)
        self.assertEqual([20] == CustomList([5, 5, 5, 4, 1]), True)

    def __ne__(self, other):
        self.assertEqual(CustomList([5, 5, 5, 5]) != CustomList([1, 9, 9, 1]), False)
        self.assertEqual(CustomList([5, 5, 5, 5]) != CustomList([10, 10]), False)
        self.assertEqual(CustomList([5, 5, 2, 1]) != CustomList([14]), True)
        self.assertEqual(CustomList([5, 5, 2, 1]) != CustomList([13]), False)
        self.assertEqual(CustomList([20]) != CustomList([5, 5, 5, 4, 1]), False)
        self.assertEqual(CustomList([5, 5, 5, 5]) != [1, 9, 9, 1], False)
        self.assertEqual(CustomList([5, 5, 5, 5]) != [10, 10], False)
        self.assertEqual(CustomList([5, 5, 2, 1]) != [14], True)
        self.assertEqual(CustomList([5, 5, 2, 1]) != [13], False)
        self.assertEqual(CustomList([20]) != [5, 5, 5, 4, 1], False)
        self.assertEqual([5, 5, 5, 5] != CustomList([1, 9, 9, 1]), False)
        self.assertEqual([5, 5, 5, 5] != CustomList([10, 10]), False)
        self.assertEqual([5, 5, 2, 1] != CustomList([14]), True)
        self.assertEqual([5, 5, 2, 1] != CustomList([13]), False)
        self.assertEqual([20] != CustomList([5, 5, 5, 4, 1]), False)

if __name__ == '__main__':
    unittest.main()
