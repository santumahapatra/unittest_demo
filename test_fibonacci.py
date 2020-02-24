import unittest
import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_api_interface(self):
        # self.assertRaises(fibonacci.calculate(), 'TypeError')
        self.assertEqual(fibonacci.calculate(0), 0)

    def test_boundary_logic(self):
        self.assertEqual(fibonacci.calculate(0), 0)
        self.assertEqual(fibonacci.calculate(1), 1)

    def test_logic(self):
        self.assertEqual(fibonacci.calculate(2), 1)
        self.assertEqual(fibonacci.calculate(3), 2)
        self.assertEqual(fibonacci.calculate(4), 3)
        self.assertEqual(fibonacci.calculate(5), 5)
        self.assertEqual(fibonacci.calculate(10), 55)

    def test_incorrect_input(self):
        self.assertEqual(fibonacci.calculate(-1), "WRONG INPUT")
        self.assertEqual(fibonacci.calculate(4.4), "WRONG INPUT")
        self.assertEqual(fibonacci.calculate("a small banana"), "WRONG INPUT")
        self.assertEqual(fibonacci.calculate(False), "WRONG INPUT")
        self.assertEqual(fibonacci.calculate(None), "WRONG INPUT")
        
    
if __name__ == '__main__':
    unittest.main(verbosity=2)