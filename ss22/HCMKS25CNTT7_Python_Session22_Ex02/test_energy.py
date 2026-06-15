import unittest
from energy_monitor import calculate_energy_financials


class TestEnergyFinancials(unittest.TestCase):
    def test_discount_applied(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 60000,
                "status": "Normal",
            }
        ]
        total, discount, cost = calculate_energy_financials(devices)
        self.assertEqual(discount, 3)
        self.assertEqual(total, 60000)

    def test_no_discount(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 40000,
                "status": "Normal",
            }
        ]
        total, discount, cost = calculate_energy_financials(devices)
        self.assertEqual(discount, 0)
        self.assertEqual(total, 40000)

    def test_multiple_devices(self):
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 30000,
                "status": "Normal",
            },
            {
                "id": "M02",
                "location": "B",
                "old_index": 0,
                "new_index": 25000,
                "status": "Normal",
            },
        ]
        total, discount, cost = calculate_energy_financials(devices)
        self.assertEqual(total, 55000)
        self.assertEqual(discount, 3)


if __name__ == "__main__":
    unittest.main()
