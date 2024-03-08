import unittest
from BMI import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        # Test case 1: Normal BMI
        self.assertAlmostEqual(calculate_bmi(150, 5, 6), 24.22, places=2)

        # Test case 2: Underweight BMI
        self.assertAlmostEqual(calculate_bmi(100, 5, 8), 15.24, places=2)

        # Test case 3: Overweight BMI
        self.assertAlmostEqual(calculate_bmi(180, 6, 0), 24.49, places=2)

        # Test case 4: Obese BMI
        self.assertAlmostEqual(calculate_bmi(220, 5, 9), 32.55, places=2)

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
