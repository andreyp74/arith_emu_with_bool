import unittest
from sum_emu import *

class SumEmuTest(unittest.TestCase):

    def test_num_as_binary_list(self):
        self.assertEqual(num_as_binary_list(0), [0])
        self.assertEqual(num_as_binary_list(1), [1])
        self.assertEqual(num_as_binary_list(2), list(reversed([1, 0])))
        self.assertEqual(num_as_binary_list(3), list(reversed([1, 1])))
        self.assertEqual(num_as_binary_list(4), list(reversed([1, 0, 0])))
        self.assertEqual(num_as_binary_list(5), list(reversed([1, 0, 1])))
        self.assertEqual(num_as_binary_list(6), list(reversed([1, 1, 0])))
        self.assertEqual(num_as_binary_list(7), list(reversed([1, 1, 1])))
        self.assertEqual(num_as_binary_list(8), list(reversed([1, 0, 0, 0])))
        self.assertEqual(num_as_binary_list(16), list(reversed([1, 0, 0, 0, 0])))
        self.assertEqual(num_as_binary_list(42), list(reversed([1, 0, 1, 0, 1, 0])))
        self.assertEqual(num_as_binary_list(0xff), list(reversed([1, 1, 1, 1, 1, 1, 1, 1])))
        
    def test_binary_list_as_num(self):
        self.assertEqual(binary_list_as_num([0]), 0)
        self.assertEqual(binary_list_as_num([1]), 1)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0]))), 2)
        self.assertEqual(binary_list_as_num(list(reversed([1, 1]))), 3)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0, 0]))), 4)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0, 1]))), 5)
        self.assertEqual(binary_list_as_num(list(reversed([1, 1, 0]))), 6)
        self.assertEqual(binary_list_as_num(list(reversed([1, 1, 1]))), 7)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0, 0, 0]))), 8)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0, 0, 0, 0]))), 16)
        self.assertEqual(binary_list_as_num(list(reversed([1, 0, 1, 0, 1, 0]))), 42)
        self.assertEqual(binary_list_as_num(list(reversed([1, 1, 1, 1, 1, 1, 1, 1]))), 0xff)
        
    def test_xor_op(self):
        self.assertEqual(xor_op(0, 0), 0)
        self.assertEqual(xor_op(1, 0), 1)
        self.assertEqual(xor_op(0, 1), 1)
        self.assertEqual(xor_op(1, 1), 0)
        self.assertEqual(xor_op(False, False), 0)
        self.assertEqual(xor_op(True, False), 1)
        self.assertEqual(xor_op(False, True), 1)
        self.assertEqual(xor_op(True, True), 0)
        
    def test_and_op(self):
        self.assertEqual(and_op(0, 0), 0)
        self.assertEqual(and_op(1, 0), 0)
        self.assertEqual(and_op(0, 1), 0)
        self.assertEqual(and_op(1, 1), 1)
        self.assertEqual(and_op(False, False), 0)
        self.assertEqual(and_op(True, False), 0)
        self.assertEqual(and_op(False, True), 0)
        self.assertEqual(and_op(True, True), 1)
        
    def test_sum(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 1), 1)
        self.assertEqual(sum(1, 1), 2)
        self.assertEqual(sum(2, 1), 3)
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(2, 2), 4)
        self.assertEqual(sum(3, 2), 5)
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(3, 3), 6)
        self.assertEqual(sum(3, 4), 7)
        self.assertEqual(sum(4, 3), 7)
        self.assertEqual(sum(4, 4), 8)
        self.assertEqual(sum(4, 5), 9)
        self.assertEqual(sum(5, 4), 9)
        self.assertEqual(sum(5, 5), 10)
        self.assertEqual(sum(42, 10), 52)
        self.assertEqual(sum(42, 42), 84)
        self.assertEqual(sum(88, 22), 110)
        self.assertEqual(sum(1024, 256), 1280)
        
if __name__ == '__main__':
    unittest.main()