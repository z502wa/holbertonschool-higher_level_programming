#!/usr/bin/env python3
"""
Author: Suhail Al-aboud
Email: 10675@holbertonstudents.com
"""

import json
import csv
import sqlite3
from pathlib import Path
from typing import List, Dict, Any
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"
DB_FILE = BASE_DIR / "products.db"


# ---------- Data Loaders (JSON / CSV / SQLite) ----------

def _load_json() -> List[Dict[str, Any]]:
    """Load products from JSON file."""
    with JSON_FILE.open(encoding="utf-8") as fp:
        data = json.load(fp)
        # Expect either a list of objects or an object containing a list
        if isinstance(data, list):
            return data
        # Fallback if user used {"products": [...]}
        return data.get("products", [])


def _load_csv() -> List[Dict[str, Any]]:
    """Load products from CSV file."""
    with CSV_FILE.open(encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        # Cast numeric fields if needed
        rows = []
        for row in reader:
            # Normalize id & price to proper types
            try:
                row["id"] = int(row.get("id"))
            except (TypeError, ValueError):
                pass
            try:
                row["price"] = float(row.get("price"))
            except (TypeError, ValueError):
                pass
            rows.append(row)
        return rows


def _load_sql() -> List[Dict[str, Any]]:
    """Load products from SQLite database."""
    if not DB_FILE.exists():
        # Return empty list (route logic will show 'Product not found' only if filtered;
        # for full listing this will just be empty table)
        return []
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # Access columns by name
        cur = conn.cursor()
        cur.execute("SELECT id, name, category, price FROM Products")
        rows = cur.fetchall()
        products = []
        for r in rows:
            products.append({
                "id": r["id"],
                "name": r["name"],
                "category": r["category"],
                "price": r["price"],
            })
        return products
    except sqlite3.Error as exc:
        # In a real app you might log the error; here we re-raise to handle upstream
        raise RuntimeError(f"Database error: {exc}") from exc
    finally:
        try:
            conn.close()
        except Exception:
            pass


def get_products(source: str) -> List[Dict[str, Any]] | None:
    """
    Dispatch loader based on source.
    Returns list of dicts or None if invalid source.
    May raise RuntimeError on DB errors.
    """
    if source == "json":
        return _load_json()
    if source == "csv":
        return _load_csv()
    if source == "sql":
        return _load_sql()
    return None


# ---------- Flask Route ----------

@app.route("/products")
def products():
    """
    Query parameters:
      source = json | csv | sql   (required)
      id     = <int>               (optional)
    Behavior:
      - If invalid source -> "Wrong source"
      - If id provided and not found -> "Product not found"
      - DB errors -> show error message
    """
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id")

    try:
        prod_list = get_products(source)
    except RuntimeError as e:
        # Database-related error surfaced
        return render_template(
            "product_display.html",
            error=str(e),
            products=[]
        )

    if prod_list is None:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    # Filter by id if provided
    if id_param:
        filtered = [p for p in prod_list if str(p.get("id")) == id_param]
        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )
        prod_list = filtered

    return render_template("product_display.html", products=prod_list, error=None)


# ---------- Quick Root (optional) ----------
@app.route("/")
def home():
    return (
        "<p>Use /products?source=json | csv | sql "
        "and optionally &id=NUMBER</p>"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
