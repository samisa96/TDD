import unittest
import Bmi


class BmiTest(unittest.TestCase):
    def test_bmicalc(self):
        # stub+assume+action+expect/assert
        self.assertEqual(Bmi.bmi_calc(45,1.6),17)
        self.assertEqual(Bmi.bmi_calc(80, 1.8), 25)
        self.assertEqual(Bmi.bmi_calc(70, 1.7), 24)
        self.assertEqual(Bmi.bmi_calc(-30, 1.8), 25)
        self.assertEqual(Bmi.bmi_calc(80, 0), 0)
    def test_bmitoweight(self):
        # stub+assume+action+expect/assert

        self.assertEqual(Bmi.bmi_toweight(45.0), "underweight")
        self.assertEqual(Bmi.bmi_toweight(80.0), "overweight")
        self.assertEqual(Bmi.bmi_toweight(0.0), None)
        self.assertNotEqual(Bmi.bmi_toweight(-30.0),"obese")
        self.assertEqual(Bmi.bmi_toweight((40.0)), "obese")

if __name__ == '__main__':
    unittest.main()
