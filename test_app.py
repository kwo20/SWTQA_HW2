import unittest
from flask import Flask, render_template, request
from app import bmi_calc, weight_input, height_feet_input, height_inches_input
from unittest import mock


class TestBMICalculator(unittest.TestCase):
  def test_height_inches_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertFalse(height_inches_input('0') > 0 and height_inches_input('0') <= 12)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(height_inches_input('1') > 0 and height_inches_input('1') <= 12)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 6
        self.assertTrue(height_inches_input('6') > 0 and height_inches_input('6') <= 12)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 12
        self.assertTrue(height_inches_input('12') > 0 and height_inches_input('12') <= 12)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 13
        self.assertFalse(height_feet_input('13') > 0 and height_feet_input('13') <= 12)
        mock.builtins.input = original_input

  def test_height_feet_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertFalse(height_feet_input('0') > 0 and height_feet_input('0') <= 8)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(height_feet_input('1') > 0 and height_feet_input('1') <= 8)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 6
        self.assertTrue(height_feet_input('6') > 0 and height_feet_input('6') <= 8)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 8
        self.assertTrue(height_feet_input('8') > 0 and height_feet_input('8') <= 8)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 9
        self.assertFalse(height_feet_input('9') > 0 and height_feet_input('9') <= 8)
        mock.builtins.input = original_input

  def test_weight_input(self):
        original_input = mock.builtins.input
        #UNDER test (will return false)
        mock.builtins.input = lambda _: 0
        self.assertFalse(weight_input('0') > 0 and weight_input('0') <= 1000)
        mock.builtins.input = original_input
        #MIN test
        mock.builtins.input = lambda _: 1
        self.assertTrue(weight_input('1') > 0 and weight_input('1') <= 1000)
        mock.builtins.input = original_input
        #INTERIOR test
        mock.builtins.input = lambda _: 500
        self.assertTrue(weight_input('500') > 0 and weight_input('500') <= 1000)
        mock.builtins.input = original_input
        #MAX test
        mock.builtins.input = lambda _: 1000
        self.assertTrue(weight_input('1000') > 0 and weight_input('1000') <= 1000)
        mock.builtins.input = original_input
        #OVER test (will return false)
        mock.builtins.input = lambda _: 1001
        self.assertFalse(weight_input('1001') > 0 and weight_input('1001') <= 1000)
        mock.builtins.input = original_input
    
  def test_bmi_calc(self):
        #Underweight tests
        self.assertFalse(bmi_calc(6, 2, 120) == "underweight" and bmi_calc(6, 2, 140) == "underweight")
        #Normal tests
        self.assertFalse(bmi_calc(6, 2, 141) == "normal" and bmi_calc(6,2,150) == "normal" and bmi_calc(6, 2, 189) == "normal")
        #Overweight tests
        self.assertFalse(bmi_calc(6, 2, 190) == "overweight" and bmi_calc(6, 2, 200) == "overweight" and bmi_calc(6,2,227.5) == "overweight")
        #Obese tests
        self.assertFalse(bmi_calc(6, 2, 228) == "obese" and bmi_calc(6, 2, 240) == "obese")

    


if __name__ == "__main__":
    unittest.main()
