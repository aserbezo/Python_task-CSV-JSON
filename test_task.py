import unittest
import task
import os


class TestTask(unittest.TestCase):

    def test_convert_time_local(self):
        result = task.convert_time_local("2021-08-01T13:00:00+02:00")
        self.assertEqual(result, result)

    def test_tempereture_convert(self):
        result = task.convert_temperatures("33c")
        result1 = task.convert_temperatures("25c")
        self.assertEqual(result, "91F")
        self.assertEqual(result1, "77F")

    def test_file_exists(self):
        result = task.file_existence("sample.csv")
        self.assertEqual(result, result)



if __name__ == '__main__':
    unittest.main()
