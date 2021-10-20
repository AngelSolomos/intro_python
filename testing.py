import unittest


def addition(a, b):
    return a + b


class TestMethods(unittest.TestCase):
    def test_1_2(self):
        self.assertEqual(addition(1, 2), 3)

    def test_2_3(self):
        self.assertEqual(addition(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
