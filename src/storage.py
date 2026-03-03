import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")


def ensure_data_file_exists() -> None:
    """Create data folder and empty JSON file if missing."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_expenses() -> list[dict]:
    """Load expenses list from JSON file."""
    ensure_data_file_exists()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if not content:
            return []

        expenses = json.loads(content)
        return expenses if isinstance(expenses, list) else []

    except json.JSONDecodeError:
        # If the JSON file is corrupted, recover with an empty list.
        return []


def save_expenses(expenses: list[dict]) -> None:
    """Save expenses list to JSON file."""
    ensure_data_file_exists()

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)
