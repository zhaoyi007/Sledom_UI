import unittest

import ddt


def demo(x, y):
    if x == y:
        print("成功")
    else:
        print("失败")


class de(unittest.TestCase):

    def test_1(self):
        a = 1
        b = 1

        if self.assertEqual(a, b, msg="测试") is None:
            demo(a, b)


if __name__ == "__main__":
    unittest.main()
