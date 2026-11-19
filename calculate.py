"""Summarize observed pass rates and bounds for aggregated evaluation counts."""
import csv
from pathlib import Path


def rate(passes, denominator):
    return f"{passes}/{denominator} ({100 * passes / denominator:.1f}%)" if denominator else "undefined"


def main():
    with Path(__file__).with_name("checks.csv").open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            assigned, passed, failed, unread = (int(row[k]) for k in ("assigned", "passed", "failed", "unread"))
            if min(assigned, passed, failed, unread) < 0 or passed + failed + unread != assigned:
                raise ValueError(f"Inconsistent counts for {row['system']}")
            print(f"{row['system']} | assigned {rate(passed, assigned)} | graded {rate(passed, passed + failed)}"
                  f" | possible passes {passed}–{passed + unread}")


if __name__ == "__main__":
    main()
