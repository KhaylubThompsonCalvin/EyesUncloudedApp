"""
Microexpression Decoder Module – Eyes Unclouded App
Purpose: Maps facial images to universal emotions based on neuroscience & Ekman's research.
Inspired by: Dr. Paul Ekman’s FACS + 'Lie to Me' (Lightman Group Deduction Model)

Author: Khaylub Thompson-Calvin
Date: 2025-04-18
"""

#!/usr/bin/env python3
"""
Microexpression Decoder CLI – Eyes Unclouded App

Wraps all emotion_utils functions behind a simple command‐line interface.
"""

import argparse
from src.utils.emotion_utils import (
    get_expression_counts, describe_emotion, verify_labels,
    log_emotion, summarize_log, plot_chart,
    clear_log, export_csv, observe_mode
)


def main():
    parser = argparse.ArgumentParser(
        description="Decode & track microexpressions via CLI."
    )

    parser.add_argument("--filter",     help="Show count + interpretation for one emotion")
    parser.add_argument("--describe",   help="Show interpretation of one emotion")
    parser.add_argument("--count",      action="store_true", help="List all image‐counts")
    parser.add_argument("--verify",     action="store_true", help="Check for mislabeled files")
    parser.add_argument("--log",        help="Log a decoded emotion")
    parser.add_argument("--summary",    action="store_true", help="Summarize logged data")
    parser.add_argument("--chart",      action="store_true", help="Save bar chart of counts")
    parser.add_argument("--clear-log",  action="store_true", help="Erase the JSON log")
    parser.add_argument("--export-csv", action="store_true", help="Export log to CSV")
    parser.add_argument("--observe",    action="store_true", help="Interactive observation mode")

    args = parser.parse_args()

    if args.filter:
        emo = args.filter.lower()
        counts = get_expression_counts()
        print(f"{emo.title()}: {counts.get(emo, 0)} images")
        print("Interpretation:", describe_emotion(emo))

    elif args.describe:
        print("Interpretation:", describe_emotion(args.describe.lower()))

    elif args.count:
        for e, c in get_expression_counts().items():
            print(f"{e.title()}: {c}")

    elif args.verify:
        invalid = verify_labels()
        if invalid:
            print("Invalid files:", *invalid, sep="\n  - ")
        else:
            print("All files correctly labeled.")

    elif args.log:
        log_emotion(args.log.lower())

    elif args.summary:
        summarize_log()

    elif args.chart:
        plot_chart()

    elif args.clear_log:
        clear_log()

    elif args.export_csv:
        export_csv()

    elif args.observe:
        observe_mode()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
