import unittest
import  BubbleSort
class test(unittest.TestCase):
    def test_bublesort(self):
        self.assertIsNotNone(BubbleSort.bubblesort([17,22,25,30,45]))
        self.assertEqual(BubbleSort.bubblesort([17,22,25,30,45]),[17,22,25,30,45])
        self.assertEqual(len(BubbleSort.bubblesort([17,22,25,30,45])),5)


if __name__ == '__main__':
    unittest.main()
