# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import unittest
from homework_2_metaclass import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50
    _x = 123
    __x = 51
    x_ = 125
    _x_ = 561
    __x_ = 61234
    x__ = 15
    _x__ = 0
    __x__ = 123

    def __init__(self, val=99):
        self.val = val
        self.__val = 9
        self._val = 10
        self._val_ = 11
        self._val__ = 12
        self.__val__ = 1
        self.__val_ = 15
        self.val_ = 0
        self.val__ = -31

    def line(self):
        pass

    def _line_(self):
        pass

    def __line(self):
        pass

    def __line_(self):
        pass

    def __line__(self):
        pass


class TestCustomMeta(unittest.TestCase):
    def test_class_attr(self):
        cls = CustomClass
        for i in cls.__dict__:
            if not (i[:2] == '__' and i[-2:] == '__'):
                self.assertTrue(i[:7] == 'custom_')

    def test_instance_attr(self):
        inst = CustomClass()
        for i in inst.__dict__:
            self.assertTrue(i[:7] == 'custom_')


if __name__ == '__main__':
    unittest.main()
