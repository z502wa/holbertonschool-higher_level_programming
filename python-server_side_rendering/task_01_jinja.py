#!/usr/bin/env python3
"""
Author: Suhail Al-aboud
Email: 10675@holbertonstudents.com
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    """Render home page"""
    return render_template("index.html")

@app.route("/about")
def about():
    """Render about page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Render contact page"""
    return render_template("contact.html")

if __name__ == "__main__":
    # Run on localhost:5000 with debug enabled
    app.run(debug=True, port=5000)
