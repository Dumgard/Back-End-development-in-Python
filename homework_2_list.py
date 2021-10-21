# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring


class CustomList(list):
    def __init__(self, data=None):
        super().__init__(data)
        self.sum = sum(self)

    def __add__(self, other):
        smallest, biggest = self, other
        if len(smallest) > len(biggest):
            smallest, biggest = biggest, smallest
        ans = CustomList(biggest.copy())
        for i, val in enumerate(smallest):
            ans[i] += val
        ans.sum = sum(ans)
        return ans

    def __sub__(self, other):
        left, right = CustomList(self), other
        if len(left) < len(right):
            for i in range(len(right) - len(left)):
                left.append(0)
        for i, val in enumerate(right):
            left[i] -= val
            left.sum -= val
        return left

    def __rsub__(self, other):
        return CustomList([-i for i in self - other])

    def __le__(self, other):
        return self.sum <= other.sum

    def __ge__(self, other):
        return self.sum >= other.sum

    def __eq__(self, other):
        return self.sum == other.sum

    def __lt__(self, other):
        return self.sum < other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __ne__(self, other):
        return self.sum != other.sum

    __radd__ = __add__
