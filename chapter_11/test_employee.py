import unittest
from employee import Employee as e

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.emp = e('Foo','Bar',50000)
    
    def test_increase_salary_default(self):
        self.assertEqual(50000,self.emp.get_salary())
        self.emp.give_raise()
        self.assertEqual(55000,self.emp.get_salary())
    
    def test_increase_salary_custom(self):
        self.assertEqual(50000,self.emp.get_salary())
        self.emp.give_raise(10000)
        self.assertEqual(60000,self.emp.get_salary())

unittest.main()