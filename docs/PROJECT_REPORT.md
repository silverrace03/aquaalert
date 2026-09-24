# Project Report: AquaAlert – Household Water Usage Monitor

> Replace all bracketed fields, add screenshots of your own execution, and
> adjust the headings to the official course report template before submission.

## Student details

- **Name:** Prakhar Kumar Singh
- **Registration number:** [Your registration number]
- **Course:** Introduction to Problem Solving using Python
- **Faculty:** [Faculty name]
- **Submission date:** [Date]
- **GitHub repository:** `https://github.com/[username]/aquaalert`

## 1. Abstract

AquaAlert is a command-line application that helps a household record
cumulative water-meter readings and understand changes in water consumption.
It calculates consumption between consecutive readings, produces summary
statistics, and compares recorded usage with a user-selected limit. When the
latest three records all exceed that limit, it displays a possible-leak warning.
The project is implemented in Python using functions, lists, dictionaries,
conditions, loops, date validation, and CSV file handling. Automated tests are
included for calculations, validation, alert logic, and data persistence.

## 2. Introduction

Water wastage can remain unnoticed when meter readings are not recorded or
compared. AquaAlert provides a small, understandable tool for manual monitoring.
Its purpose is awareness and early investigation rather than professional leak
diagnosis. The terminal interface keeps the project portable and suitable for
an introductory Python course.

## 3. Problem statement

Households require a simple way to record water-meter readings, calculate usage,
and receive a warning when consumption is repeatedly higher than a chosen
limit.

## 4. Objectives

1. Store valid, dated meter readings.
2. Calculate consumption between consecutive readings.
3. Summarize recorded consumption.
4. Detect high-usage records using a configurable limit.
5. Warn about a continuing three-record high-usage pattern.
6. Demonstrate introductory problem-solving and Python programming concepts.

## 5. Requirements and system design

The functional requirements, non-functional requirements, architecture,
workflow, use case diagram, component diagram, data design, and algorithms are
documented in [`DESIGN.md`](DESIGN.md). Export the diagrams as images for the
report if the official template does not support Mermaid diagrams.

## 6. Tools and technologies

- Python 3.9 or newer
- `csv`, `datetime`, and `pathlib` standard-library modules
- `unittest` for automated testing
- Git and GitHub for version control and public submission
- CSV for local persistent storage

No external Python package, database server, API key, or graphical setup is
required.

## 7. Implementation

The program has four logical areas:

1. **Storage:** `load_readings()` and `save_readings()` read and write CSV data.
2. **Validation:** `is_valid_date()` and `validate_new_reading()` reject invalid
   dates, duplicate dates, negative values, and inconsistent cumulative values.
3. **Analysis:** `calculate_usage()`, `calculate_summary()`, and `find_alerts()`
   calculate consumption and warnings.
4. **Interaction:** menu and display functions collect choices and show results.

The main formula is:

```text
consumption = current cumulative reading - previous cumulative reading
```

## 8. Testing and evaluation

Run the automated tests using:

```bash
python3 -m unittest -v
```

Complete this table using your own final execution results:

| Test area | Expected result | Observed result | Status |
|---|---|---|---|
| Consumption calculation | Correct difference | [Add result] | [Pass/Fail] |
| Summary calculation | Correct statistics | [Add result] | [Pass/Fail] |
| Invalid date | Rejected | [Add result] | [Pass/Fail] |
| Duplicate date | Rejected | [Add result] | [Pass/Fail] |
| High-usage alert | Values above limit listed | [Add result] | [Pass/Fail] |
| Three-record pattern | Warning displayed | [Add result] | [Pass/Fail] |
| CSV persistence | Data available after restart | [Add result] | [Pass/Fail] |

Add screenshots showing:

1. The main menu.
2. Successful entry of readings.
3. The usage table.
4. The summary.
5. A high-usage or possible-leak warning.
6. The automated test output.

## 9. Results and discussion

Record the dataset used, manually calculated expected values, AquaAlert's
outputs, and any differences. Discuss what the warning means and why repeated
high usage is only an indication—not proof—of a leak.

Do not invent evaluation results. Fill this section after running the final
version and collecting your own evidence.

## 10. Limitations

- Readings must be entered manually.
- The interval is daily only when one reading is entered each day.
- The threshold is selected by the user.
- The warning cannot distinguish a leak from legitimate heavy use.
- Only one local household dataset is supported.

## 11. Future scope

- Editing and deletion of incorrect records
- Multiple household profiles
- Optional charts and monthly reports
- Smart water-meter or flow-sensor integration
- More advanced anomaly detection based on historical patterns

## 12. Conclusion

AquaAlert demonstrates how a household problem can be divided into input,
validation, storage, calculation, and reporting tasks. It provides transparent
calculations and repeatable tests while remaining executable from a terminal
without external dependencies.

## 13. References

List only materials you actually consulted, using the citation format required
by the course. Possible categories include official Python documentation, water
conservation guidance, and course notes.

## 14. Originality declaration

I confirm that I reviewed, understood, tested, and can explain the submitted
source code and report. Any references or assistance used in developing the
project have been acknowledged according to the course rules.
