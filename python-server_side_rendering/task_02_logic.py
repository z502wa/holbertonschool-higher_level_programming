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
    """Return the list of items from items.json (empty list on error)."""
    try:
        with DATA_FILE.open(encoding="utf-8") as fp:
            payload = json.load(fp)
            return payload.get("items", []) if isinstance(payload, dict) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


# ---- Basic pages needed by header.html ----
@app.route("/")
def home():
    return "<p>Home page</p>"


@app.route("/about")
def about():
    return "<p>About page</p>"


@app.route("/contact")
def contact():
    return "<p>Contact page</p>"


# ---- Task‑02 endpoint ----
@app.route("/items")
def items():
    """Render the dynamic items list (shows 200 even if list is empty)."""
    return render_template("items.html", items=load_items())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
