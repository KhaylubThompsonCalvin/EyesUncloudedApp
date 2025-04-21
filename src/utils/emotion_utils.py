"""
Emotion Utilities for Eyes Unclouded App

Contains all core logic for decoding, logging, summarizing, and plotting microexpressions.
"""

from pathlib import Path
import os
import json
import csv
from collections import defaultdict, Counter
from datetime import datetime
import matplotlib.pyplot as plt

# Base of the project (three levels up from this file: src/utils/emotion_utils.py → project root)
BASE_PATH = Path(__file__).parent.parent.parent

EXPRESSIONS_PATH = BASE_PATH / "src" / "views" / "static" / "images" / "expressions"
LOG_PATH         = BASE_PATH / "logs" / "emotion_log.json"
CSV_PATH         = BASE_PATH / "logs" / "emotion_log.csv"
CHART_PATH       = BASE_PATH / "logs" / "chart.png"

UNIVERSAL_EMOTIONS = [
    "anger", "contempt", "disgust", "fear",
    "happiness", "neutral", "sadness", "surprise"
]

DESCRIPTIONS = {
    "anger":      "Triggered by perceived injustice or threat. Observable in lowered brows and glaring eyes.",
    "contempt":   "A unilateral expression of superiority—one corner of the mouth raised.",
    "disgust":    "An aversion response—nose wrinkle and upper lip raise signal repulsion.",
    "fear":       "Evolutionarily tied to survival; wide eyes and raised eyelids signal potential danger.",
    "happiness":  "Marked by Duchenne smile—eye crinkles and lip raise linked to reward pathways.",
    "neutral":    "Baseline state—used for comparison or when emotion is suppressed.",
    "sadness":    "Signals loss or empathy; inner brow raise and downward mouth angle.",
    "surprise":   "Heightened alertness—raised brows and dropped jaw reflect sudden stimulus."
}


def get_expression_counts() -> dict[str,int]:
    """Count how many images exist for each universal emotion."""
    counts: dict[str,int] = defaultdict(int)
    for fn in os.listdir(EXPRESSIONS_PATH):
        emo = fn.split("_")[0].lower()
        if emo in UNIVERSAL_EMOTIONS:
            counts[emo] += 1
    return dict(counts)


def describe_emotion(emotion: str) -> str:
    """Return the neuroscience‐based interpretation of a given emotion."""
    return DESCRIPTIONS.get(emotion.lower(), "Unknown emotion.")


def verify_labels() -> list[str]:
    """Return list of files whose prefix isn’t a known universal emotion."""
    invalid: list[str] = []
    for fn in os.listdir(EXPRESSIONS_PATH):
        if fn.split("_")[0].lower() not in UNIVERSAL_EMOTIONS:
            invalid.append(fn)
    return invalid


def log_emotion(emotion: str) -> None:
    """Append an emotion with UTC timestamp to the JSON log."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {"emotion": emotion.lower(), "timestamp": datetime.utcnow().isoformat()}
    if LOG_PATH.exists():
        logs = json.loads(LOG_PATH.read_text())
    else:
        logs = []
    logs.append(entry)
    LOG_PATH.write_text(json.dumps(logs, indent=2))


def summarize_log() -> None:
    """Print total, most common emotion, and time range from JSON log."""
    if not LOG_PATH.exists():
        print("No log file found."); return

    logs = json.loads(LOG_PATH.read_text())
    if not logs:
        print("Log file is empty."); return

    total = len(logs)
    counts = Counter(e["emotion"] for e in logs)
    most, freq = counts.most_common(1)[0]
    timestamps = [e["timestamp"] for e in logs]

    print(f"Total observations: {total}")
    print(f"Most logged emotion: {most} ({freq} times)")
    print("Time range:")
    print(f"  Start: {timestamps[0]}")
    print(f"  End:   {timestamps[-1]}")


def plot_chart() -> None:
    """Save a bar chart of image‐count per emotion to disk."""
    counts = get_expression_counts()
    emotions, values = zip(*sorted(counts.items()))
    plt.figure(figsize=(8,4))
    plt.bar(emotions, values)
    plt.title("Microexpression Image Count")
    plt.xlabel("Emotion")
    plt.ylabel("Count")
    plt.tight_layout()

    CHART_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(CHART_PATH)
    plt.close()
    print(f"Chart saved to: {CHART_PATH}")


def clear_log() -> None:
    """Erase all entries from the JSON log."""
    if LOG_PATH.exists():
        LOG_PATH.write_text("[]")
        print("Emotion log cleared.")
    else:
        print("No emotion log to clear.")


def export_csv() -> None:
    """Convert the JSON log into a CSV file."""
    if not LOG_PATH.exists():
        print("No JSON log to export."); return

    logs = json.loads(LOG_PATH.read_text())
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_PATH, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["emotion", "timestamp"])
        writer.writeheader()
        writer.writerows(logs)
    print(f"Exported log to CSV at: {CSV_PATH}")


def observe_mode() -> None:
    """Interactive CLI loop to log emotions until 'exit' is typed."""
    print("Entering observer mode (type 'exit' to quit):")
    while True:
        emo = input("Enter observed emotion: ").strip().lower()
        if emo == "exit":
            break
        if emo not in UNIVERSAL_EMOTIONS:
            print("Invalid emotion. Choose from:", ", ".join(UNIVERSAL_EMOTIONS))
        else:
            log_emotion(emo)
            print(f"Logged: {emo}")
