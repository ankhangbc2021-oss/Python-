"""
tests/test_matches.py

Unit tests cho hàm determine_winner trong utils/helpers.py
Sử dụng unittest, gồm 3 test case bắt buộc.
"""

import unittest
from utils.helpers import determine_winner


class TestDetermineWinner(unittest.TestCase):
    def test_team_a_wins(self):
        """Test: Đội A thắng (score_a > score_b)."""
        match = {
            "team_a": "T1",
            "team_b": "GenG",
            "score_a": 2,
            "score_b": 0,
            "status": "Completed",
        }
        self.assertEqual(determine_winner(match), "T1")

    def test_draw(self):
        """Test: Trận hòa (score_a == score_b)."""
        match = {
            "team_a": "JDG",
            "team_b": "BLG",
            "score_a": 1,
            "score_b": 1,
            "status": "Completed",
        }
        self.assertEqual(determine_winner(match), "Draw")

    def test_not_started(self):
        """Test: Trận chưa diễn ra (status == 'Pending')."""
        match = {
            "team_a": "G2",
            "team_b": "FNC",
            "score_a": 0,
            "score_b": 0,
            "status": "Pending",
        }
        self.assertEqual(determine_winner(match), "Not Started")


if __name__ == "__main__":
    unittest.main()
