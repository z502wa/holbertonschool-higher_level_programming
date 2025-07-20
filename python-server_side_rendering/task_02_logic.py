#!/usr/bin/env python3
"""
Author: Suhail Al‑aboud
Email: 10675@holbertonstudents.com
"""

import json
from pathlib import Path
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("items.json")


def load_items():
    """Read the JSON file and return the list of items (or an empty list)."""
    try:
        with DATA_FILE.open(encoding="utf-8") as fp:
            payload = json.load(fp)
            # Expecting {"items": [...]}; fall back to []
            return payload.get("items", [])
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        # Log the error in real apps; for now abort with 500
        abort(500, description=f"Data file error: {exc}")


@app.route("/items")
def items():
    """Render the items list page."""
    return render_template("items.html", items=load_items())


# Optional: keep previously implemented pages working when you run this file alone
@app.route("/")
def home():
    return "<p>Home – go to <a href='/items'>/items</a></p>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
