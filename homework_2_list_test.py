import unittest
from homework_2_list import CustomList


a = [1, 2, 6]                   # 9
b = CustomList([3, 6, 1, 12])   # 22
c = CustomList([8, 1, 5])       # 14
d = [7, 1, 9, 2, 8]             # 27


class TestCustomList(unittest.TestCase):
    """
    Class for testing my CustomList
    """
    def test_add_and_radd(self):
        self.assertEqual(a + b, CustomList([4, 8, 7, 12]))
        self.assertEqual(b + a, CustomList([4, 8, 7, 12]))
        self.assertEqual(c + d, CustomList([15, 2, 14, 2, 8]))
        self.assertEqual(d + c, CustomList([15, 2, 14, 2, 8]))
        self.assertEqual(c + b, CustomList([11, 7, 6, 12]))
        self.assertEqual(b + c, CustomList([11, 7, 6, 12]))

        self.assertEqual((a + b).sum, sum(a) + b.sum)
        self.assertEqual((b + a).sum, sum(a) + b.sum)
        self.assertEqual((c + d).sum, sum(d) + c.sum)
        self.assertEqual((d + c).sum, sum(d) + c.sum)
        self.assertEqual((c + b).sum, b.sum + c.sum)
        self.assertEqual((b + c).sum, b.sum + c.sum)

        self.assertIsInstance(a + b, CustomList)
        self.assertIsInstance(b + a, CustomList)
        self.assertIsInstance(c + d, CustomList)
        self.assertIsInstance(d + c, CustomList)
        self.assertIsInstance(c + b, CustomList)
        self.assertIsInstance(b + c, CustomList)

    def test_sub_and_rsub(self):
        self.assertEqual(a - b, CustomList([-2, -4, 5, -12]))
        self.assertEqual(b - a, CustomList([2, 4, -5, 12]))
        self.assertEqual(c - d, CustomList([1, 0, -4, -2, -8]))
        self.assertEqual(d - c, CustomList([-1, 0, 4, 2, 8]))
        self.assertEqual(c - b, CustomList([5, -5, 4, -12]))
        self.assertEqual(b - c, CustomList([-5, 5, -4, 12]))

        self.assertEqual((a - b).sum, sum(a) - b.sum)
        self.assertEqual((b - a).sum, -sum(a) + b.sum)
        self.assertEqual((c - d).sum, -sum(d) + c.sum)
        self.assertEqual((d - c).sum, sum(d) - c.sum)
        self.assertEqual((c - b).sum, -b.sum + c.sum)
        self.assertEqual((b - c).sum, b.sum - c.sum)

        self.assertIsInstance(a - b, CustomList)
        self.assertIsInstance(b - a, CustomList)
        self.assertIsInstance(c - d, CustomList)
        self.assertIsInstance(d - c, CustomList)
        self.assertIsInstance(c - b, CustomList)
        self.assertIsInstance(b - c, CustomList)

    def test_le_lt_ge_gt_eq_ne(self):
        aa = CustomList(a)
        dd = CustomList(d)
        self.assertTrue(aa < b)
        self.assertTrue(aa < c)
        self.assertTrue(aa < dd)
        self.assertTrue(aa <= b)
        self.assertTrue(aa <= c)
        self.assertTrue(aa <= dd)
        self.assertTrue(aa <= aa)
        self.assertTrue(aa == aa)
        self.assertTrue(b >= b)
        self.assertTrue(b >= c)
        self.assertTrue(b >= aa)
        self.assertTrue(b > c)
        self.assertTrue(b > aa)
        self.assertTrue(b != c)
        self.assertFalse(aa > b)
        self.assertFalse(aa >= b)
        self.assertFalse(aa != aa)
        self.assertFalse(aa > aa)
        self.assertFalse(aa < aa)
        self.assertEqual(aa + b, a + b)
        self.assertEqual(aa + b, b + a)


if __name__ == '__main__':
    unittest.main()
