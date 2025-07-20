#!/usr/bin/env python3
"""
Author: Suhail Al‑aboud
Email: 10675@holbertonstudents.com
"""

import json
import csv
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"


def _load_json() -> list[dict]:
    """Load products from products.json and return a list of dicts."""
    with JSON_FILE.open(encoding="utf-8") as fp:
        return json.load(fp)


def _load_csv() -> list[dict]:
    """Load products from products.csv and return a list of dicts."""
    with CSV_FILE.open(encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        return [row for row in reader]


def get_products(source: str) -> list[dict] | None:
    """Return product list based on data source or None on invalid source."""
    if source == "json":
        return _load_json()
    if source == "csv":
        return _load_csv()
    return None


@app.route("/products")
def products():
    """
    Render products table based on query parameters:
    • source=[json|csv]  (required)
    • id=<int>           (optional)
    """
    source = request.args.get("source", "").lower()
    prod_list = get_products(source)

    # تحقّق من صحة معطى source
    if prod_list is None:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[],
        )

    # تحقّق من وجود معرّف id (اختياري)
    id_param = request.args.get("id")
    if id_param:
        filtered = [p for p in prod_list if str(p.get("id")) == id_param]
        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )
        prod_list = filtered

    return render_template("product_display.html", products=prod_list, error=None)


# نقطة انطلاق سريعة عند تشغيل الملف مباشرة
if __name__ == "__main__":
    app.run(debug=True, port=5000)
