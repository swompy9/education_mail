import unittest
from metaclass_underscore import CustomMeta

class Class_for_test(metaclass=CustomMeta):
    x = 50
    y = 150
    def __init__(self, val=99, stroka='test_stroka'):
        self.val = val
        self.stroka = stroka
    def set_hello(self):
        self.hello = 'Hello'
        return 'its okay'
    def line(self):
        return 100

class TestCustomList(unittest.TestCase):
    def test_success_access(self):
        tested_class = Class_for_test()
        tested_class.point = (10, 20)
        dynamic_tested_class = CustomMeta('New_class_for_test', (), {'tupl': (10, 20, 30), 'func': lambda lst: lst})
        self.assertEqual(tested_class.custom_x, 50)
        self.assertEqual(tested_class.custom_y, 150)
        self.assertEqual(tested_class.custom_val, 99)
        self.assertEqual(tested_class.custom_stroka, 'test_stroka')
        self.assertEqual(tested_class.custom_set_hello(), 'its okay')
        self.assertEqual(tested_class.custom_hello, 'Hello')
        self.assertEqual(tested_class.custom_line(), 100)
        self.assertEqual(tested_class.custom_x, 50)
        self.assertEqual(tested_class.custom_y, 150)
        self.assertEqual(tested_class.custom_val, 99)
        self.assertEqual(tested_class.custom_point, (10, 20))
        self.assertEqual(dynamic_tested_class.custom_tupl, (10, 20, 30))
        self.assertEqual(dynamic_tested_class.custom_func([0, 1, 2, 3, 'lambda']), [0, 1, 2, 3, 'lambda'])
    def test_failed_access(self):
        tested_class = Class_for_test()
        tested_class.point = (10, 20)
        dynamic_tested_class = CustomMeta('New_class_for_test', (), {'tupl': (10, 20, 30), 'func': lambda lst: lst})
        with self.assertRaises(AttributeError):
            tested_class.x
            tested_class.y
            tested_class.val
            tested_class.stroka
            tested_class.set_hello()
            tested_class.hello
            tested_class.line()
            tested_class.x
            tested_class.y
            tested_class.val
            tested_class.point
            dynamic_tested_class.tupl
            dynamic_tested_class.func([0, 1, 2, 3, 'lambda'])

if __name__ == '__main__':
    unittest.main()
