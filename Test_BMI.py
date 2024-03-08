import unittest
from BMI import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test case 1: Normal BMI
        self.assertAlmostEqual(calculate_bmi(150, 5, 6), 24.79, places=2)

        # Test case 2: Underweight BMI
        self.assertAlmostEqual(calculate_bmi(100, 5, 8), 15.57, places=2)

        # Test case 3: Overweight BMI
        self.assertAlmostEqual(calculate_bmi(210, 6, 0), 29.17, places=2)

        # Test case 4: Obese BMI
        self.assertAlmostEqual(calculate_bmi(250, 5, 9), 37.81, places=2)

    def test_get_bmi_category(self):
        # Test case 1: Normal BMI
        self.assertEqual(get_bmi_category(22), "Normal weight")

        # Test case 2: Underweight BMI
        self.assertEqual(get_bmi_category(16), "Underweight")

        # Test case 3: Overweight BMI
        self.assertEqual(get_bmi_category(27), "Overweight")

        # Test case 4: Obese BMI
        self.assertEqual(get_bmi_category(35), "Obese")

if __name__ == "__main__":
    unittest.main()
