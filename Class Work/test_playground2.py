import unittest
import playground2


#gamp@gamp-Latitude-7480:~/Desktop/python exercises/Class Work$ python3 -m unittest test_playground2.py


class TestCubeFunction(unittest.TestCase):
    
    def test_that_cube_function_exists(self):
        playground2.cube(3)

    def test_that_cube_function_returns_correct_result(self):
        actual = playground2.cube(3)
        expected = 27
        self.assertEqual(actual, expected)

        actual = playground2.cube(3)
        expected = 27
        self.assertEqual(actual, expected)

    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
        actual = playground2.cube("musa")
        expected = "invalid input"
        self.assertEqual(actual, expected)
