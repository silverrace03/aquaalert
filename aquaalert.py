"""AquaAlert - a beginner-friendly household water usage monitor."""

import csv
from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "water_readings.csv"
DATE_FORMAT = "%Y-%m-%d"


def load_readings(file_path=DATA_FILE):
    """Load meter readings from a CSV file and return them sorted by date."""
    file_path = Path(file_path)
    if not file_path.exists():
        return []

    readings = []
    with file_path.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            readings.append(
                {
                    "date": row["date"],
                    "meter_reading": float(row["meter_reading"]),
                }
            )

    return sorted(readings, key=lambda item: item["date"])


def save_readings(readings, file_path=DATA_FILE):
    """Save all readings to a CSV file."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "meter_reading"])
        writer.writeheader()
        writer.writerows(sorted(readings, key=lambda item: item["date"]))


def is_valid_date(date_text):
    """Return True when date_text uses YYYY-MM-DD and is a real date."""
    try:
        datetime.strptime(date_text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_new_reading(readings, date_text, meter_reading):
    """Check that a new cumulative meter reading is logically possible."""
    if not is_valid_date(date_text):
        return False, "Enter the date in YYYY-MM-DD format."

    if meter_reading < 0:
        return False, "The meter reading cannot be negative."

    if any(item["date"] == date_text for item in readings):
        return False, "A reading already exists for this date."

    earlier = [item for item in readings if item["date"] < date_text]
    later = [item for item in readings if item["date"] > date_text]

    if earlier and meter_reading < earlier[-1]["meter_reading"]:
        return False, "The reading cannot be lower than the previous reading."

    if later and meter_reading > later[0]["meter_reading"]:
        return False, "The reading cannot be higher than the next saved reading."

    return True, "Reading is valid."


def calculate_usage(readings):
    """Convert cumulative meter readings into daily consumption records."""
    sorted_readings = sorted(readings, key=lambda item: item["date"])
    usage_records = []

    for index in range(1, len(sorted_readings)):
        previous = sorted_readings[index - 1]
        current = sorted_readings[index]
        usage_records.append(
            {
                "date": current["date"],
                "usage": current["meter_reading"] - previous["meter_reading"],
            }
        )

    return usage_records


def calculate_summary(usage_records):
    """Return average, minimum, maximum, total and monthly estimate."""
    if not usage_records:
        return None

    values = [item["usage"] for item in usage_records]
    average = sum(values) / len(values)
    return {
        "total": sum(values),
        "average": average,
        "minimum": min(usage_records, key=lambda item: item["usage"]),
        "maximum": max(usage_records, key=lambda item: item["usage"]),
        "monthly_estimate": average * 30,
    }


def find_alerts(usage_records, daily_limit, leak_days=3):
    """Find high-usage days and a possible recent continuous leak."""
    high_usage = [
        item for item in usage_records if item["usage"] > daily_limit
    ]
    recent = usage_records[-leak_days:]
    possible_leak = (
        len(recent) == leak_days
        and all(item["usage"] > daily_limit for item in recent)
    )
    return high_usage, possible_leak


def add_reading(readings):
    """Ask the user for and save one meter reading."""
    date_text = input("Date (YYYY-MM-DD): ").strip()
    try:
        meter_reading = float(input("Cumulative meter reading in litres: "))
    except ValueError:
        print("Invalid reading. Enter a number.")
        return

    valid, message = validate_new_reading(readings, date_text, meter_reading)
    if not valid:
        print(message)
        return

    readings.append({"date": date_text, "meter_reading": meter_reading})
    readings.sort(key=lambda item: item["date"])
    save_readings(readings)
    print("Reading saved successfully.")


def display_records(readings):
    """Display meter readings and calculated usage."""
    if not readings:
        print("No readings have been recorded.")
        return

    usage_by_date = {
        item["date"]: item["usage"] for item in calculate_usage(readings)
    }
    print("\nDate         Meter reading (L)   Usage since previous reading (L)")
    print("-" * 65)
    for item in readings:
        usage = usage_by_date.get(item["date"])
        usage_text = "--" if usage is None else f"{usage:.2f}"
        print(f"{item['date']:<12} {item['meter_reading']:<19.2f} {usage_text}")


def display_summary(readings):
    """Display consumption statistics."""
    summary = calculate_summary(calculate_usage(readings))
    if summary is None:
        print("Add at least two readings to generate a summary.")
        return

    print("\nWATER USAGE SUMMARY")
    print(f"Total recorded usage : {summary['total']:.2f} L")
    print(f"Average usage        : {summary['average']:.2f} L")
    print(f"Estimated monthly use: {summary['monthly_estimate']:.2f} L")
    print(
        "Highest usage day   : "
        f"{summary['maximum']['date']} ({summary['maximum']['usage']:.2f} L)"
    )
    print(
        "Lowest usage day    : "
        f"{summary['minimum']['date']} ({summary['minimum']['usage']:.2f} L)"
    )


def display_alerts(readings):
    """Ask for a limit and display high-usage and possible-leak warnings."""
    usage_records = calculate_usage(readings)
    if not usage_records:
        print("Add at least two readings to check usage alerts.")
        return

    try:
        daily_limit = float(input("Enter your usage limit in litres: "))
        if daily_limit <= 0:
            raise ValueError
    except ValueError:
        print("Enter a number greater than zero.")
        return

    high_usage, possible_leak = find_alerts(usage_records, daily_limit)
    if high_usage:
        print("\nHigh-usage days:")
        for item in high_usage:
            print(f"- {item['date']}: {item['usage']:.2f} L")
    else:
        print("No usage exceeded the selected limit.")

    if possible_leak:
        print("WARNING: Usage exceeded the limit for the last 3 records.")
        print("This may indicate continuous excessive use or a possible leak.")


def print_menu():
    print("\n=== AQUAALERT ===")
    print("1. Add meter reading")
    print("2. View readings")
    print("3. View usage summary")
    print("4. Check high-usage and leak alerts")
    print("5. Exit")


def main():
    readings = load_readings()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_reading(readings)
        elif choice == "2":
            display_records(readings)
        elif choice == "3":
            display_summary(readings)
        elif choice == "4":
            display_alerts(readings)
        elif choice == "5":
            print("Thank you for using AquaAlert.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
