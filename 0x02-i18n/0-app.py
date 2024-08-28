#!/usr/bin/env python3
"""
Flask app for serving a simple webpage.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Handle the root route by rendering the index page.
    :return: HTML content for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

