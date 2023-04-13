import unittest
from app import bmi_calc, weight_input, height_feet_input, height_inches_input
from unittest import mock


class TestBMICalculator(unittest.TestCase):
  def test_height_inches_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertTrue(height_inches_input() > 0 and height_inches_input() <= 12)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(height_inches_input() > 0 and height_inches_input() <= 12)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 6
        self.assertTrue(height_inches_input() > 0 and height_inches_input() <= 12)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 12
        self.assertTrue(height_inches_input() > 0 and height_inches_input() <= 12)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 13
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 12)
        mock.builtins.input = original_input

  def test_height_feet_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 8)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 8)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 6
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 8)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 8
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 8)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 9
        self.assertTrue(height_feet_input() > 0 and height_feet_input() <= 8)
        mock.builtins.input = original_input

  def test_weight_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertTrue(weight_input() > 0 and weight_input() <= 1000)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(weight_input() > 0 and weight_input() <= 1000)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 500
        self.assertTrue(weight_input() > 0 and weight_input() <= 1000)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 1000
        self.assertTrue(weight_input() > 0 and weight_input() <= 1000)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 1001
        self.assertTrue(weight_input() > 0 and weight_input() <= 1000)
        mock.builtins.input = original_input
    
  def test_bmi_calc(self):
        #Underweight tests
        self.assertTrue(bmi_calc(6, 2, 120) == "Underweight" and bmi_calc(6,2,140) == "Underweight")
        #Normal tests
        self.assertTrue(bmi_calc(6, 2, 141) == "Normal" and bmi_calc(6,2,150) == "Normal" and bmi_calc(6, 2, 189) == "Normal")
        #Overweight tests
        self.assertTrue(bmi_calc(6, 2, 190) == "Overweight" and bmi_calc(6, 2, 200) == "Overweight" and bmi_calc(6,2,227.5) == "Overweight")
        #Obese tests
        self.assertTrue(bmi_calc(6, 2, 228) == "Obese" and bmi_calc(6, 2, 240) == "Obese")

    


if __name__ == "__main__":
    unittest.main()