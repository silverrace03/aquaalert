# AquaAlert Evaluation Record

**Evaluation date:** 24 September 2026  
**Application mode:** Command line  
**Python dependencies:** Standard library only

## Automated test result

Command executed from the repository root:

```bash
python3 -m unittest -v
```

Result: **8 tests passed, 0 failed**.

The tests covered:

1. Usage calculation from cumulative readings
2. Total, average, and monthly estimate calculations
3. Insufficient data handling
4. Date-format and impossible-date validation
5. High-usage and possible-leak detection
6. Duplicate-date rejection
7. Decreasing and negative meter-reading rejection
8. CSV save/load consistency

## End-to-end scenario

The following cumulative readings were entered through the interactive menu:

| Date | Meter reading (L) | Calculated usage (L) |
|---|---:|---:|
| 2026-09-20 | 1000 | Not applicable |
| 2026-09-21 | 1300 | 300 |
| 2026-09-22 | 1650 | 350 |
| 2026-09-23 | 2050 | 400 |

Expected and observed summary:

| Measurement | Expected | Observed | Result |
|---|---:|---:|---|
| Total usage | 1050 L | 1050 L | Pass |
| Average usage | 350 L | 350 L | Pass |
| Estimated monthly use | 10500 L | 10500 L | Pass |
| Highest usage | 400 L on 2026-09-23 | 400 L on 2026-09-23 | Pass |
| Lowest usage | 300 L on 2026-09-21 | 300 L on 2026-09-21 | Pass |

With the usage limit set to 200 litres, all three calculated usage records were
correctly listed as high usage. Because the latest three records exceeded the
limit, the program displayed the possible-leak warning as expected.

## Interpretation

The evaluation verifies the implemented arithmetic and rule-based behavior. It
does not demonstrate that the program can diagnose a real plumbing leak. Such a
claim would require sensor data and confirmed real-world leak events.
