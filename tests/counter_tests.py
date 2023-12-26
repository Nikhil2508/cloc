import sys
sys.path.append("..")
import unittest
import os
from app.PythonCounter import PythonCounter
from app.utils.constants import TEST_DATA
class TestStringMethods(unittest.TestCase):

    def test_file_counter(self):
        directory_path = TEST_DATA.get("python")
        obj = PythonCounter(directory_path).analyze_file()
        self.assertEqual(obj.blank_lines, 1)
        self.assertEqual(obj.comment_lines, 1)
        self.assertEqual(obj.code_lines, 4)


if __name__ == '__main__':
    unittest.main()