"""
tests/test_roster.py

Unit tests cho hàm calculate_actual_pay trong utils/helpers.py
Sử dụng unittest, gồm 2 test case bắt buộc.
"""

import unittest
from utils.helpers import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):
    def test_active_player_gets_full_salary(self):
        player = {
            "player_id": "P10",
            "name": "TestActive",
            "role": "Top",
            "salary": 4000.0,
            "status": "Active",
        }
        self.assertEqual(calculate_actual_pay(player), 4000.0)

    def test_benched_player_gets_half_salary(self):
        player = {
            "player_id": "P11",
            "name": "TestBenched",
            "role": "Support",
            "salary": 3000.0,
            "status": "Benched",
        }
        self.assertEqual(calculate_actual_pay(player), 1500.0)


if __name__ == "__main__":
    unittest.main()
