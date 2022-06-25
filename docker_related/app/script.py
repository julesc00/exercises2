import os
import logging
from datetime import date

from flask import Flask

# app = Flask(__name__)


def get_logs():
    with open("logs.txt", "r") as f:
        print(f.read())
        names = f.read().split("\n")
        print(names)
    return names


# @app.route("/")
# def home():

if __name__ == "__main__":
    print(get_logs())
