#!/usr/bin/env python3
"""
Author: Suhail Al-aboud
Email: 10675@holbertonstudents.com
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any, Optional

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"


# ---------- Data Loaders ----------

def _load_json() -> List[Dict[str, Any]]:
    """Load products from JSON file."""
    with JSON_FILE.open(encoding="utf-8") as fp:
        data = json.load(fp)
    # Accept either list or {"products": [...]}
    return data if isinstance(data, list) else data.get("products", [])


def _load_csv() -> List[Dict[str, Any]]:
    """Load products from CSV file."""
    rows: List[Dict[str, Any]] = []
    with CSV_FILE.open(encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            # Normalize numeric fields
            try:
                row["id"] = int(row["id"])
            except (KeyError, ValueError):
                pass
            try:
                row["price"] = float(row["price"])
            except (KeyError, ValueError):
                pass
            rows.append(row)
    return rows


def get_products(source: str) -> Optional[List[Dict[str, Any]]]:
    """Return product list for a given source, or None if source invalid."""
    if source == "json":
        return _load_json()
    if source == "csv":
        return _load_csv()
    return None


# ---------- Flask Route ----------

@app.route("/products")
def products():
    """
    /products?source=[json|csv]&id=<optional int>
    """
    source = request.args.get("source", "").lower()
    prod_list = get_products(source)

    if prod_list is None:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=[])

    # Optional ID filter
    target_id = request.args.get("id")
    if target_id:
        prod_list = [p for p in prod_list if str(p.get("id")) == target_id]
        if not prod_list:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=[])

    return render_template("product_display.html",
                           products=prod_list,
                           error=None)


# ---------- Quick root (optional) ----------
@app.route("/")
def home():
    return "<p>Use /products?source=json|csv[&id=]</p>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
