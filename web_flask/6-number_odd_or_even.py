#!/usr/bin/python3
"""Start a flask application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display 'C' followed by route param"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display 'Python' followed by route param"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display 'n is a number' if true"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display an HTML page if n is a number"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page if n is a number"""
    return render_template(
        "6-number_odd_or_even.html", number=n,
        odd_or_even="even" if (n % 2 == 0) else "odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
""
