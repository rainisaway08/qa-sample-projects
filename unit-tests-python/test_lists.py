import unittest

class TestLists(unittest.TestCase):
    def test_append(self):
        lst = [1, 2]
        lst.append(3)
        self.assertEqual(lst, [1, 2, 3])

    def test_len(self):
        self.assertEqual(len([1, 2, 3]), 3)

if __name__ == "__main__":
    unittest.main()
