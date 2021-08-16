import unittest
import utest
class TestMain(unittest.TestCase):
    def setUp(self):
        print('Testing function')
    def test_do_stuff(self):
        test_param=10
        result=utest.do_stuff(test_param)
        self.assertEqual(result,15)
    def test_do_stuff2(self):
        test_param='asdhfguad'
        result=utest.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
    def test_do_stuff3(self):
        test_param=None
        result=utest.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')
    def test_do_stuff4(self):
        test_param=''
        result=utest.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')
    def tearDown(self):
        print('Test completed')
if __name__ == '__main__':
    unittest.main()