import unittest
from homework_2_list import CustomList


class TestCustomList(unittest.TestCase):
    """
    Class for testing my CustomList
    """

    def setUp(self):
        self.a = [1, 2, 6]                      # 9
        self.b = CustomList([3, 6, 1, 12])      # 22
        self.c = CustomList([8, 1, 5])          # 14
        self.d = [7, 1, 9, 2, 8]                # 27

    def test_add_and_radd(self):
        self.assertEqual(self.a + self.b, CustomList([4, 8, 7, 12]))
        self.assertEqual(self.b + self.a, CustomList([4, 8, 7, 12]))
        self.assertEqual(self.c + self.d, CustomList([15, 2, 14, 2, 8]))
        self.assertEqual(self.d + self.c, CustomList([15, 2, 14, 2, 8]))
        self.assertEqual(self.c + self.b, CustomList([11, 7, 6, 12]))
        self.assertEqual(self.b + self.c, CustomList([11, 7, 6, 12]))

        self.assertEqual((self.a + self.b).sum, sum(self.a) + self.b.sum)
        self.assertEqual((self.b + self.a).sum, sum(self.a) + self.b.sum)
        self.assertEqual((self.c + self.d).sum, sum(self.d) + self.c.sum)
        self.assertEqual((self.d + self.c).sum, sum(self.d) + self.c.sum)
        self.assertEqual((self.c + self.b).sum, self.b.sum + self.c.sum)
        self.assertEqual((self.b + self.c).sum, self.b.sum + self.c.sum)

        self.assertIsInstance(self.a + self.b, CustomList)
        self.assertIsInstance(self.b + self.a, CustomList)
        self.assertIsInstance(self.c + self.d, CustomList)
        self.assertIsInstance(self.d + self.c, CustomList)
        self.assertIsInstance(self.c + self.b, CustomList)
        self.assertIsInstance(self.b + self.c, CustomList)

    def test_sub_and_rsub(self):
        self.assertEqual(self.a - self.b, CustomList([-2, -4, 5, -12]))
        self.assertEqual(self.b - self.a, CustomList([2, 4, -5, 12]))
        self.assertEqual(self.c - self.d, CustomList([1, 0, -4, -2, -8]))
        self.assertEqual(self.d - self.c, CustomList([-1, 0, 4, 2, 8]))
        self.assertEqual(self.c - self.b, CustomList([5, -5, 4, -12]))
        self.assertEqual(self.b - self.c, CustomList([-5, 5, -4, 12]))

        self.assertEqual((self.a - self.b).sum, sum(self.a) - self.b.sum)
        self.assertEqual((self.b - self.a).sum, -sum(self.a) + self.b.sum)
        self.assertEqual((self.c - self.d).sum, -sum(self.d) + self.c.sum)
        self.assertEqual((self.d - self.c).sum, sum(self.d) - self.c.sum)
        self.assertEqual((self.c - self.b).sum, -self.b.sum + self.c.sum)
        self.assertEqual((self.b - self.c).sum, self.b.sum - self.c.sum)

        self.assertIsInstance(self.a - self.b, CustomList)
        self.assertIsInstance(self.b - self.a, CustomList)
        self.assertIsInstance(self.c - self.d, CustomList)
        self.assertIsInstance(self.d - self.c, CustomList)
        self.assertIsInstance(self.c - self.b, CustomList)
        self.assertIsInstance(self.b - self.c, CustomList)

    def test_le_lt_ge_gt_eq_ne(self):
        aa = CustomList(self.a)
        dd = CustomList(self.d)
        self.assertTrue(aa < self.b)
        self.assertTrue(aa < self.c)
        self.assertTrue(aa < dd)
        self.assertTrue(aa <= self.b)
        self.assertTrue(aa <= self.c)
        self.assertTrue(aa <= dd)
        self.assertTrue(aa <= aa)
        self.assertTrue(aa == aa)
        self.assertTrue(self.b >= self.b)
        self.assertTrue(self.b >= self.c)
        self.assertTrue(self.b >= aa)
        self.assertTrue(self.b > self.c)
        self.assertTrue(self.b > aa)
        self.assertTrue(self.b != self.c)
        self.assertFalse(aa > self.b)
        self.assertFalse(aa >= self.b)
        self.assertFalse(aa != aa)
        self.assertFalse(aa > aa)
        self.assertFalse(aa < aa)
        self.assertEqual(aa + self.b, self.a + self.b)
        self.assertEqual(aa + self.b, self.b + self.a)


if __name__ == '__main__':
    unittest.main()
