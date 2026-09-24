# AquaAlert – Household Water Usage Monitor

AquaAlert is a command-line Python application that records cumulative household
water-meter readings, calculates consumption between readings, summarizes usage,
and warns the user about unusually high consumption or a possible continuing
leak.

The project is designed for an **Introduction to Problem Solving using Python**
course and uses only Python's standard library.

## Problem statement

Households often discover excessive water use only after receiving a high bill.
Manual meter readings are also difficult to compare over time. A simple tool is
needed to store readings, calculate consumption, highlight unusual usage, and
provide an early indication of a possible leak.

> AquaAlert provides an educational warning based on consumption patterns. It
> does not prove that a plumbing leak exists.

## Objectives

1. Record cumulative water-meter readings with dates.
2. Calculate water consumed between consecutive readings.
3. Summarize total, average, minimum, maximum, and estimated monthly usage.
4. Compare consumption against a limit selected by the user.
5. Warn when the latest three usage records all exceed that limit.
6. Preserve readings in a human-readable CSV file.
7. Demonstrate variables, conditions, loops, collections, functions, file
   handling, validation, and testing in Python.

## Features

- Menu-driven terminal interface
- CSV data storage
- Date and numeric input validation
- Duplicate-date prevention
- Cumulative meter consistency checks
- Usage summary and monthly estimate
- Configurable high-usage threshold
- Possible-leak warning
- Automated unit tests

## Requirements

- Python 3.9 or newer
- A terminal or command prompt
- No external Python packages

## Setup and execution

These instructions assume that the evaluator has no prior project context.

### 1. Clone the public repository

```bash
git clone https://github.com/silverrace03/aquaalert.git
cd aquaalert
```



### 2. Create a virtual environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

The project currently uses only the Python standard library, so this command
does not download third-party packages.

### 4. Configuration

No configuration file or API key is required. The high-usage limit is entered
at runtime when menu option 4 is selected.

The program stores readings in:

```text
data/water_readings.csv
```

This file is created automatically after the first reading is saved.

### 5. Run AquaAlert

```bash
python3 aquaalert.py
```

On Windows, `py aquaalert.py` can be used instead.

### 6. Run the automated tests

```bash
python3 -m unittest -v
```

## How to use the program

1. Select **Add meter reading**.
2. Enter the date in `YYYY-MM-DD` format.
3. Enter the cumulative value shown on the water meter in litres.
4. Add another reading on a later date.
5. Select **View readings** to see consumption between readings.
6. Select **View usage summary** for usage statistics.
7. Select **Check high-usage and leak alerts**, then enter a suitable limit.

For meaningful daily comparisons, record the meter at approximately the same
time each day.

## Main calculations

```text
Usage = Current cumulative reading - Previous cumulative reading
Average usage = Total calculated usage / Number of usage records
Monthly estimate = Average usage × 30
```

A possible-leak warning is displayed when each of the latest three calculated
usage records is greater than the limit entered by the user.

## Repository structure

```text
aquaalert/
├── aquaalert.py             # Application and calculation functions
├── test_aquaalert.py        # Automated unit tests
├── requirements.txt         # Dependency declaration
├── README.md                # Setup and usage instructions
├── data/                    # CSV file is created here at runtime
└── docs/
    ├── DESIGN.md            # Requirements, diagrams, and evaluation method
    ├── EVALUATION_RECORD.md # Verified test scenario and results
    ├── PROJECT_REPORT.md     # Structured report draft
    └── SUBMISSION_CHECKLIST.md
```

## Design documentation

The complete design artefacts are available in [docs/DESIGN.md](docs/DESIGN.md):

- Problem statement and objectives
- Functional and non-functional requirements
- System architecture diagram
- Process workflow diagram
- Use case diagram
- Component diagram
- Evaluation methodology

## Testing status

The test suite checks:

- Consumption calculation
- Summary calculation
- High-usage and possible-leak detection
- Duplicate and decreasing reading rejection
- CSV save/load consistency

## Limitations

- Readings are entered manually.
- Usage represents the interval between two readings; it is daily only when
  readings are entered once per day.
- The threshold is supplied by the user and is not a professional leak test.
- The program currently supports one household data file.

## Future improvements

- Edit or delete an incorrect reading
- Separate profiles for multiple households
- Weekly and monthly text reports
- Automatic sensor integration
- Graphical charts as an optional extension

## Repository submission

The final repository must be public. Submit only its root URL:

```text
https://github.com/silverrace03/aquaalert
```

Do not submit a URL containing `/tree/`, `/blob/`, or a file name.

## Author

**Name:** Prakhar Kumar Singh  
**Registration number:** 22MIP10083
**Course:** Introduction to Problem Solving using Python
