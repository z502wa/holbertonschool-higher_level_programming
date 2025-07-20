#!/usr/bin/env python3
"""
Author: Suhail Al‑aboud
Email: 10675@holbertonstudents.com
"""

import json
import csv
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"
DB_FILE = BASE_DIR / "products.db"


# ---------- Data Loaders ----------

def _load_json() -> List[Dict[str, Any]]:
    with JSON_FILE.open(encoding="utf-8") as fp:
        data = json.load(fp)
    return data if isinstance(data, list) else data.get("products", [])


def _load_csv() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with CSV_FILE.open(encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            row["id"] = int(row.get("id", 0))
            row["price"] = float(row.get("price", 0))
            rows.append(row)
    return rows


def _load_sql() -> List[Dict[str, Any]]:
    if not DB_FILE.exists():
        return []
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT id, name, category, price FROM Products")
        records = cur.fetchall()
        return [
            {
                "id": rec["id"],
                "name": rec["name"],
                "category": rec["category"],
                "price": rec["price"],
            }
            for rec in records
        ]
    except sqlite3.Error as exc:
        raise RuntimeError(f"Database error: {exc}") from exc
    finally:
        try:
            conn.close()
        except Exception:
            pass


def get_products(source: str) -> Optional[List[Dict[str, Any]]]:
    if source == "json":
        return _load_json()
    if source == "csv":
        return _load_csv()
    if source == "sql":
        return _load_sql()
    return None


# ---------- Flask Routes ----------

@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    prod_list: Optional[List[Dict[str, Any]]]
    try:
        prod_list = get_products(source)
    except RuntimeError as e:
        return render_template("product_display.html", error=str(e), products=[])

    if prod_list is None:
        return render_template("product_display.html", error="Wrong source", products=[])

    target_id = request.args.get("id")
    if target_id:
        prod_list = [p for p in prod_list if str(p.get("id")) == target_id]
        if not prod_list:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=[])

    return render_template("product_display.html", products=prod_list, error=None)


@app.route("/")
def home():
    return "<p>Use /products?source=json|csv|sql[&id=]</p>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
