"""Tests for AquaAlert's calculation and validation functions."""

import tempfile
import unittest
from pathlib import Path

from aquaalert import (
    calculate_summary,
    calculate_usage,
    find_alerts,
    is_valid_date,
    load_readings,
    save_readings,
    validate_new_reading,
)


class AquaAlertTests(unittest.TestCase):
    def setUp(self):
        self.readings = [
            {"date": "2026-09-20", "meter_reading": 1000.0},
            {"date": "2026-09-21", "meter_reading": 1250.0},
            {"date": "2026-09-22", "meter_reading": 1570.0},
            {"date": "2026-09-23", "meter_reading": 1900.0},
        ]

    def test_usage_is_difference_between_readings(self):
        usage = calculate_usage(self.readings)
        self.assertEqual([item["usage"] for item in usage], [250.0, 320.0, 330.0])

    def test_summary(self):
        summary = calculate_summary(calculate_usage(self.readings))
        self.assertAlmostEqual(summary["total"], 900.0)
        self.assertAlmostEqual(summary["average"], 300.0)
        self.assertAlmostEqual(summary["monthly_estimate"], 9000.0)

    def test_summary_requires_usage_records(self):
        self.assertIsNone(calculate_summary([]))

    def test_date_validation(self):
        self.assertTrue(is_valid_date("2026-09-24"))
        self.assertFalse(is_valid_date("2026-02-30"))
        self.assertFalse(is_valid_date("24-09-2026"))

    def test_alerts_and_possible_leak(self):
        high_usage, possible_leak = find_alerts(
            calculate_usage(self.readings), daily_limit=200
        )
        self.assertEqual(len(high_usage), 3)
        self.assertTrue(possible_leak)

    def test_rejects_duplicate_date_and_decreasing_meter(self):
        valid, _ = validate_new_reading(self.readings, "2026-09-21", 1300)
        self.assertFalse(valid)
        valid, _ = validate_new_reading(self.readings, "2026-09-24", 1800)
        self.assertFalse(valid)

    def test_rejects_negative_meter_reading(self):
        valid, _ = validate_new_reading([], "2026-09-24", -1)
        self.assertFalse(valid)

    def test_csv_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "readings.csv"
            save_readings(self.readings, file_path)
            self.assertEqual(load_readings(file_path), self.readings)


if __name__ == "__main__":
    unittest.main()
