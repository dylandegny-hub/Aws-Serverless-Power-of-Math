import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lambda"))
from lambda_function import lambda_handler


class TestPowerOfMathLambda(unittest.TestCase):
    def test_two_to_the_eighth(self):
        event = {"body": json.dumps({"base": "2", "exponent": "8"})}
        result = lambda_handler(event, None)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(json.loads(result["body"]), 256.0)

    def test_negative_exponent(self):
        event = {"body": json.dumps({"base": "2", "exponent": "-2"})}
        result = lambda_handler(event, None)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(json.loads(result["body"]), 0.25)

    def test_invalid_input_current_behavior(self):
        event = {"body": json.dumps({"base": "xyz", "exponent": "2"})}
        result = lambda_handler(event, None)
        self.assertEqual(result["statusCode"], 500)


if __name__ == "__main__":
    unittest.main()
